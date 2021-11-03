class SQL:
    SELECT_USER_BY_ID_USER = '''
SELECT * FROM user WHERE id_user = %(id_user)s
    '''

    SELECT_USER_BY_LOGIN_ID = '''
SELECT * FROM user WHERE login_id = %(login_id)s
    '''

    SELECT_ACCOUNT_BY_ID_USER = '''
SELECT 
    account.*,
    tag.title,
    tag.color_code
FROM account 
LEFT OUTER JOIN tag ON tag.id_tag = account.id_tag
WHERE account.id_user = %(id_user)s
    '''

    SELECT_ACCOUNT_BY_ID_USER_START_END = '''
SELECT 
    account.*,
    tag.title,
    tag.color_code
FROM account 
LEFT OUTER JOIN tag ON tag.id_tag = account.id_tag
WHERE account.id_user = %(id_user)s
AND dt_account BETWEEN %(start)s AND %(end)s
    '''

    SELECT_ACCOUNT_BY_ID_ACCOUNT = '''
SELECT * FROM account WHERE id_account = %(id_account)s
    '''

    INSERT_ACCOUNT = '''
INSERT INTO account (
    id_account,
    id_user,
    id_tag,
    debit,
    credit,
    dt_account,
    dt_create,
    dt_update
) VALUES (
    %(id_account)s,
    %(id_user)s,
    %(id_tag)s,
    %(debit)s,
    %(credit)s,
    %(dt_account)s,
    NOW(),
    NOW()
)
    '''

    UPDATE_ACCOUNT = '''
UPDATE account SET
    id_account = %(id_account)s,
    id_user = %(id_user)s,
    id_tag = %(id_tag)s,
    debit = %(debit)s,
    credit = %(credit)s,
    dt_account = %(dt_account)s,
    dt_create = %(dt_create)s,
    dt_update = NOW()
WHERE id_account = %(id_account)s
    '''

    DELETE_ACCOUNT = '''
DELETE FROM account WHERE id_account = %(id_account)s
    '''

    SELECT_TAG_BY_ID_USER = '''
SELECT * FROM tag WHERE id_user = %(id_user)s
    '''

    INSERT_TAG = '''
INSERT INTO tag (
    id_tag,
    id_user,
    title,
    color_code,
    dt_create,
    dt_update
) VALUES (
    %(id_tag)s,
    %(id_user)s,
    %(title)s,
    %(color_code)s,
    NOW(),
    NOW()
)
    '''

    UPDATE_TAG = '''
UPDATE tag SET
    id_tag = %(id_tag)s,
    id_user = %(id_user)s,
    title = %(title)s,
    color_code = %(color_code)s,
    dt_create = %(dt_create)s,
    dt_update = NOW()
WHERE id_tag = %(id_tag)s
    '''

    DELETE_TAG = '''
DELETE FROM tag WHERE id_tag = %(id_tag)s
    '''
