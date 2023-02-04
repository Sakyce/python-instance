from instance import Instance

def represent(instance:Instance):
    layer = 1

    def recurse(inst:Instance):
        nonlocal layer

        for children in inst.GetChildren():
            print(f'{"-"*layer}> {children}')
            if len(children.GetChildren()) > 0: 
                layer += 1
                recurse(children)
                layer -= 1

    recurse(instance)