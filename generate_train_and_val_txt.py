#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
instructions:
__filename = "generate_train_and_val_txt.py"
__time__ = "2024/07/12 14:47"
__author__ = "Gu Pengli"
__email__ = "pengli.gu@hopechart.com"
__version__ = "1.0.0"
__license__ = "MIT"
"""
import os
import random


def get_image_paths(directory):
    """Recursively get all image paths from the given directory."""
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    image_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_paths.append(os.path.splitext(os.path.join(root, file))[0])
    return image_paths


def write_paths_to_file(paths, filename):
    """Write the given paths to a file."""
    with open(filename, 'w') as file:
        for path in paths:
            file.write(f"{path}\n")


def main():
    # Directory containing the images
    directory = '/mnt/f/datasets/300W_LP'

    # Get all image paths
    image_paths = get_image_paths(directory)

    # Shuffle the image paths
    random.shuffle(image_paths)

    class_rate = 0.9
    # Split the image paths into training and testing sets (90% train, 10% test)
    split_index = int(class_rate * len(image_paths))
    train_paths = image_paths[:split_index]
    test_paths = image_paths[split_index:]

    # Write the paths to train.txt and test.txt
    write_paths_to_file(train_paths, 'train.txt')
    write_paths_to_file(test_paths, 'test.txt')

    print(f"Total images: {len(image_paths)}")
    print(f"Training images: {len(train_paths)}")
    print(f"Testing images: {len(test_paths)}")


if __name__ == '__main__':
    main()
