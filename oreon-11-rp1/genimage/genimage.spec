%global source0_hash 397545be2fa52d482c5fba9a11897c61324bfc559ea0efb700b9edba7a807b55
%global fs_block_tools %(cat <<EOF
e2fsprogs \\
genext2fs \\
genisoimage \\
f2fs-tools \\
btrfs-progs \\
squashfs-tools \\
dosfstools \\
mtools \\
mdadm \\
qemu-img \\
mtd-utils \\
mtd-utils-ubi \\
uboot-tools
EOF)
Name:           genimage
Version:        20
Release:        1%{?dist}
Summary:        Flexible filesystem and disk image generator
License:        GPL-2.0-only
URL:            https://github.com/pengutronix/genimage/
Source0:        https://github.com/pengutronix/%{name}//releases/download/v%{version}/%{name}-%{version}.tar.xz
Recommends:     %{fs_block_tools}
ExcludeArch: s390x %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  btrfs-progs
BuildRequires:  coreutils
BuildRequires:  dosfstools
BuildRequires:  e2fsprogs
BuildRequires:  f2fs-tools
BuildRequires:  fakeroot
BuildRequires:  gcc
BuildRequires:  genext2fs
BuildRequires:  genisoimage
BuildRequires:  libconfuse-devel
BuildRequires:  libtool
BuildRequires:  mdadm
BuildRequires:  mtd-utils
BuildRequires:  mtd-utils-ubi
BuildRequires:  mtools
BuildRequires:  python3-docutils
BuildRequires:  qemu-img
BuildRequires:  squashfs-tools
BuildRequires:  uboot-tools
# /oreon:deps
%description
genimage is a tool to generate multiple filesystem and flash/disk
images from a given root filesystem tree. genimage is intended to 
be run in a fakeroot environment. 
It also supports creating flash/disk images out of different 
file-system images and files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fi

%build

%configure
%make_build
rst2man README.rst > %{name}.1
%install
%make_install
install -D -m644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%check

make check || ! cat test-suite.log
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
