<p align="center">
  <img src="./assets/profile-hero.gif" width="800" alt="Animated pixel-art night sky over a lake, with twinkling stars and a figure fishing">
</p>

<p align="center"><img src="./assets/ui/profile-nameplate.svg" width="800" alt="Rohan Purohit"></p>

<p align="center"><strong>Trying to explore stuff, one step at a time.</strong></p>

<p align="center">
  <a href="https://rohan-purohit.vercel.app"><img src="./assets/ui/button-portfolio.svg" width="126" height="38" alt="Visit my portfolio"></a>
  <a href="https://linkedin.com/in/rohan-purohit-b65062277"><img src="./assets/ui/button-linkedin.svg" width="124" height="38" alt="Connect on LinkedIn"></a>
</p>

<p align="center"><a href="https://github.com/ARPurohit07?tab=repositories">Browse all repositories →</a></p>

---

### Featured work

#### 01 / Milky Way Star Map &nbsp; `C++` `WebAssembly` `WebGL2`

**An explorable map of our stellar neighbourhood.** Catalogue-based star positions from HYG and Gaia sit within a procedural galaxy field. I brought the C++ renderer into the browser with WebAssembly and WebGL2, then added search and shareable views.

**[Explore the live map →](https://star-map-three.vercel.app)**

<p align="center"><img src="./assets/galaxy-sol-view.png" width="800" alt="Actual Milky Way Star Map view showing nearby stars, labels, and a spatial grid"></p>

#### 02 / RocketRL &nbsp; `Python` `MuJoCo` `PPO`

**Teach a rocket to land in three dimensions.** A Pythia-70M-based PPO policy controls the engine and two steering axes in a MuJoCo simulation. The repository reports **373 landings in 400 untouched evaluation starts**, with separate development seeds used to select the checkpoint.

**[Explore RocketRL →](https://github.com/ARPurohit07/RocketRL)**

<p align="center"><img src="./assets/rocketrl-landing.gif" width="800" alt="Animated illustration of a rocket descending onto a landing pad, pausing, then rising for the next loop"></p>
<p align="center"><sub>Simulation illustration. Code is public; model checkpoints currently require access to a private release.</sub></p>

#### 03 / Military Drone Detection &nbsp; `PyTorch` `Faster R-CNN` `Streamlit`

**Detect the drone; treat its origin as a hypothesis.** Two separate Faster R-CNN models locate drones and rank possible airframe design or manufacturing countries. Their boxes are paired by overlap, so uncertain origin labels cannot suppress a binary drone alert. Held-out testing reports **0.9503 mAP@0.5** for binary detection and documents false positives on unseen bird flocks.

**[See the models, evaluation, and limitations →](https://github.com/ARPurohit07/Military-Drone-Detection-System)**

<p align="center"><img src="./assets/drone-detection-card.svg" width="800" alt="Illustration of separate drone and country detectors, with boxes paired by overlap for ranked origin candidates"></p>
<p align="center"><sub>Pipeline illustration. Datasets and model checkpoints are not included in the public repository.</sub></p>

#### 04 / GoodFlow &nbsp; `React` `TypeScript` `FastAPI` `Ollama`

**Turn a workflow image into a diagram you can actually edit.** Qwen2.5-VL reads the image locally. A React Flow canvas stays in sync with Mermaid text, and the result can be exported as Mermaid, SVG, PNG, or JSON.

**[View the open-source project →](https://github.com/ARPurohit07/GoodFlow)**

<p align="center"><img src="./assets/goodflow-card.svg" width="800" alt="Illustration of a workflow screenshot becoming an editable diagram through a local model"></p>
<p align="center"><sub>Workflow illustration; see the repository for the application.</sub></p>

#### 05 / GaiaRAG &nbsp; `Python` `DuckDB` `Ollama`

**Ask questions about the stars, with every number traceable to a catalogue row.** This companion to the star map combines SQL-backed catalogue facts with source documents. Deterministic checks catch unsupported numbers; when evidence is missing, the local system abstains.

**[Read the engineering notes and source →](https://github.com/ARPurohit07/GaiaRAG)**

<p align="center"><img src="./assets/gaiarag-flow.svg" width="800" alt="GaiaRAG architecture: a question is checked against catalogue rows and source documents before a grounded answer is returned"></p>

---

<p align="center"><a href="https://github.com/ARPurohit07?tab=repositories">See the rest of my projects →</a></p>
