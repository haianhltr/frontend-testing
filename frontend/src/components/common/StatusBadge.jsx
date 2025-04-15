import React from 'react';

const colors = {
  'Not Started': 'gray',
  'Running': 'blue',
  'Success': 'green',
  'Failed': 'red',
};

export default function StatusBadge({ status }) {
  return (
    <span
      style={{
        backgroundColor: colors[status] || 'black',
        color: 'white',
        padding: '4px 8px',
        borderRadius: '8px',
        fontSize: '0.85em',
        marginRight: '5px',
      }}
    >
      {status}
    </span>
  );
}
