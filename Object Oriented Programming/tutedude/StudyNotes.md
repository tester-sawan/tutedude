> Class: A class is the blueprint or template that defines
- Attributes(data)
- Methods/Functions (behaviours)
> A class doesnot occupies memory until object is created.
> Syntax for creating class: | class <class_name>: |

> Two types of variables are: Class Variable & Instance Variable.
> Object: It is a real instance of a class
- Created using class name.
- Occupies memory & has its own copy of instance variable.
> How object is created?
- <object_name> = Class_Name()
- when object created python perform: "__new__" creates the object, __init__ prepares it.
> How to call class Variable & Instance variable.
- Access Instance Variable in the same class: self.variable_name
- Access Class Variable in the same class: className.Variable_name
- Access Instance variable from the different class: ObjectName.Variable_name
- Access Class variable from different class: Class_name.variable_name.

> When we call an instance method using object/instance of a class, python passes the object itself as the first argument to that method.
> So, the first argument as standard is given as 'self'.

> Class Method & Static Method
> 