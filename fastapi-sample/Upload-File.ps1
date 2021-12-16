#doesnt work
$url = "http://localhost:8000/files"
$filepath = "C:\Users\fastewaie\Source\fastapi-sample\test.txt"
#$checksumMD5 = (Get-FileHash -Path $filepath -Algorithm MD5).Hash
#$checksumSHA1 = (Get-FileHash -Path $filepath -Algorithm SHA1).Hash
#$checksumSHA256 = (Get-FileHash -Path $filepath -Algorithm SHA256).Hash
$parameters = @{
    Method = "POST"
    Uri = $url
    Headers = @{
        Accept = "application/json"
    }  
    InFile = $filepath
    ContentType = "multipart/form-data"
}
$result = Invoke-WebRequest @parameters
$result.StatusCode

# works
#curl.exe -X 'POST' 'http://localhost:8000/files/' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@C:\Users\fastewaie\Source\fastapi-sample\test.txt;type=text/plain'

# works 
$filepath = "C:\Users\sandro.bormolini\Source\fastapi-sample\test.txt"

$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Content-Type", "multipart/form-data")
$headers.Add("Accept", "application/json")
$headers.Add("Authorization", "Basic aGFuczpwYXNzd29yZA==")

$multipartContent = [System.Net.Http.MultipartFormDataContent]::new()
$multipartFile = $filepath
$FileStream = [System.IO.FileStream]::new($multipartFile, [System.IO.FileMode]::Open)
$fileHeader = [System.Net.Http.Headers.ContentDispositionHeaderValue]::new("form-data")
$fileHeader.Name = "file"
$fileHeader.FileName = $filepath
$fileContent = [System.Net.Http.StreamContent]::new($FileStream)
$fileContent.Headers.ContentDisposition = $fileHeader
$multipartContent.Add($fileContent)

$stringHeader = [System.Net.Http.Headers.ContentDispositionHeaderValue]::new("form-data")
$stringHeader.Name = "type"
$stringContent = [System.Net.Http.StringContent]::new("text/plain")
$stringContent.Headers.ContentDisposition = $stringHeader
$multipartContent.Add($stringContent)

$body = $multipartContent

$response = Invoke-RestMethod 'http://localhost:8000/files' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json

<#
# csharp / restsharp
var client = new RestClient("http://localhost:8000/files");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "application/json");
request.AddHeader("Content-Type", "multipart/form-data");
request.AddFile("file", "/C:/Users/sandro.bormolini/Source/fastapi-sample/test.txt");
request.AddParameter("type", "text/plain");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
#>