import os
import pandas as pd
import tqdm
from typing import List

def read_parquet_dataset_from_local(path_to_dataset: str, start_from: int = 0, num_parts_to_read: int = 2, 
                                    columns: List[str] = None, verbose: bool = False) -> pd.DataFrame:
    """
    Читает `num_parts_to_read` партиций и преобразует их к pandas.DataFrame.

    Параметры:
    -----------
    path_to_dataset: str
        Путь до директории с партициями.
    start_from: int, default=0
        Номер партиции, с которой начать чтение.
    num_parts_to_read: int, default=2
        Число партиций, которые требуется прочитать.
    columns: List[str], default=None
        Список колонок, которые нужно прочитать из каждой партиции. Если None, то считываются все колонки.
    verbose: bool, default=False
        Флаг для вывода отладочной информации.

    Возвращаемое значение:
    ----------------------
    frame: pandas.DataFrame
        Прочитанные партиции, преобразованные к pandas.DataFrame.
    """

    res = []  # Список для хранения прочитанных DataFrame'ов
    start_from = max(0, start_from)  # Убедимся, что `start_from` не отрицательный
    
    # Словарь для хранения путей к файлам партиций с ключами - номерами партиций
    dataset_paths = {}
    for filename in os.listdir(path_to_dataset):
        file_path = os.path.join(path_to_dataset, filename)
        if os.path.isfile(file_path):  # Проверка, что это файл, а не директория
            try:
                # Попытка извлечь номер партиции из имени файла
                key = int(os.path.splitext(filename)[0].split("_")[-1])
                dataset_paths[key] = file_path
            except ValueError:
                # Если не удалось преобразовать к числу, пропускаем файл
                if verbose:
                    print(f"Пропускаем нечисловое имя файла: {filename}")
    
    # Отбор и сортировка партиций для чтения
    chunks = [dataset_paths[num] for num in sorted(dataset_paths.keys()) if num >= start_from][:num_parts_to_read]
    
    if verbose:
        # Вывод путей к читаемым файлам, если verbose=True
        print("Чтение партиций:", *chunks, sep="\n")
    
    # Чтение партиций в DataFrame
    for chunk_path in tqdm.tqdm_notebook(chunks, desc="Чтение набора данных с pandas"):
        chunk = pd.read_parquet(chunk_path, columns=columns)
        res.append(chunk)
    
    # Объединение всех прочитанных DataFrame'ов в один и сброс индексов
    return pd.concat(res).reset_index(drop=True)


def prepare_transactions_dataset(path_to_dataset: str, num_parts_to_preprocess_at_once: int=1, num_parts_total: int=50,
                                 save_to_path=None, verbose: bool=False):
    preprocessed_frames = []
    for step in tqdm.tqdm_notebook(range(0, num_parts_total, num_parts_to_preprocess_at_once), 
                                   desc='Transforming transactions data'):
        transactions_frame = read_parquet_dataset_from_local(path_to_dataset, step, num_parts_to_preprocess_at_once, verbose=verbose)

        if save_to_path:
            block_as_str = str(step)
            if len(block_as_str) == 1:
                block_as_str = '00' + block_as_str
            else:
                block_as_str = '0' + block_as_str
            transactions_frame.to_parquet(os.path.join(save_to_path, f'processed_chunk_{block_as_str}.parquet'))

        preprocessed_frames.append(transactions_frame)
    return pd.concat(preprocessed_frames)