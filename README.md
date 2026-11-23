# Sites vitrines

Ce dépôt contient deux versions du site, chacune dans son dossier et indépendante de l'autre :

| Dossier | Version |
|---|---|
| `SitePACouverture/` | **P.A Couverture** : couvreur, charte bleue |
| `SitePARenovation/` | **PA Rénovation** : rénovation intérieure et extérieure, charte orange |

Chaque dossier a son propre `README.md`, ses dépendances, son serveur et ses données. Pour lancer l'un d'eux :

```bash
cd SitePARenovation      # ou SitePACouverture
npm install
npm run set-admin
npm start
```
