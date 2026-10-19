%global source0_hash ba66e6c7b46da3339bc7369ca90d647383660f8e74874a82dd8034a39193876e
%{!?testsuite: %global testsuite 1}
Summary:        Utility to clone and restore a partition
Name:           partclone
Version:        0.3.50
Release:        1%{?dist}
License:        BSD-2-Clause AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:            https://partclone.org/
Source0:        https://github.com/Thomas-Tsai/partclone/archive/%{version}/%{name}-%{version}.tar.gz
%if 0%{?testsuite}
%endif
Recommends:     bash-completion
Provides:       bundled(libbtrfs) = 6.16
Provides:       bundled(libbtrfsutil) = 6.16
Provides:       bundled(xfsprogs-libs) = 6.13.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  dosfstools
BuildRequires:  e2fsprogs
BuildRequires:  e2fsprogs-devel
BuildRequires:  exfatprogs
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libblkid-devel
BuildRequires:  libmount-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libxslt
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  ntfs-3g-devel
BuildRequires:  ntfsprogs
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  userspace-rcu-devel
BuildRequires:  xfsprogs
BuildRequires:  xxhash-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Partclone provides utilities to clone and restore used blocks on a partition
and is designed for higher compatibility of the file system by using existing
libraries, e.g. e2fslibs is used to read and write the ext2 partition.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# https://github.com/Thomas-Tsai/partclone/issues/285
autoreconf -i -f

%build

%configure \
  --enable-fuse \
  --enable-extfs \
  --enable-xfs \
  --disable-reiserfs \
  --disable-reiser4 \
  --enable-hfsp \
  --enable-apfs \
  --enable-fat \
  --enable-exfat \
  --enable-f2fs \
  --disable-nilfs2 \
  --enable-ntfs \
  --disable-ufs \
  --disable-vmfs \
  --disable-jfs \
  --enable-btrfs \
  --enable-minix \
  --enable-ncursesw \
  --enable-fs-test
%make_build
%install
%make_install
mv -f $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/%{name}{-completion,}
%find_lang %{name}
%oreon_autofiles main
%if 0%{?testsuite}
%check

sed -e 's/^\(am__append_[[:digit:]]* = nilfs2.test\)/#\1/' \
    -i tests/Makefile
sed -e 's/^\(am__append_[[:digit:]]* = reiser4.test\)/#\1/' \
    -i tests/Makefile
make check || { cat tests/test-suite.log; exit 1; }
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
