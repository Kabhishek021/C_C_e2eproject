import os, sys

class CustomException(Exception):
    def __init__(self, error_message:Exception, error_details: sys):
        self.error_message = CustomException.get_detailed_error_message(
                                            error_message = error_message,
                                            error_details = error_details
                                            
                                            )
        
#try ->
#exception ->
# a,b,c = 1,2,3
# _, _, c
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_details: sys)->str:
        _, _, exce_tb = error_details.exc_info()

        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error occured in execution of :
        [{file_name}] at
        try block line number : [{try_block_line_number}]
        and exception block line number : [{exception_block_line_number}]
        error message : [{error_message}]
        """
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()
    


# @staticmethod: This decorator indicates that the method does not depend on the class instance (i.e., it doesn't use self).
# error_details.exc_info(): This function returns a tuple containing the exception type, exception value, and a traceback object.
# exce_tb.tb_frame.f_lineno: This retrieves the line number where the exception occurred within the block of code.
# exce_tb.tb_lineno: This gets the line number in the try block where the exception was raised.
# exce_tb.tb_frame.f_code.co_filename: This gets the filename where the exception occurred.

# __str__: This method is called when you use print() on the exception object. It returns the error message.
# __repr__: This method is called when you inspect the exception object. It returns the class name as a string.