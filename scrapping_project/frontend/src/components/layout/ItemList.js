import React, { useState, useEffect } from 'react';
import styled from 'styled-components'

import EnhancedTable from '../Table/EnhancedTable';
import { getData } from '../Api';

const Styles = styled.div`
  padding: 2rem;

  table {
    border-spacing: 0;
    border: 1px solid black;

    tr {
      :last-child {
        td {
          border-bottom: 0;
        }
      }
    }

    th,
    td {
      margin: 0;
      padding: 0.5rem;
      border-bottom: 1px solid black;
      border-right: 1px solid black;

      :last-child {
        border-right: 0;
      }
    }
  }
`;

const ItemList = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    getData('/api/products').then(data => setItems(data));
  }, [])

  const getNextData = () => {
    if (items.next) {
      getData(items.next).then(data => setItems(data));
    }
  };

  const getPreviousData = () => {
    if (items.previous) {
      getData(items.previous).then(data => setItems(data));
    }
  };

  return (
    <Styles>
      <h1 className="text-center">Products</h1>
      <EnhancedTable
        data={items}
        getNextData={getNextData}
        getPreviousData={getPreviousData} />
    </Styles>
  );
}

export default ItemList;
