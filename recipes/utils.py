from .models import Recipes
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_recipe_difficulty(recipe_id):
    try:
        recipe = Recipes.objects.get(id=recipe_id)
        return recipe.difficulty
    except Recipes.DoesNotExist:
        return None

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 5))
    
    if chart_type == '#1':  # Bar chart
        plt.bar(data['name'], data['cooking_time'])
        plt.xlabel('Recipe Name')
        plt.ylabel('Cooking Time (minutes)')
        plt.title('Recipe Cooking Times')
        plt.xticks(rotation=45, ha='right')
        
    elif chart_type == '#2':  # Pie chart
        labels = kwargs.get('labels')
        cooking_times = data['cooking_time']
        plt.pie(cooking_times, labels=labels, autopct='%1.1f%%')
        plt.title('Recipe Cooking Time Distribution')
        
    elif chart_type == '#3':  # Line chart
        plt.plot(range(len(data)), data['cooking_time'], marker='o')
        plt.xlabel('Recipe Index')
        plt.ylabel('Cooking Time (minutes)')
        plt.title('Recipe Cooking Times Trend')
        plt.grid(True)
    
    plt.tight_layout()
    chart = get_graph()
    return chart