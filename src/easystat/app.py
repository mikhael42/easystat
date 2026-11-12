"""Test the easystat package."""

from easystat.measurements import result_with_uncertainty


def main():
    measurements = [1, 2, 2, 2, 3]
    result, uncertainty = result_with_uncertainty(measurements)
    print(f"{measurements=}")
    print(f"Result of measurements is: {result:.2f} +- {uncertainty:.2f}.")

if __name__ == "__main__":
    main()