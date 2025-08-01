
import subprocess

sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
execution_time = 30

with open("results.csv", "w") as f:

    print("Running experiments ...\n", flush=True)
    for size in sizes:
        f.write(f"T={size}" + ",")
    f.write("\n")

    for i in range(execution_time):
        print(f"Running batch {i + 1} sizes ", flush=True)
        for size in sizes:
            try:
                print(f"{size} ", flush=True)
                completed = subprocess.run(
                        ["make", "run", f"TAMANHO={size}"],
                        capture_output=True,
                        text=True,
                        check=True
                        )
                output = completed.stdout.strip()
                parts = output.split(',')
                if len(parts) >= 2:
                    f.write(f"{parts[1]},")
            except subprocess.CalledProcessError as e:
                print("Failed")
                print(e.stderr)
        f.write("\n")

print("Finished running all experiments. \n", flush=True)

