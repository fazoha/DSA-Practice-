class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0] * n
        callstack = []
        previousStart = 0

        # Step 2: iterate through logs
        for log in logs:
            functionID, event, timestamp = log.split(":")
            functionID = int(functionID)
            timestamp = int(timestamp)

            # if a function is starting
            if event == "start":
                # If another function was already running, give it time until now
                if callstack:
                    output[callstack[-1]] += timestamp - previousStart
                # Push current function on stack and mark its start
                callstack.append(functionID)
                previousStart = timestamp
            else:
                # Current function ends, add its inclusive time
                output[callstack.pop()] += timestamp - previousStart + 1
                # Next function (if any) starts at timestamp + 1
                previousStart = timestamp + 1

        return output


        








        