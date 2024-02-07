# Theia (v0.1.3-dev0)

Bleed-Through Correction in Fluorescent Microscopy Images

## Installation

### Linux

- From PyPI: `pip install "theia-py==0.1.3-dev0"`
- Using poetry: `poetry add theia-py@0.1.3-dev0`

### MacOS (Apple Silicon)

1. Install xcode command line tools:
   - `xcode-select --install`
2. Install miniforge:
   - [Instructions](https://github.com/conda-forge/miniforge)
3. Disable the `base` conda environment from activating by default:
  - `conda config --set auto_activate_base false`
4. Install poetry:
  - `curl -sSL https://install.python-poetry.org | python3 -`
  - Add poetry to your path using the hint provided by the poetry installer.
5. Create a conda environment:
  - `conda create -n theia python=3.9`
  - `conda activate theia`
6. Install tensorflow dependencies:
  - `conda install -c apple tensorflow-deps`
7. Install using poetry:
  - `poetry add theia-py@0.1.3-dev0`

### Windows

1. Re-evaluate your life choices.
2. Install Linux.
3. Read this document from the beginning.

## Usage

Here is a simple example of how to use Theia to correct a set of images.
For a more detailed example, see the streamlit app in `examples/rxrx.py`.

```python
import theia

# Load training and validation images
train_images = ...
valid_images = ...

# Make a tile-generator for feeding the model
train_generator = theia.TileGenerator(train_images, tile_size=(256, 256), normalize=False)
valid_generator = theia.TileGenerator(valid_images, tile_size=(256, 256), normalize=False)

# Build the model
model = theia.models.Neural(
    num_channels=...,
    channel_overlap=1,
    kernel_size=5,
    alpha=1,
    beta=1,
    tile_size=256,
)
model.early_stopping(
    min_delta=1e-3,
    patience=4,
    verbose=1,
    restore_best_weights=True,
)
model.compile(optimizer="adam")
model.fit_theia(
    train_gen=train_gen,
    valid_gen=valid_gen,
    epochs=128,
    verbose=1,
)

# Get the transformer
transformer = model.transformer

# Correct and save the images
for image in train_images + valid_images:
    corrected_image = transformer.transform(image, remove_interactions=True)
    with open("<path-to-image>", "w") as f:
        ...
```
