class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """

        d = {
            "(al)":"al",
            "()":"o",
            "G":"G"
        }

        tmp = ""
        res = ""

        for i in range(len(command)):
            tmp += command[i]
            if(tmp in d):
                res += d[tmp]
                tmp = ""

        return res