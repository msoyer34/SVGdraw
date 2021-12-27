import cv2 as cv
img = cv.imread("image.jpeg") #give the image path

heigth, width = img.shape[:2] #take the shape of the image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert the image to the gray


edges = cv.Canny(gray,100,200) #detect the edges

cnt, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) #find the contours to draw

cv.imshow('edges', edges)
cv.drawContours(img, cnt, -1,(0,0,0), 1)#draw contours
cv.imshow('cnt',img)

#save svg data for the image
with open("path.svg", "w+") as f:
    f.write(f'<svg width="{width}" height="{heigth}" xmlns="http://www.w3.org/2000/svg">')

    for c in cnt:
        f.write('<path d="M')
        for i in range(len(c)):
            x, y = c[i][0]
            f.write(f"{x} {y} ")
        f.write('" style="stroke:pink"/>')
    f.write("</svg>")



cv.waitKey(0)
cv.destroyAllWindows()




