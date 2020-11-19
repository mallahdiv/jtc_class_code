class Booklist():
	def __init__(self):
		self.books = []
		

	def add(self, title, author):
		new_book = {'title': title, 'author': author}
		self.books.append(new_book)

		
		

	def count_books(self):
		return len(self.books)

	def remove_title(self, title):
		for book in self.books:
			if title == book['title']:
				self.books.remove(book)

	def display_titles(self):
		pass

