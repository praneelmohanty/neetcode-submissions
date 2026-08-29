class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local, domain = email.split('@')
            local = ''.join(local.split('+')[0].split('.'))
            email = local + '@' + domain
            email_set.add(email)
        return len(email_set)