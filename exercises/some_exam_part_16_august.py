@staticmethod
def release_software_component(hardware_name: str, software_name: str):
    current_hardware = [h for h in System._hardware if h.name == hardware_name]
    current_software = [s for s in System._software if s.name == software_name]

    if not current_hardware or not current_software:
        return "Some of the components do not exist"

    current_hardware[0].uninstall(current_software[0])
    System._software.remove(current_software[0])


@staticmethod
def analyze():
    total_memory = sum(h.memory for h in System._hardware)
    total_capacity = sum(h.capacity for h in System._hardware)
    used_memory = sum(s.memory_consumption for s in System._software)
    used_capacity = sum(s.capacity_consumption for s in System._software)

    return f'System Analysis\n' \
           f'Hardware Components: {len(System._hardware)}\n' \
           f'Software Components: {len(System._software)}\n' \
           f'Total Operational Memory: {used_memory} / {total_memory}\n' \
           f'Total Capacity Taken: {used_capacity} / {total_capacity}'


@staticmethod
def system_split():
    result = ''
    for h in System._hardware:
        name = h.name
        length_express = len([s for s in h.software_components if s.__class__.__name__ == "ExpressSoftware"])
        length_light = len([s for s in h.software_components if s.__class__.__name__ == "LightSoftware"])
        memory_usage = sum([s.memory_consumption for s in h.software_components])
        memory_total = h.memory
        capacity_usage = sum([s.capacity_consumption for s in h.software_components])
        capacity_total = h.capacity
        type_hardware = h.type
        software_components = ', '.join(s.name for s in h.software_components) if h.software_components else None

        result += f'Hardware Component - {name}\n' \
                  f'Express Software Components: {length_express}\n' \
                  f'Light Software Components: {length_light}\n' \
                  f'Memory Usage: {memory_usage} / {memory_total}\n' \
                  f'Capacity Usage: {capacity_usage} / {capacity_total}\n' \
                  f'Type: {type_hardware}\n' \
                  f'Software Components: {software_components}'

    return result