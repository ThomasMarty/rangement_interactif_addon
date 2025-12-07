# Add-on: rangement_interactif


Add-on Home Assistant for managing an interactive storage wall (cartons / blocs / tiroirs).


**Fonctionnalités**
- Base SQLite embarquée (génération automatique des tiroirs selon dimensions des blocs)
- API REST (GET/POST) : blocs / tiroirs / objets / positions / recherche
- Interface web intégrée (UI interactive, drag & drop pour changer positions)
- Endpoint `/highlight` pour demander une mise en évidence (utile via Home Assistant automation)


**Installation (manuel)**
1. Sur ta machine locale, crée un dossier `rangement_interactif`.
2. Copie tous les fichiers du repo (ce qui est dans ce add-on) dans ce dossier.
3. Sur Home Assistant, va dans Supervisor → Add-on Store → Trois points → Repositories → "Create" ou alors installe localement :
- Copie le dossier dans `/addons/rangement_interactif` sur le stockage de Home Assistant (via Samba share ou File Editor si disponible).
4. Dans Supervisor → Add-on Store → click on the three dots → "Install from local" (ou trouve l'add-on si tu as mis correctement le dossier).
5. Démarre l'add-on.


**Endpoints principaux**
- `GET /api/blocs` — liste des blocs (id, rows, cols, type)
- `GET /api/positions` — position actuelle des blocs (row, col)
- `POST /api/positions` — modifier positions (payload: {"id":"A2","row":3,"col":1})
- `GET /api/tiroirs` — liste de tous les tiroirs
- `GET /api/objets` — liste des objets
- `POST /api/objets` — ajouter / modifier objet
- `GET /api/search?q=...` — rechercher objets
- `POST /api/highlight` — demande de mise en évidence (payload: {"tiroir_id":"A2-3","color":"#ff0000","duration":5000})


**Intégration Home Assistant**
Exemple d'appel REST dans une automation ou un script :


```yaml
script:
highlight_tiroir:
sequence:
- service: rest_command.highlight_tiroir


rest_command:
highlight_tiroir:
url: "http://homeassistant.local:8123/api/hassio_ingress/ADDON_ID/api/highlight"
method: POST
content_type: 'application/json'
payload: '{"tiroir_id":"A2-3","color":"#00ff00","duration":3000}'
