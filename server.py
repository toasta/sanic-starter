from sanic import Sanic

app = Sanic("ThisIsYourPackageName")


@app.get("/")
@app.ext.template("index.html")
async def this_is_your_handler_name_for_slash(r):
    return dict(
        first_key = "first_key_value",
        second_key = "second_key_value",
        third_key = [1,2,4],
    )

