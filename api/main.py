import os
import django
from fastapi import FastAPI, HTTPException, Response
from typing import List

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TheForestWiki.settings")
django.setup()

from core.models import Comentario
from django.contrib.auth import get_user_model
from api.schemas import CommentaryIn, CommentaryOut, UserOut
from api.utils import serialize_comment, serialize_user

app = FastAPI(title="The Forest Wiki API")

# Endpoint de ping
@app.get("/ping")
async def pong():
    return {"ping": "pong"}

# Endpoints de Comentarios
@app.get("/comentarios/", response_model=List[CommentaryOut])
def list_comments():
    qs = (Comentario.objects
          .filter(parent__isnull=True)
          .select_related("usuario")
          .prefetch_related("replies__usuario")
          .order_by("-created"))
    return [serialize_comment(c) for c in qs]

@app.post("/comentarios/", response_model=CommentaryOut)
def create_comment(payload: CommentaryIn):
    User = get_user_model()
    usuario = User.objects.first()
    c = Comentario.objects.create(
        content=payload.content,
        parent_id=payload.parent,
        usuario=usuario
    )
    return serialize_comment(c)

@app.put("/comentarios/{pk}/", response_model=CommentaryOut)
def update_comment(pk: int, payload: CommentaryIn):
    try:
        c = Comentario.objects.get(pk=pk)
    except Comentario.DoesNotExist:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    c.content = payload.content
    c.parent_id = payload.parent
    c.save()
    return serialize_comment(c)

@app.delete("/comentarios/{pk}/", status_code=204)
def delete_comment(pk: int):
    try:
        Comentario.objects.get(pk=pk).delete()
    except Comentario.DoesNotExist:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return Response(status_code=204)

# Endpoints de Usuarios
User = get_user_model()

@app.get("/usuarios/", response_model=List[UserOut])
def list_users():
    qs = User.objects.order_by("date_joined")
    return [serialize_user(u) for u in qs]

@app.get("/usuarios/{pk}/", response_model=UserOut)
def get_user(pk: int):
    try:
        u = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return serialize_user(u)