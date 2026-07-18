class ArtGallery:
    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location
        self.artworks = []

    def add_artwork(self, artworks):
        self.artworks.append(artworks)
    
    def remove_artwork(self, artworks):
        self.artworks.remove(artworks)

    def display_artwork(self):
        print(self.artworks)
    
    def __del__(self):
        print("Closing the gallery manager")

artGallery = ArtGallery("Creative Canvas Gallery", "Bengaluru")

while True:
    choice = int(input("Enter a choice "))
    if choice == 1:
        print(artGallery.add_artwork(input("Enter Artwork Name: ")))
    elif choice == 2:
        print(artGallery.remove_artwork(input("Remove Artwork Name: ")))
    elif choice == 3:
        print(artGallery.display_artwork())
    else:
        print("Please enter the correct choice")
        break
    
del artGallery
