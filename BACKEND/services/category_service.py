from repositories.category_repository import CategoryRepository
from repositories.file_repository import FileRepository


class CategoryService:
    def __init__(self):
        self.category_repo = CategoryRepository()
        self.file_repo = FileRepository()