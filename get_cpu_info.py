import psutil

statistics = {}

# Get Physical CPU Count
physical_cpu_count = psutil.cpu_count(logical=False)
statistics['physical_cpu_count'] = physical_cpu_count

# Get Physical and Logical CPU Count
physical_and_logical_cpu_count = psutil.cpu_count(logical=True)
statistics['physical_and_logical_cpu_count'] = physical_and_logical_cpu_count

# CPU percentage load
cpu_load = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
statistics['cpu_load'] = cpu_load

# CPU utilization as a percentage.
cpu_utilization = psutil.cpu_times_percent()
statistics['cpu_utilization'] = dict({
    'user': cpu_utilization.user, 'system': cpu_utilization.system,
    'idle': cpu_utilization.idle})
