class Dictionary:
    """Najprostsza możliwa implementacja własnego słownika."""

    def __init__(self, initial_capacity: int = 8) -> None:
        self.capacity = initial_capacity
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def _bucket_index(self, key: int) -> int:
        return hash(key) % self.capacity

    def __setitem__(self, key: any, value: any) -> None:
        index = self._bucket_index(key)
        bucket = self.table[index]

        # sprawdź czy klucz już istnieje
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # wstaw nowy element
        bucket.append((key, value))
        self.size += 1

        # sprawdz czy trzeba powiększyć tablicę
        if self.size / self.capacity > 0.75:
            self._resize()

    def __getitem__(self, key: any) -> None:
        index = self._bucket_index(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def __len__(self) -> int:
        return self.size

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0  # zostanie naliczona ponownie podczas reinsertów

        for bucket in old_table:
            for key, value in bucket:
                self[key] = value
