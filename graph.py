import rolls
import plotly.express as px
import pandas

def plot_success(pool1, pool2, opposition):
    
    pool1_chances = pool1.chances_of_result(opposition)
    pool2_chances = pool2.chances_of_result(opposition)
    end_pool1 = False
    end_pool2 = False
    index = 0
    result = []
    while (not end_pool1 and not end_pool2):
        curr = [0, 0]
        if (index < len(pool1_chances)):
            curr[0] = pool1_chances[index]
        else:
            end_pool1 = True
            
        if (index < len(pool2_chances)):
            curr[1] = pool2_chances[index]
        else:
            end_pool2 = True
        result.append(curr)
        index = index + 1
    result.pop()
    df = pandas.DataFrame(result, index=["Failure", "Partial Success", "Success", "Greater Success"])
    fig = px.bar(df, barmode="group")
    fig.update_layout(
        xaxis_title="Success Type",
        yaxis_title="% Chance"
    )
    fig.show()