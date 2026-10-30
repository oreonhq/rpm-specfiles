%global source0_hash e596083744e746be7d2823b62b43f4418dd7bf56303b4dc09e6fe8112fe3d7ed
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: util-linux
Version: 2.41.6
Release: 1%{?dist}
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
%endif

%description
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%package devel
Summary: Low-level system utilities and libraries
Requires: util-linux%{?_isa} = %{version}-%{release}

%description devel
util-linux provides libmount, libblkid, libfdisk and libsmartcols.

%prep
%oreon_sha256
%autosetup -n util-linux-%{version} -p1

%build
%oreon_configure \
  --disable-static \
  --with-systemd=no \
  --without-python \
  --with-ncursesw \
  --enable-libuuid \
  --enable-libblkid \
  --enable-libmount \
  --enable-libfdisk \
  --enable-libsmartcols
%oreon_make

%install
fakeroot %oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel
python3 - %{_builddir}/%{name}.files %{_builddir}/%{name}-devel.files << 'PY'
import sys
from pathlib import Path
attrs = {
    "/bin/mount": "%attr(4755,root,root) ",
    "/bin/umount": "%attr(4755,root,root) ",
    "/bin/su": "%attr(4755,root,root) ",
    "/bin/wall": "%attr(2755,root,tty) ",
    "/bin/write": "%attr(2755,root,tty) ",
}
for name in sys.argv[1:]:
    path = Path(name)
    if not path.is_file():
        continue
    lines = []
    for line in path.read_text().splitlines():
        item = line.split()[-1] if line else ""
        prefix = ""
        for suffix, attr in attrs.items():
            if item.endswith(suffix):
                prefix = attr
                break
        lines.append(prefix + line)
    path.write_text("\n".join(lines) + "\n")
PY

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
