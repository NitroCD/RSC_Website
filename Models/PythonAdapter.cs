namespace RSC_Website.Models;

using Python.Runtime;

public class PythonAdapter
{
    public string PythonString() 
    {
        string? output = "";
        using (Py.GIL())
        {
            var pythonScript = Py.Import("member");
            var obj = pythonScript.InvokeMethod("test_method");
            if (obj != null) { output = obj.ToString(); }
        }
        return output ?? "";
    }
}
