from imtool import ImageTool

# Import tool
tool = ImageTool()

# Specify panorama idenfitiers array
panos = ['fS6TugPzyIuvnTrptOK0mg', 'Q9qGjZth2vH5XOHrmv6Zpg']

# Provide a list of custom identifiers to name the images
ids = [1,2]

# Final size of the image
size = (946, 473)

# Number of threads
nthreads = 8

# Horizontal Google Street View tiles
h_tiles = 26

# Vertical Google Street View tiles
v_tiles = 13

# Output path for the images
out_path = '../im/'

# Chose whether to have final images split vertically in two equal images
# The function compose_folder() can be used to compose the downloaded images in a second time
cropped = True

# Chose whether to have final images in one single file
full = False

# Call function
ImageTool.dwl_multiple(panos, ids, nthreads, size, v_tiles, 
                       h_tiles, out_path, cropped, full)