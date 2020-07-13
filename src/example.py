from imtool import ImageTool

tool = ImageTool()
panos = ['fS6TugPzyIuvnTrptOK0mg', 'Q9qGjZth2vH5XOHrmv6Zpg']
ids = [1,2]
size = (946, 473)
nthreads = 8
h_tiles = 26
v_tiles = 13
out_path = '../im/'

ImageTool.dwl_multiple(panos, ids, nthreads, size, v_tiles, h_tiles, out_path)
