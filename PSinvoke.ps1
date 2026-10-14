$body = @{
    title = "Need SAP access for a new employee"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "https://prod-30.swedencentral.logic.azure.com:443/workflows/eb9aff43b0954bd7a81083f5b6ed78b3/triggers/When_an_HTTP_request_is_received/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2FWhen_an_HTTP_request_is_received%2Frun&sv=1.0&sig=AaiM4iH4wGAOufPpSlLg93lCx8HtpqiBxvnKQD-OL3o" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"