from csv import reader
from xml.dom.minidom import Document

class csv2xml(object):
  """Convert CSV to XML"""
  def __init__(self, infile, header_row=None):
    super(csv2xml, self).__init__()
    self.header_row = header_row
    self.infile     = infile
    self.doc = Document()
    
  def get_max_items(self):
    """Get maximum items in any given row.  
       This sets the column headers/keys if
       none are given."""
    item_counts = []
    for line in reader(open(self.infile)):
      item_counts.append(len(line))
    return max(item_counts) + 1

  def generate(self, print_results=False):
    """Generate XML from CSV"""
    row_counter = 0
    headers = []
    
    items = self.doc.createElement('items')
    self.doc.appendChild(items)
    for line in reader(open(self.infile)):
      row_counter += 1
      if self.header_row is not None:
        if row_counter == self.header_row:
          headers = line
          continue
        elif row_counter < self.header_row:
          continue
      elif self.header_row is None and len(headers)==0:
        # No headers, assign some
        if row_counter == 1:
          for i in range(1,self.get_max_items()):
            headers.append("column%d" % i)
      else:
        pass

      row = self.doc.createElement("row")      
      row.setAttribute("number",str(row_counter - 1))
      items.appendChild(row)
      if len(line) == 0:
        continue
      counter = 0
      for key in headers:
          child_item = self.doc.createElement(key)
          row.appendChild(child_item)
          value = self.doc.createTextNode(line[counter])
          child_item.appendChild(value)
          counter+=1
    final_xml = self.doc.toxml()
    if print_results:
      print final_xml
    return final_xml
