# save text to a file
# there needs to be an svg open tag at start and close tag at end
# each object is between open and close svg tag
#
#

def create_svg(width = 800, height = 600):
    svg = {"width": width, "height": height, "items": []}
    return svg

def save_svg(svg, filepath):
    try:
        file = open(filepath, mode="w")
        file.write("<svg width='{0}' height='{1}'>".format(svg["width"], svg["height"]))
        for item in svg["items"]:
            file.write(item)
        file.write("</svg>")
        file.close()
    except:
        raise

def save_html(svg, filepath):
    try:
        file = open(filepath, mode="w")
        file.write("(!DOCTYPE HTML> \n <html>\n<head>\n<title>MY Image</title>\n</head>\n<body>\n")
        file.write("<svg width='{0}' height='{1}'>".format(svg["width"], svg["height"]))
        for item in svg["items"]:
            file.write(item)
        file.write("</svg>")
        file.write("</html>")
        file.close()
    except:
        raise

# try to write a function for adding circles to the svg image

def make_circle(cx, cy, r, stroke, stroke_width, fill, opacity=1.0):
    return("<circle cx='{}' cy='{}' r='{}' stroke='{}' stroke-width='{}' fill='{}' opacity='{6}'/>\n".format(cx, cy, r, stroke, stroke_width, fill, opacity))
    

def main():
    try:
        filepath = "mypic1.html"
        svg = create_svg(width=600, height=400)
        svg["items"].append("<circle cx='50' cy='50' r='40' stroke='green' stroke_width='4' fill='yellow' />")
        circle = make_circle(75, 125, 110, "yellow", 6, "orange")
        svg["items"].append(circle)
        save_svg(svg, filepath)
    except Exception as error:
        print("An error occurred:", error)

main()
