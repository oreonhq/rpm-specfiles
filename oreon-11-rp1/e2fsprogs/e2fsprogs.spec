%global source1_hash ff826cf86828bf3ed8a7fcbe3e5c0c171f8ebfc5f46c43b27adc1ffc2c6a7b9c
%global source0_hash fd5bf388cbdbe006a3d3b318d983b2948382440acc85a87f1e7d108653e8db0b
Summary:        Utilities for managing ext2, ext3, and ext4 file systems
Name: e2fsprogs
Version: 1.47.4
Release:        1%{?dist}
License: GPL-2.0-only
Source0:        https://www.kernel.org/pub/linux/kernel/people/tytso/%{name}/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/linux/kernel/people/tytso/%{name}/v%{version}/%{name}-%{version}.tar.sign
Source2: tytso-key.asc
Url: http://e2fsprogs.sourceforge.net/
Requires: e2fsprogs-libs%{?_isa} = %{version}-%{release}
Requires: libcom_err%{?_isa} = %{version}-%{release}
Requires: libss = %{version}-%{release}
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/mke2fs
Provides: /usr/sbin/fsck.ext2
Provides: /usr/sbin/fsck.ext3
Provides: /usr/sbin/fsck.ext4
Provides: /usr/sbin/mkfs.ext2
Provides: /usr/sbin/mkfs.ext3
Provides: /usr/sbin/mkfs.ext4
%endif
Patch 0:	0001-remove-local-PATH.patch
# oreon:deps
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  libblkid-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  multilib-rpm-config
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  texinfo
BuildRequires:  xz
# /oreon:deps
%description
The e2fsprogs package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in second,
third and fourth extended (ext2/ext3/ext4) file systems. E2fsprogs
contains e2fsck (used to repair file system inconsistencies after an
unclean shutdown), mke2fs (used to initialize a partition to contain
an empty ext2 file system), debugfs (used to examine the internal
structure of a file system, to manually repair a corrupted
file system, or to create test cases for e2fsck), tune2fs (used to
modify file system parameters), and most of the other core ext2fs
file system utilities.

You should install the e2fsprogs package if you need to manage the
performance of an ext2, ext3, or ext4 file system.

%package libs
Summary: Ext2/3/4 file system specific shared libraries
License: GPL-2.0-only AND LGPL-2.0-only
Requires: libcom_err%{?_isa} = %{version}-%{release}
%description libs
E2fsprogs-libs contains libe2p and libext2fs, the libraries of the
e2fsprogs package.

These libraries are used to directly access ext2/3/4 file systems
from user space.

%package static
Summary: Ext2/3/4 file system specific static libraries
License: GPL-2.0-only AND LGPL-2.0-only
%description static
E2fsprogs-static contains all static libraries built from e2fsprogs,
including libext2fs, libcom_err, libe2p, and libss.

These libraries are used to directly access ext2/3/4 file systems
from user space, and perform other useful functions.

%package devel
Summary: Ext2/3/4 file system specific libraries and headers
License: GPL-2.0-only AND LGPL-2.0-only
Requires: e2fsprogs-libs%{?_isa} = %{version}-%{release}
Requires: libcom_err-devel%{?_isa} = %{version}-%{release}
Requires: gawk
Requires: pkgconfig
%description devel
E2fsprogs-devel contains the libraries and header files needed to
develop second, third and fourth extended (ext2/ext3/ext4)
file system specific programs.

You should install e2fsprogs-devel if you want to develop ext2/3/4
file system specific programs. If you install e2fsprogs-devel, you'll
also want to install e2fsprogs.

%package -n libcom_err
Summary: Common error description library
License: MIT
%description -n libcom_err
This is the common error description library, part of e2fsprogs.

libcom_err is an attempt to present a common error-handling mechanism.

%package -n libcom_err-devel
Summary: Common error description library
License: MIT
Requires: libcom_err%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description -n libcom_err-devel
This is the common error description development library and headers,
part of e2fsprogs.  It contains the compile_et command, used
to convert a table listing error-code names and associated messages
messages into a C source file suitable for use with the library.

libcom_err is an attempt to present a common error-handling mechanism.

%package -n libss
Summary: Command line interface parsing library
License: MIT
Requires: libcom_err%{?_isa} = %{version}-%{release}
%description -n libss
This is libss, a command line interface parsing library, part of e2fsprogs.

This package includes a tool that parses a command table to generate
a simple command-line interface parser, the include files needed to
compile and use it.

It was originally inspired by the Multics SubSystem library.

%package -n libss-devel
Summary: Command line interface parsing library
License: MIT
Requires: libss%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description -n libss-devel
This is the command line interface parsing (libss) development library
and headers, part of e2fsprogs.  It contains the mk_cmds command, which
parses a command table to generate a simple command-line interface parser.

It was originally inspired by the Multics SubSystem library.

%package -n e2scrub
Summary: Online Ext4 metadata consistency checking tool and service
License: GPL-2.0-only AND LGPL-2.0-only
Recommends: /usr/sbin/sendmail
Requires: systemd
Requires: util-linux
Requires: lvm2
Requires: e2fsprogs%{?_isa} = %{version}-%{release}
%description -n e2scrub
This package includes e2scrub script that can check ext[234] file system
metadata consistency while the file system is online. It also containes a
systemd service that can be enabled to do consistency check periodically.

The file system consistency check can be performed online and does not
require the file system to be unmounted. It uses lvm snapshots to do this
which means that it can only be done on file systems that are on a lvm
managed device with some free space available in respective volume group.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
xzcat '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%setup -q

%patch -P0 -p1
# Remove flawed tests
rm -rf tests/m_rootdir_acl

%global _udevdir %{_prefix}/lib/udev/rules.d

%build

%configure CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
	   --enable-elf-shlibs --enable-nls --disable-uuidd --disable-fsck \
	   --disable-e2initrd-helper --disable-libblkid --disable-libuuid \
	   --enable-quota --with-root-prefix=/usr --with-crond-dir=no
%make_build
%install
rm -rf %{buildroot}
export PATH=/sbin:$PATH
%make_install install-libs \
	root_sbindir=%{_sbindir} root_libdir=%{_libdir}
%multilib_fix_c_header --file %{_includedir}/ext2fs/ext2_types.h
chmod +w %{buildroot}%{_libdir}/*.a
%find_lang %{name}
%oreon_autofiles libcom_err usr/*/lib*.so.*
%oreon_autofiles libcom_err-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libss usr/*/lib*.so.*
%oreon_autofiles libss-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles e2scrub usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make PRINT_FAILED=yes fullcheck
%ldconfig_scriptlets libs
%ldconfig_scriptlets -n libcom_err
%ldconfig_scriptlets -n libss
%files -f %{oreon_filedir}/main.list
%files -n e2fsprogs-libs -f %{oreon_filedir}/e2fsprogs-libs.list
%files -n e2fsprogs-static -f %{oreon_filedir}/e2fsprogs-static.list
%files -n e2fsprogs-devel -f %{oreon_filedir}/e2fsprogs-devel.list
%files -n libcom_err -f %{oreon_filedir}/libcom_err.list
%files -n libcom_err-devel -f %{oreon_filedir}/libcom_err-devel.list
%files -n libss -f %{oreon_filedir}/libss.list
%files -n libss-devel -f %{oreon_filedir}/libss-devel.list
%files -n e2scrub -f %{oreon_filedir}/e2scrub.list

%changelog

%autochangelog
