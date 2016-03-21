# upload

We're given a raw disk image of a btrfs filesystem, and we need to recover some files.
We ran `btrfs-find-root ./disk.img` to find the roots, and restored the second root with snapshots using `btrfs restore -s -t 30031872 ./disk.img ./outdirectory`.
Taking recursive diffs of each snapshot under `btrfs/subvolumes/`, we found an ELF that printed the flag under `btrfs/subvolumes/978670fd616dfa44a685df56298cd950a44bc914207f92e753dd1c0cd569613b/data/`.
