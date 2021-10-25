import matplotlib.pyplot as plt 
girls_scores=[81,90,70,89,100,80,90,100,80,34]
boys_scores=[30,29,49,48,100,48,34,45,20,30]
grades_range=[10,20,30,40,50,60,70,80,90,100]
fig=plt.figure() 
ax=fig.add_axes([0.1,0.1,0.8,0.8]) # left,bottom,width,height
ax.scatter(grades_range,girls_scores,color='r')
ax.scatter(grades_range,boys_scores,color='b')
ax.set_xlabel('Grades range') 
ax.set_ylabel('Grades scored') 
ax.set_title('scatter plot') 
ax.legend(["girls scores", "boys scores"]) 
plt.show()
