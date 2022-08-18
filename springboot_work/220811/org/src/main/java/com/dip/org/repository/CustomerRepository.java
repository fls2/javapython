package com.dip.org.repository;

import com.dip.org.entity.Customer;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CustomerRepository extends JpaRepository<Customer,Long> {
        List<Customer> findByLastName(String lastName);
        Customer findById(long id);

}
