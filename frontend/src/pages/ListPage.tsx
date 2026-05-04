import React, { useEffect, useState } from "react";
import axios from "axios";

interface Risk {
  id: number;
  name: string;
  status: string;
}

const ListPage: React.FC = () => {
  const [data, setData] = useState<Risk[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get("http://localhost:8080/api/risks")
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;
  if (data.length === 0) return <p>No records found.</p>;

  return (
    <table className="min-w-full border-collapse border border-gray-300">
      <thead>
        <tr>
          <th className="border px-4 py-2">ID</th>
          <th className="border px-4 py-2">Risk Name</th>
          <th className="border px-4 py-2">Status</th>
        </tr>
      </thead>
      <tbody>
        {data.map(risk => (
          <tr key={risk.id}>
            <td className="border px-4 py-2">{risk.id}</td>
            <td className="border px-4 py-2">{risk.name}</td>
            <td className="border px-4 py-2">{risk.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default ListPage;
