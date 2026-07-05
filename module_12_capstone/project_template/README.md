# <Your Capstone Project>

> Starter scaffold. Copy this whole folder to a new location and build your capstone
> here. Replace this README with a real one describing YOUR project.

## Structure

```
project_template/
├── README.md          <- this file (rewrite it for your project)
├── requirements.txt   <- pin your dependencies here
├── main.py            <- entry point; the pipeline skeleton lives here
├── data/              <- put datasets here (git-ignore large files)
├── src/               <- your modules (data loading, model, evaluation)
├── results/           <- plots, metrics, and outputs get written here
└── writeup.md         <- your report (copy from ../writeup_template.md)
```

## Run

```bash
pip install -r requirements.txt
python main.py
```

## Checklist before you call it done
- [ ] Beats a stated baseline on the right metric (not just accuracy).
- [ ] Evaluated on unseen data / cross-validation; no leakage.
- [ ] Ethics component done (bias audit / adversarial test / injection test).
- [ ] `writeup.md` complete; results reproducible from a clean checkout.
- [ ] Ran `../../module_11_ethics/red_team_checklist.md` on your own model.
