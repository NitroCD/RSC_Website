using Python.Runtime;

Runtime.PythonDLL = @"C:\Users\cdhan\AppData\Local\Programs\Python\Python311\python311.dll";
PythonEngine.Initialize();
PythonEngine.BeginAllowThreads();

using (Py.GIL())
{
    dynamic sys = Py.Import("sys");
    sys.path.append(@"C:\Users\cdhan\Projects\RSC_Website");
}

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

// comment out when testing on locally
// app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
