class SQL:
    SELECT_ACCOUNT_BY_ID_USER = '''
SELECT 
    account.*,
    tag.title
FROM account 
LEFT OUTER JOIN tag ON tag.id_tag = account.id_tag
WHERE account.id_user = %(id_user)s
    '''
