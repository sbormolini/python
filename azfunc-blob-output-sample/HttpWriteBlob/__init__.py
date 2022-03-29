import logging
import azure.functions as func

from datetime import date

def main(req: func.HttpRequest, outputblob: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        today = date.today()
        data = f'Date,Value\n{today},{name}' 
        logging.info(f'write blob with data: {data}')
        outputblob.set(data)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
