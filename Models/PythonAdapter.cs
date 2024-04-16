using Python.Runtime;

public class PythonAdapter
{
    public string pythonString() {
        string output = "";
        using (Py.GIL())
        {
            dynamic sys = Py.Import("sys");
            sys.path.append(@"C:\dotnet\RSC_Website");
            var pythonScript = Py.Import("mypythonscript");
            var obj = pythonScript.InvokeMethod("test_method");
            output = obj.ToString();
        }
        return output;
    }
}
