az group create --name myResourceGroup --location eastus
az configure --defaults group=myResourceGroup location=eastus
az appservice plan create --name myPlan --sku F1
az webapp create --name flask_app --plan myPlan --runtime "node|6.9"