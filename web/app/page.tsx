'use client';

import { useEffect, useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

export default function Home() {
  const [status, setStatus] = useState('loading...');

  useEffect(() => {
    fetch('http://localhost:5000/health')
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus('API DOWN'));
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center">
      <Card className="w-[350px]">
        <CardContent className="p-6 space-y-4 text-center">
          <h1 className="text-xl font-bold">DevOps Playground</h1>
          <p>Backend status: <b>{status}</b></p>
          <Button onClick={() => location.reload()}>Recheck</Button>
        </CardContent>
      </Card>
    </div>
  );
}
