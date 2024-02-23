from __future__ import annotations
from dataclasses import dataclass
import heapq

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    # if you are a parent you have children
    parents_id = set()
    for file in files:
        parents_id.add(file.parent)
    
    return [f.name for f in files if f.id not in parents_id]


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:

    hmap = {}
    for file in files:
        for category in file.categories:
            if category not in hmap:
                hmap[category] = 1
            else:
                hmap[category] += 1
    pq = []
    
    for h in hmap:
        heapq.heappush(pq, (hmap[h], h))
    
    k_list = [heapq.heappop(pq) for i in range(len(pq))]
    k_list = k_list[::-1]
    print(k_list)

    return sorted([name for _, name in k_list]) if len(k_list) < k else sorted([name for _, name in k_list[:k]])


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    return 0


if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]
    print(kLargestCategories(testFiles, 3))
    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
