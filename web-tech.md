## eleven
 ### https://www.youtube.com/watch?v=94UM0Ss3uoU&list=PL0Zuz27SZ-6Oi6xNtL_fwCrwpuqylMsgT&index=11
 were
 ### https://www.youtube.com/watch?v=u_lLNH38n5E&list=PL0Zuz27SZ-6Oi6xNtL_fwCrwpuqylMsgT&index=13
 
 ### https://www.youtube.com/watch?v=WbG86sMd3SU&list=PL0Zuz27SZ-6Oi6xNtL_fwCrwpuqylMsgT&index=21

## nine:HTML Forms, Variables, Numbers & Maths Methods
### links
https://youtu.be/vzLdq3b0w3Y?list=PL0Zuz27SZ-6Oi6xNtL_fwCrwpuqylMsgT

### slides
HTML <form>
 enable user interaction and data collection on websites
 <form action="login.php" method="post">
  <!-- form content goes here --> 
 </form>
form structure
 forms are enclosed within <form> </form> element
 The action attribute defines where the form data is sent.
 The method attribute specifies how the data is sent.
Text input fields
 <input> element with the type text attribute allows single-line text to be entered
 The id attribute is used to identify the field's name when the form is submitted.
 The <label> element associated with the input improves accessibility.
 placeholder attribute can provide hints of examples of expected input.
 <form action="process.php" method="post">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username">
 </form>
Passwords inputs
 password fields are created using the <input> element with the type attribute using the password value.
 <form action="process.php" method="post">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username">
  <label for="password">Password:</label>
  <input type="password" id="password" name="password">
 </form> 
Radio buttons and checkboxes
 radio buttons are created using the <input> element with the type attribute and the radio value. Allowing to select a single option from a group of choices.
 Using the name attribute with the same value groups them together, ensuring only one option is selected.
 <form action="process.php" method="post">
  <input type="radio" 
         id="approve" 
         name="approval" 
         value="yes" />
  <label for="approval">Approve</label>
  <input type="radio" 
         id="deny" 
         name="approval" 
         value="deny" />
 Checkboxes are created using <input> element with type attribute and the checkbox value, allows selection of one or more options from a list.
 checkboxes can be used independently or grouped as needed.
 <label for="deny">Deny</label> 
 <input type="checkbox" 
         id="subscribe" 
         name="subscribe" 
         value="yes" />
  </form>
Textarea and labels
 allows users to provide multiline text.
 label element is used to improve accessability.
 

## eight:Images, Tables and Intro to JavaScript
### links
 https://youtu.be/SajRjc9KKUE?list=PL0Zuz27SZ-6Oi6xNtL_fwCrwpuqylMsgT

 https://css-tricks.com/almanac/properties/o/object-fit/

### slides
HTML <img> tag attributes
 alt: Provides alternative text for screen readers and if the 
image cannot be displayed.
 width and height: Set the dimensions of the image.
 title: Adds a tooltip when the user hovers over the image.

 <img src="image.jpg" alt="Description">
 <img src="image.jpg" alt="Description"
 width="300" height="200">
Relative Paths
 relative paths are defined in relation to the current location of the HTML file. 
 used when the image is within the same directory as the HTML file or in a subdirectory of it.
 <img src="images/image.jpg" alt="Description"
 width="300" height="200">
Absolute Paths
 absolute paths specify the full URL or file system path to the image
 used when the image is hosted on a different server or in a different directory.
 <img src="http://example.com/images/image.jpg" alt="Description">
 <img src="file:///C:/path/to/your/image.jpg" alt="Description">
Accessibility
 the alt attribute in the <img> tag plays a crucial role in accessibility.
 providing alternative text for users who cannot see the images.
Responsive Images
 use max-width in CSS to set the max-width property for the image to a percentage value to make it responsive.
 ensuring the image never exceeds its container's width.
 img {max-width: 100%; height: auto;}
Responsive Images Two
 srcset attribute in the <img> tag allows you to provide multiple image sources with different resolutions.
 browsers can then choose the most appropriate one based on the user's device.
 <img
      src="image-small.jpg"
      alt="Description"
      srcset="
      image-small.jpg 400w,
      image-medium.jpg 800w,
      image-large.jpg 1200w
      "
      sizes="
      (max-width: 600px) 100vw.
      (max-width: 1200px) 50vw, 1000px
      "
  >
Image Formats - Considerations
 balance quality and file size
 match the format to the purpose
  JPEG is suitable for photographs
  PNG for images with transparency
  GIF or simple animations
  SVG for scalable vector graphics
 Optimism your load times
  selecting the appropriate format to optimism loading 
  crucial for user experience and SEO

Lazy loading
 lazy loading delays the loading of images until they are in or near the user's viewport
 this con significantly improve page load times and user experience
Lazy loading attribute
 loading attribute allows you to specify how an image should be loaded
 "lazy" for lazy loading and "eger" for immediate loading
 <img src="image.jpg" alt="Description" loading="lazy">
 <img src="image.jpg" alt="Description" loading="eager">

Challenge 1 – Insert Images
 Using the <img> tag and set the src, alt, and optionally, width and height attributes. 

 Insert an image in the header section (<header>). 
Within the "Latest News" section, replace one of the news articles' placeholder text with an image. 
In the sidebar (<aside>), add an image that adjusts its size based on the screen width (responsive design). Use CSS to style the image to be a maximum of 100% of the container's width. 
Place an image in the footer section (<footer>). 
Eager load all of your images
 
Basic table structure
 <table> element is used to create a table</table>
 <th>(table header) tag for improving clarity</th>
 <tr> (table row) is used to define a row within the table</tr>
 <td>(table date) is used to hold data in the table</td>
  <table>
    <tr>
      <td>row one, cell one</td>
      <td>row one, cell two</td>
    </tr>
    <tr>
      <td>row two, cell one</td>
      <td>row two, cell two</td>
    </tr>
  </table>

Table attributes
 rowspan="value"
 colspan="value"

Styling table with css

Challenge 2 – Insert a Table
 Add a table containing information about upcoming events to the provided HTML code.

 Locate the <aside class="sidebar"> element.
 Inside the <aside>, insert an HTML table structure that    includes the following columns:
  Event Name
  Date
  Location
 Populate the table with three upcoming events, include names, dates, & locations.
 Apply CSS styles to the table using "styles.css”

What is JavaScript
 Officially called ECMAScript
 ECMA-262 standard
 2022:ECMA-262 revision 13
 ECMAScript:
  ECMA-262 specification is a blueprint for creating a scripting language. 
The “Official” name for JavaScript
 JavaScript:
  general-purpose scripting language.
  conforms to the ECMAScript specification. 
  is an implementation of that blueprint. 
  implements the ECMAScript specification.
Where to use it
 front-end
  web browser
  desktop
   electron
   NW.js
 back-end
  server
  server run-times
   NodeJS
   Bun
   Deno
Embedded JS
 similar to inline css
 <script>
  console.loa('javascript');
 </script>
External JS
 There is a source link in the script tags attribute, works similar to external css file.
 <script src="Javascript-file.js"></script>

Chrome dev tools
 Console: Execute JavaScript code and view logs. 
 Sources: Set breakpoints, step through code, and inspect variables.
 Network: Monitor requests and responses when working with APIs
Performance: Analyse JavaScript performance and optimize code.

Video reference
 JavaScript Tutorial For Beginners - Intro + VSCode Setup
https://youtu.be/36Evo9c8gfU


## four
 pptx
 <link rel="stylesheet" href="https://cdnjs/cloudflare.com/ajax/normalize/8.0.1/normalize.min.css">
 https://meyerweb.com/eric/tools/css/reset/reset.css
 font-size: % em rem vw px
 
 Box Model
  content
  padding
  boarder
  margin
  width/height
 
 selectors
  Type
  Class
  ID
  Descendant
  Child
  Adjacent
  General Sibling
  Attribute
  Pseudo-Class
  Pseudo-Element
  TRBL top right bottom left

 Flexbox
  one-dimensional layout model that distributes space and alignment items within a container.
  parent-child - parent container (flex) and child elements (flex)
  main and cross axes:
  main flex: flex-direction: justify-content:
  cross align-items: align-self: align-content:
 media queries to make layout responsive.

 https://css-tricks.com/snippets/css/a-guide-to-flexbox/

 https://css-tricks.com/snippets/css/complete-guide-grid/
 
 ### Properties for the Parent
 display - defines the element as a grid container and establishes a new grid formatting context for its contents.
 gird - generates a block-level grid.
 inline-grid - generates an inline-level grid.

 .container {
  display: grid | inline-grid;
 }

 grid-template-columns
 grid-template-rows

 Defines the columns and rows of the grid with a space-separated list of values. The values represent the track size, and the space between then represents the grid line.

 Values
 track size can be a length, a percentage, or a fraction eg 100px, , 1fr.
 inline name an arbitrary name of your choosing, skewer case

 left to right assigned positive number, right to left negative number.
 To explicitly name lines use brackets []
  grid-template-columns: [first] 40px [line2] 50px [line3] auto [col4-start] 50px [five] 40px [end];
  grid-template-rows: [row1-start] 25% [row1-end] 100px [third-line] auto [last-line];
  a line can have more than one name .container {
  grid-template-rows: [row1-start] 25% [row1-end row2-start] 25% [row2-end];}

repeat() notation.
 .container {grid-template-columns: repeat(3, 20px [col0start]);}
 repeats 20px than line named col-start three times.
Multiple same name can be referenced by the their name and count
 .item{grid-column-start: col-start 2;}
fr unit set the size of a track as a fraction of the free space of the grid container. The free space is calculated after any non-flexible items item. 

week-three
 validation
 do dom chrome 

### q
slide 28 why is validating you html important?

week-two
 in teams there is shared files
  general - class materials - c web technologies
  downloaded file structure for 20 sessions
 figmia
 sematic mark up is equivalent to documenting code
 inline style, inpage styling at the top of a page and styling with a separate file.

links in session two shell
https://developer.chrome.com/docs/devtools/dom/
https://www.youtube.com/playlist?list=PL0Zuz27SZ-6OlAwitnFUubtE93DO-l0vu
https://www.youtube.com/watch?v=ZT4WRRhacWk
a - anchor tag
article - self-contained composition or part of a HTML document. 
aside - a portion of a document whose content is only indirectly related to the document's main content.
b - boldface two other ways to show importance font-weight CSS property and strong element
dd - description details, description or definition or value in a description list.
dl - description list, encloses a list of groups of terms using the dt tag with descriptions using the dd tag.
dt - specifies a term in a description.
em - emphasis tag, can be nested with each level of nesting indicating a greater degree of emphasis.
footer - represents the footer for its nearest ancestor sectioning content or sectioning root. Footer typically contains information about tbe author of the section, copyright data or links to related documents.
h - h1 to h6 are heading tags.
meta - meta tag represents metadata that cannot be represented by other meta-related tags like base, link, script, style or title.
title - The title tag defines the document's title that is shown in a browser's title bar or pages's tab. It only contains text; tags within the element are ignored.
header - represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.
a - anchor tag
dl - represents a description list. The element encloses a list of groups of terms (specified using the <dt> dt element) and descriptions (provided by <dd> dd element).
dt - Description term, specifies a term in a description or definition list.
dd - The description details element, provides the description, definition, or value for the preceding term. 
i - idiomatic, italicized text.
ol - ordered list. Contains list items li.
ul - unordered list. Contains list items li.
li - list item. It must be contained in a parent tag: an ordered list ol or unordered list ul.
main - tag represents the dominant content of the body of a document.
p - Paragraph tag.
section - a generic standalone section of a document.
strong - indicates that its contents have strong importance.
thead - Table head tag defines a set of rows defining the head of the columns of the table.
tbody - encapsulates a set of table rows tr tags indicating that they comprise the body of the table.
tfoot - Table foot defines a set of rows summarising the columns of the table.
table - Represents tabular data - that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.
tr - Table row defines a row of cells in a table. The row's cells can then be established using a mix of table data td and table header th.
td - Table data defines a cell of a table that contains data. It participates in the table model.
th - Table header defines a cell as the header of a group of table cells. The exact nature of this group is defined by the scope and header attributes.
img - Image embedding tag
br - Break line produces a carriage-return. Useful for writing where the division of lines is significant.
hr - Horizontal rule gives a thematic break between paragraphs.
area - Defines an area inside an image map that has predefined clickable areas.
embed - Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as browser plug-in.
input - Is used to create interactive controls for web-based forms in order to accept data from the user.
source - Specifies multiple media resources for the picture, audio or video tags.
div - Is the generic container for flow content.

week-one
 PAN LAN WAN
 Internet
 DNS lookup
 HTML
 HTTP hyper text transfer protocol
 TCP/IP transfer control protocol over internet protocol
 Content is king, HTML gives structure, CSS gives format, JavaScript give interactivity.
 What we need Browser, two different engines chrome and firefox, IDE firestorm and web server screencraft.
 Short cut for getting to repo. win+e for file explorer, in address bar %userprofile%
 Web server windows is laragon, top bar means?
  change the root address, menu, www, switch document root, select another, select user/source/repos
 Webstorm 
  set up git and github
  plugin gitignore, rainbow brackets colours brackets, indent rainbow - colours indent, key promoter - shows key board short cuts
  preferences editor change font size with mouse, ligutres - 
 HTML 

## setting up webstorm
 plugin 2:01:35
 setting ctrl + alt + s
  plugins
   .ignore
    jetBrains
   rainbow
    brackets lite
    indent
   key promoter x - doesn't seem to be available for linux version running
   material
    atom material icons
    material theme ui
  
  appearance & behavior
   appearance
    I like high contrast - maybe be good for lecturing
    use custom fonts ->Segoe UI size 12
    apply
   accessability
    use contrast scrollbars
   ui options
    show tree indent guides
    
   editor
    general
     change font size with ctrl+mouse wheel
 tools
  terminal
   application settings
    shell path
     to set shell bash is fine for now

2:11:25
 File structure
  mkdir assets assets/css assets/js assets/images
  
     