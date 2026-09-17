%global source0_hash 8215844d14737d8fbb09fe1b1eafe688a8c790eafc8413a26c08e5795ac9ccd3

# Testsuite is CPU and disk space intensive, partially also just broken
%{!?testsuite: %global testsuite 1}

Summary:        Utility to clone and restore a partition
Name:           partclone
Version:        0.3.47
Release:        1%{?dist}
# Partclone itself is GPL-2.0-or-later but uses other source codes, breakdown:
# GPL-3.0-or-later: fail-mbr/fail-mbr.S
# BSD-2-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-3.0-or-later: src/btrfs*
# GPL-2.0-or-later: src/exfat*
# GPL-2.0-only: src/f2fs/
# GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only: src/xfs*
# GPL-2.0-or-later: src/{apfs,dd,extfs,fat,f2fs,hfsplus,minix,nilfs,ntfsclone-ng,part}clone*
# GPL-2.0-or-later: src/{{fuseimg,info,main,ntfsfixboot,readblock}.c,progress*}
# LGPL-2.0-or-later: src/gettext.h
# Unused source code (= not built): src/{jfs,reiser,ufs,vmfs}*
License:        BSD-2-Clause AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:            https://partclone.org/
Source0:        https://github.com/Thomas-Tsai/partclone/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libuuid-devel
BuildRequires:  xxhash-devel
BuildRequires:  fuse3-devel
BuildRequires:  userspace-rcu-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel >= 1.1.0
BuildRequires:  zlib-devel
BuildRequires:  libzstd-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  ntfs-3g-devel
BuildRequires:  libblkid-devel
BuildRequires:  libmount-devel
%if 0%{?fedora}
BuildRequires:  nilfs-utils-devel
%endif
BuildRequires:  pkgconfig(bash-completion)
%if 0%{?testsuite}
BuildRequires:  e2fsprogs
BuildRequires:  ntfsprogs
BuildRequires:  dosfstools
BuildRequires:  xfsprogs
BuildRequires:  exfatprogs
%if 0%{?fedora}
BuildRequires:  btrfs-progs
BuildRequires:  f2fs-tools
BuildRequires:  hfsplus-tools
%endif
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
Recommends:     bash-completion
# Partclone depends on specific source files, either not exposed to -devel package or no -devel package exists
# Version information origin: src/btrfs/libbtrfs/version.h
Provides:       bundled(libbtrfs) = 6.16
Provides:       bundled(libbtrfsutil) = 6.16
# Version information origin: https://github.com/Thomas-Tsai/partclone/pull/290
Provides:       bundled(xfsprogs-libs) = 6.13.0

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
%if 0%{?fedora}
  --enable-nilfs2 \
%else
  --disable-nilfs2 \
%endif
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

%if 0%{?testsuite}
%check
# NILFS2 tests must be run as root (mockbuild is unprivileged)
sed -e 's/^\(am__append_[[:digit:]]* = nilfs2.test\)/#\1/' \
    -i tests/Makefile

# Reiser4 tests require reiser4progs (which are not packaged)
sed -e 's/^\(am__append_[[:digit:]]* = reiser4.test\)/#\1/' \
    -i tests/Makefile

# No btrfs-progs, f2fs-tools and hfsplus-tools in RHEL or EPEL
%if 0%{?rhel}
sed -e 's/^\(am__append_[[:digit:]]* = btrfs.test\)/#\1/' \
    -e 's/^\(am__append_[[:digit:]]* = f2fs.test\)/#\1/' \
    -e 's/^\(am__append_[[:digit:]]* = hfsplus.test\)/#\1/' \
    -i tests/Makefile
%endif

make check || { cat tests/test-suite.log; exit 1; }
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%{_sbindir}/%{name}.*
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man8/%{name}*.8*

%changelog
%autochangelog
