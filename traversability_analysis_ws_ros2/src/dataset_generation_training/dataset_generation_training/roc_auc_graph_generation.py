import json
import matplotlib.pyplot as plt

# Load the history
history_filename = '/home/charlie/traversability_analysis_ws_ros2/src/dataset_generation_training/output/traversability_husky_b150_spe_50_e_10_patch_60_acc_XX_history.json'  # Update this path
with open(history_filename, 'r') as f:
    history = json.load(f)

# Plot settings
plt.figure(figsize=(14, 6))  # Increase figure size for better readability

# Plot training & validation accuracy
plt.subplot(1, 2, 1)
plt.plot(history['accuracy'], label='Training Accuracy')
plt.plot(history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])  # Adjust based on your accuracy values if needed
plt.legend(loc='lower right')
plt.grid(True)

# Plot training & validation loss
plt.subplot(1, 2, 2)
plt.plot(history['loss'], label='Training Loss')
plt.plot(history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim(bottom=0)  # Adjust based on your loss values if needed
plt.legend(loc='upper right')
plt.grid(True)

plt.tight_layout()  # Automatically adjust subplot params to give specified padding
plt.show()

# Optional: Plot AUC if available
if 'val_auc' in history:
    plt.figure(figsize=(7, 5))
    plt.plot(history['val_auc'], label='Validation AUC')
    plt.title('Validation AUC Score per Epoch')
    plt.xlabel('Epoch')
    plt.ylabel('AUC Score')
    plt.ylim([0, 1])  # AUC scores range from 0 to 1
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()