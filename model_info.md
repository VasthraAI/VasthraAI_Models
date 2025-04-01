# Model information

- This document contains in detail information about each model and their differences.
- It also discusses some basic information about how GAN model architecure, and how they work.

# Generative Aderserial Networks (GANs)

Generative Adversarial Networks (GANs) are a class of machine learning models designed to generate new data similar to the training set. Introduced by Ian Goodfellow and colleagues in 2014, GANs consist of two neural networks that are trained simultaneously in a competitive setting.

### How Do GANs Work?

- GANs have two main components:

#### Generator

- This network takes random noise as input and generates fake data (e.g., images, audio).

#### Discriminator

- This network evaluates whether a given sample is real (from the true dataset) or fake (produced by the generator).

### Training Process

- The two networks are trained in opposition:

**Generator Goal**: To "fool" the discriminator by producing data that looks as real as possible.

**Discriminator Goal**: To correctly distinguish real data from fake data.
The process can be broken down into steps:

**Step 1**: The generator creates fake data from random noise.
**Step 2**: The discriminator is fed both real data (from the dataset) and fake data (from the generator) and tries to classify them.
**Step 3**: The discriminator provides feedback:
If it correctly identifies real vs. fake, it improves its ability to detect.
If it’s fooled by the generator, the generator learns how to improve its output.
**Step 4**: Both networks update their parameters through backpropagation, and the cycle repeats.

### The Adversarial Dynamic

This setup creates a "game" between the generator and discriminator:

- The generator gets better at creating realistic data.
- The discriminator gets better at spotting fakes.
- Over time, they reach an equilibrium where the generator produces highly realistic outputs.

## Applications

GANs are widely used for:

- Generating realistic images (e.g., faces, artwork).
- Image-to-image translation (e.g., turning sketches into photos).
- Data augmentation (creating synthetic data for training).

## Challenges

- **Training Instability**: Balancing the generator and discriminator can be tricky.
- **Mode Collapse**: The generator might produce limited varieties of outputs.

In essence, GANs are like an artist (generator) and a critic (discriminator) working together—or against each other—to create something new and convincing!

---

# Models

## **GEN_1**

### Model Architecture

This GAN consits of the follwoing:

1. A Generator that translates sketches to images.
2. A Discriminator that evaluates the realism of generated images.

### Generator

The Generator follows a U-Net structure:

**Encoder:** Extracts high-level features from sketches.
**Bottleneck:** Latent representation.
**Decoder:** Upscales features to generate a high-quality image.

```
class Generator(nn.Module):
    def __init__(self, input_channels=1, output_channels=3, num_residual_blocks=6):
        super(Generator, self).__init__()
        self.conv1 = nn.Conv2d(input_channels, 64, kernel_size=7, stride=1, padding=3)
        self.bn1 = nn.BatchNorm2d(64)

        self.res_blocks = nn.Sequential(*[ResidualBlock(64) for _ in range(num_residual_blocks)])

        self.conv2 = nn.Conv2d(64, output_channels, kernel_size=7, stride=1, padding=3)
        self.tanh = nn.Tanh()

    def forward(self, x):
        x = F.relu(self.bn1(self.conv1(x)))
        x = self.res_blocks(x)
        x = self.tanh(self.conv2(x))
        return x
```

### Discriminator

The Discriminator is a PatchGAN:

* Instead of classifying an image as real or fake, it looks at small patches.
* Outputs a 63×63 matrix (each value is the probability of realism for that patch).

```
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(128, 1, kernel_size=4, stride=1, padding=1),
            nn.Sigmoid()  # Output probability of real/fake
        )

    def forward(self, x):
        return self.model(x)
```

Instead of just looking at global realism, patchGAN examines textures locally. It works well for fine-grained details like batik patterns.

#### Residual Blocks

* Residual Blocks are used to help retain details in generated images. It reduces vanishing gradient problems.

```
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x):
        residual = x
        x = F.relu(self.bn1(self.conv1(x)))
        x = self.bn2(self.conv2(x))
        return F.relu(x + residual)
```


## GEN_2

## GEN_3

## GEN_4

## GEN_5
