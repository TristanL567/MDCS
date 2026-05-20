relevant-when: Open this drawer when writing PL/SQL blocks, cursors, or bulk operations.

# PL/SQL Basics Reference

## 1. Cursor Management
Cursors are used to fetch multi-row query results.

```sql
DECLARE
    CURSOR emp_cur IS
        SELECT employee_id, last_name FROM employees WHERE department_id = 10;
    r_emp emp_cur%ROWTYPE;
BEGIN
    OPEN emp_cur;
    LOOP
        FETCH emp_cur INTO r_emp;
        EXIT WHEN emp_cur%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(r_emp.last_name);
    END LOOP;
    CLOSE emp_cur;
END;
/
```

---

## 2. Exception Handling
Exceptions are raised to handle run-time errors inside blocks.

```sql
BEGIN
    -- Block logic
    SELECT salary INTO v_salary FROM employees WHERE employee_id = v_emp_id;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No employee found.');
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Multiple records matched unique query.');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error code: ' || SQLCODE || ' - ' || SQLERRM);
        RAISE;
END;
/
```

---

## 3. Bulk Operations
Bulk binds reduce context switching overhead between PL/SQL and SQL engines.

```sql
DECLARE
    TYPE t_emp_ids IS TABLE OF employees.employee_id%TYPE;
    TYPE t_emp_names IS TABLE OF employees.last_name%TYPE;
    v_ids t_emp_ids;
    v_names t_emp_names;
BEGIN
    -- BULK COLLECT INTO (queries bulk fetch)
    SELECT employee_id, last_name 
    BULK COLLECT INTO v_ids, v_names
    FROM employees 
    WHERE department_id = 20;

    -- FORALL (bulk DML execution)
    FORALL i IN 1..v_ids.COUNT
        UPDATE employees 
        SET salary = salary * 1.05 
        WHERE employee_id = v_ids(i);
END;
/
```

---

## 4. Autonomous Transactions
Runs an independent transaction inside the main transaction. Useful for logging errors without rolling back main changes.

```sql
PROCEDURE log_error (p_msg IN VARCHAR2) IS
    PRAGMA AUTONOMOUS_TRANSACTION;
BEGIN
    INSERT INTO error_logs (log_msg, log_time) VALUES (p_msg, SYSDATE);
    COMMIT; -- Commit only commits autonomous insert, doesn't commit outer transaction
END;
/
```
