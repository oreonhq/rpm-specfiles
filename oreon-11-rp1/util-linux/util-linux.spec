%global source0_hash e596083744e746be7d2823b62b43f4418dd7bf56303b4dc09e6fe8112fe3d7ed
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: util-linux
Version: 2.41.6
Release: 2%{?dist}
Summary: Low-level system utilities and libraries
License: GPL-2.0-or-later
URL: https://github.com/util-linux/util-linux
Source0: https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/v2.41/util-linux-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: readline-devel
BuildRequires: pam-devel
BuildRequires: sqlite-devel
BuildRequires: libcap-devel
BuildRequires: libselinux-devel
BuildRequires: patchelf
BuildRequires: fakeroot
BuildRequires: systemd-devel
BuildRequires: python3-devel
%endif
Requires: util-linux-core%{?_isa} = %{version}-%{release}

%description
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n util-linux-core
Summary: Low-level system utilities and libraries

%description -n util-linux-core
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n util-linux-i18n
Summary: Low-level system utilities and libraries

%description -n util-linux-i18n
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n util-linux-script
Summary: Low-level system utilities and libraries
Requires: util-linux%{?_isa} = %{version}-%{release}

%description -n util-linux-script
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n uuidd
Summary: Low-level system utilities and libraries
Requires: libuuid%{?_isa} = %{version}-%{release}

%description -n uuidd
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%if %{without bootstrap} && !0%{?bootstrap}
%package -n python3-libmount
Summary: Low-level system utilities and libraries
License: LGPL-2.1-or-later
Requires: libmount%{?_isa} = %{version}-%{release}
Requires: python3

%description -n python3-libmount
util-linux provides libmount, libblkid, libfdisk and libsmartcols.
%endif

%package -n libblkid
Summary: Block device identification library
License: LGPL-2.1-or-later

%description -n libblkid
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libblkid-devel
Summary: Block device identification library
License: LGPL-2.1-or-later
Requires: libblkid%{?_isa} = %{version}-%{release}
Provides: pkgconfig(blkid) = %{version}-%{release}

%description -n libblkid-devel
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libfdisk
Summary: Partition table library
License: LGPL-2.1-or-later

%description -n libfdisk
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libfdisk-devel
Summary: Partition table library
License: LGPL-2.1-or-later
Requires: libfdisk%{?_isa} = %{version}-%{release}
Provides: pkgconfig(fdisk) = %{version}-%{release}

%description -n libfdisk-devel
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libmount
Summary: Mount library
License: LGPL-2.1-or-later
Requires: libblkid%{?_isa} = %{version}-%{release}

%description -n libmount
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libmount-devel
Summary: Mount library
License: LGPL-2.1-or-later
Requires: libmount%{?_isa} = %{version}-%{release}
Provides: pkgconfig(mount) = %{version}-%{release}

%description -n libmount-devel
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libsmartcols
Summary: Column output library
License: LGPL-2.1-or-later

%description -n libsmartcols
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libsmartcols-devel
Summary: Column output library
License: LGPL-2.1-or-later
Requires: libsmartcols%{?_isa} = %{version}-%{release}
Provides: pkgconfig(smartcols) = %{version}-%{release}

%description -n libsmartcols-devel
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libuuid
Summary: UUID library
License: BSD-3-Clause

%description -n libuuid
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n libuuid-devel
Summary: UUID library
License: BSD-3-Clause
Requires: libuuid%{?_isa} = %{version}-%{release}
Provides: pkgconfig(uuid) = %{version}-%{release}

%description -n libuuid-devel
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n liblastlog2
Summary: Lastlog2 library
License: BSD-2-Clause

%description -n liblastlog2
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package -n liblastlog2-devel
Summary: Lastlog2 library
License: BSD-2-Clause
Requires: liblastlog2%{?_isa} = %{version}-%{release}
Provides: pkgconfig(lastlog2) = %{version}-%{release}

%description -n liblastlog2-devel
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%prep
%oreon_sha256
%autosetup -n util-linux-%{version} -p1

%build
%oreon_configure \
  --disable-static \
  --with-ncursesw \
  --enable-libuuid \
  --enable-libblkid \
  --enable-libmount \
  --enable-libfdisk \
  --enable-libsmartcols \
%if %{without bootstrap} && !0%{?bootstrap}
  --with-systemd \
  --with-python=3
%else
  --without-systemd \
  --without-python
%endif
%oreon_make

%install
%{_oreon_flags} fakeroot %{_oreon_helper} make-install %{_oreon_paths} --destdir %{buildroot} --
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
rm -rf %{_builddir}/ul
mkdir -p %{_builddir}/ul
python3 - %{buildroot} %{_builddir}/ul %{?with_bootstrap:boot}%{!?with_bootstrap:full} << 'PY'
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
out = Path(sys.argv[2])
full = sys.argv[3] == "full"
core = {
    "agetty", "blkid", "blockdev", "chrt", "dmesg", "findmnt", "flock", "fsck",
    "hardlink", "ionice", "ipcmk", "ipcrm", "ipcs", "kill", "logger", "losetup",
    "mkswap", "more", "mount", "mountpoint", "nsenter", "partx", "renice",
    "setsid", "sulogin", "swapoff", "swapon", "switch_root", "taskset", "umount",
    "unshare",
}
script_tools = {"script", "scriptlive", "scriptreplay"}
attrs = {
    "mount": "%attr(4755,root,root) ",
    "umount": "%attr(4755,root,root) ",
    "su": "%attr(4755,root,root) ",
    "wall": "%attr(2755,root,tty) ",
    "write": "%attr(2755,root,tty) ",
}
pc = {
    "blkid.pc": "libblkid-devel",
    "fdisk.pc": "libfdisk-devel",
    "mount.pc": "libmount-devel",
    "smartcols.pc": "libsmartcols-devel",
    "uuid.pc": "libuuid-devel",
    "lastlog2.pc": "liblastlog2-devel",
}
include = (
    ("/include/blkid/", "libblkid-devel"),
    ("/include/libfdisk/", "libfdisk-devel"),
    ("/include/libmount/", "libmount-devel"),
    ("/include/libsmartcols/", "libsmartcols-devel"),
    ("/include/uuid/", "libuuid-devel"),
    ("/include/liblastlog2/", "liblastlog2-devel"),
)
soname = re.compile(r"/lib(?:64)?/(lib(?:blkid|fdisk|mount|smartcols|uuid|lastlog2))\.so(\..+)?$")
buckets = {}

def add(pkg, line):
    buckets.setdefault(pkg, []).append(line)

def stem(name):
    base = name[:-3] if name.endswith(".gz") else name
    man = re.match(r"(.+)\.(\d+)$", base)
    return man.group(1) if man else base

for path in sorted(root.rglob("*")):
    if not path.is_file() and not path.is_symlink():
        continue
    rel = "/" + path.relative_to(root).as_posix()
    if "/share/licenses/" in rel:
        continue
    name = rel.rsplit("/", 1)[-1]
    pkg = None
    if "/site-packages/libmount" in rel:
        pkg = "python3-libmount"
    elif "/share/locale/" in rel or ("/share/man/" in rel and "/share/man/man" not in rel):
        pkg = "util-linux-i18n"
    elif name in pc:
        pkg = pc[name]
    else:
        hit = soname.search(rel)
        if hit:
            pkg = hit.group(1) + ("-devel" if hit.group(2) is None else "")
        else:
            for needle, dest in include:
                if needle in rel:
                    pkg = dest
                    break
    if pkg is None and "/share/man/man3/" in rel:
        if name.startswith("ll2_") or name.startswith("lastlog2."):
            pkg = "liblastlog2-devel"
        elif name.startswith("libblkid."):
            pkg = "libblkid-devel"
        elif name.startswith("libfdisk."):
            pkg = "libfdisk-devel"
        elif name.startswith("libmount."):
            pkg = "libmount-devel"
        elif name.startswith("libsmartcols."):
            pkg = "libsmartcols-devel"
        elif name.startswith("uuid"):
            pkg = "libuuid-devel"
    if pkg is None and ("pam_lastlog2" in name or "lastlog2-import" in name or "lastlog2-tmpfiles" in name):
        pkg = "liblastlog2"
    if pkg is None and (name == "uuidd" or name.startswith("uuidd.") or name.startswith("uuidd-") or rel in ("/run/uuidd", "/var/lib/libuuid")):
        pkg = "uuidd"
    if pkg is None and (rel.startswith("/usr/bin/") or rel.startswith("/usr/sbin/") or "/bash-completion/" in rel or "/share/man/man" in rel or rel == "/etc/mtab"):
        tool = stem(name)
        if tool in core:
            pkg = "util-linux-core"
        elif tool in script_tools:
            pkg = "util-linux-script"
        elif tool == "uuidd":
            pkg = "uuidd"
        elif tool == "lastlog2":
            pkg = "util-linux"
    if pkg is None and ("/include/" in rel or rel.endswith(".pc") or rel.endswith(".so")):
        sys.exit("unclassified devel file " + rel)
    if pkg is None:
        pkg = "util-linux"
    prefix = ""
    if rel.rsplit("/", 1)[0] in ("/usr/bin", "/usr/sbin") and name in attrs:
        prefix = attrs[name]
    text = prefix + (rel if " " not in rel else '"' + rel + '"')
    add(pkg, text)

if full:
    have = {line.split()[-1].strip('"') for lines in buckets.values() for line in lines}
    for needle in ("uuidd.service", "lastlog2-import.service", "/site-packages/libmount/"):
        if not any(needle in item for item in have):
            sys.exit("missing " + needle)
names = [
    "util-linux", "util-linux-core", "util-linux-i18n", "util-linux-script", "uuidd",
    "python3-libmount", "libblkid", "libblkid-devel", "libfdisk", "libfdisk-devel",
    "libmount", "libmount-devel", "libsmartcols", "libsmartcols-devel",
    "libuuid", "libuuid-devel", "liblastlog2", "liblastlog2-devel",
]
for name in names:
    lines = buckets.get(name, [])
    (out / (name + ".files")).write_text(("\n".join(lines) + "\n") if lines else "")
PY

%files -f %{_builddir}/ul/util-linux.files
%license COPYING

%files -n util-linux-core -f %{_builddir}/ul/util-linux-core.files
%license COPYING

%files -n util-linux-i18n -f %{_builddir}/ul/util-linux-i18n.files
%license COPYING

%files -n util-linux-script -f %{_builddir}/ul/util-linux-script.files
%license COPYING

%files -n uuidd -f %{_builddir}/ul/uuidd.files
%license COPYING

%if %{without bootstrap} && !0%{?bootstrap}
%files -n python3-libmount -f %{_builddir}/ul/python3-libmount.files
%license libmount/COPYING
%endif

%files -n libblkid -f %{_builddir}/ul/libblkid.files
%license libblkid/COPYING

%files -n libblkid-devel -f %{_builddir}/ul/libblkid-devel.files
%license libblkid/COPYING

%files -n libfdisk -f %{_builddir}/ul/libfdisk.files
%license libfdisk/COPYING

%files -n libfdisk-devel -f %{_builddir}/ul/libfdisk-devel.files
%license libfdisk/COPYING

%files -n libmount -f %{_builddir}/ul/libmount.files
%license libmount/COPYING

%files -n libmount-devel -f %{_builddir}/ul/libmount-devel.files
%license libmount/COPYING

%files -n libsmartcols -f %{_builddir}/ul/libsmartcols.files
%license libsmartcols/COPYING

%files -n libsmartcols-devel -f %{_builddir}/ul/libsmartcols-devel.files
%license libsmartcols/COPYING

%files -n libuuid -f %{_builddir}/ul/libuuid.files
%license libuuid/COPYING

%files -n libuuid-devel -f %{_builddir}/ul/libuuid-devel.files
%license libuuid/COPYING

%files -n liblastlog2 -f %{_builddir}/ul/liblastlog2.files
%license liblastlog2/COPYING

%files -n liblastlog2-devel -f %{_builddir}/ul/liblastlog2-devel.files
%license liblastlog2/COPYING
