# from PIL import Image
# from transformers import BlipProcessor, BlipForConditionalGeneration

# class BlipModel:
#     def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
#         """
#         Инициализация модели BLIP.
#         :param model_name: Название модели в Hugging Face Hub.
#         """
#         self.processor = BlipProcessor.from_pretrained(model_name)
#         self.model = BlipForConditionalGeneration.from_pretrained(model_name)

#     def describe(self, image: Image.Image) -> str:
#         """
#         Генерирует описание для изображения.
#         :param image: Изображение (объект PIL Image).
#         :return: Сгенерированное описание.
#         """
#         inputs = self.processor(image, return_tensors="pt")
#         outputs = self.model.generate(**inputs)
#         return self.processor.decode(outputs[0], skip_special_tokens=True)


# def process_image(file_path: str):
#     """
#     Обрабатывает изображение, генерируя его описание.
#     :param file_path: Путь к изображению.
#     :return: Словарь с описанием изображения.
#     """
#     image = Image.open(file_path)
#     blip_model = BlipModel()  # Инициализация модели
#     description = blip_model.describe(image)
#     return description