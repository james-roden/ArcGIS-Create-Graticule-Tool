import arcpy
class ToolValidator(object):
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""

  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    self.params = arcpy.GetParameterInfo()

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""

    # Default is a 1 degree interval
    self.params[0].value = 1
    self.params[1].value = 0
    self.params[2].value = 0    

    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
  
    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""

    # Degrees, minutes, & seconds cannot all be 0
    if self.params[0].value == '0' and self.params[1].value == '0' and self.params[2].value == '0':
        self.params[0].setErrorMessage("Please enter a valid interval of at least 1 second.")

    # Check degrees, minutes, & seconds are within the correct range
    if not 0 <= int(self.params[0].value) <= 90:
        self.params[0].setErrorMessage("Value must be between 0 and 90 degrees")

    if not 0 <= int(self.params[1].value) <= 59:
        self.params[1].setErrorMessage("Value must be between 0 and 59 minutes")

    if not 0 <= int(self.params[2].value) <= 59:
        self.params[2].setErrorMessage("Value must be between 0 and 59 seconds")

    mxd = arcpy.mapping.MapDocument('current')

    # Check map units are decimal degrees
    if not mxd.activeDataFrame.mapUnits == 'DecimalDegrees':
      self.params[3].setErrorMessage("Active data frame map units must be decimal degrees. E.g. WGS84")
    return
