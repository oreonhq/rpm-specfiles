# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 686de715e27c30b579d468ab02d7a841ab2a1f553975754fd134ebf627b26149

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name: fsverity-utils
Version:        1.7
Release:        1%{?dist}
Summary: fsverity utilities

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://github.com/ebiggers/fsverity-utils
Source0:        https://github.com/ebiggers/fsverity-utils/archive/v%{version}/fsverity-utils-%{version}.tar.gz
# https://github.com/ebiggers/fsverity-utils/pull/5
Patch0:        openssl4.patch

BuildRequires: gcc make
BuildRequires: kernel-headers glibc-headers
BuildRequires: openssl-devel
BuildRequires:  oreon-rpm-macros
Requires:      libfsverity = %{version}-%{release}

%description
This is fsverity, a userspace utility for fs-verity.
fs-verity is a Linux kernel feature that does transparent on-demand
integrity/authenticity verification of the contents of read-only files,
using a hidden Merkle tree (hash tree) associated with the file.
The mechanism is similar to dm-verity, but implemented at the file level
rather than at the block device level. The fsverity utility allows you
to set up fs-verity protected files.

%package -n libfsverity
Summary:          Development package for fsverity-utils
%description -n libfsverity
Library for fsverity-utils.

%package devel
Summary:          Development package for fsverity-utils
Requires:         libfsverity = %{version}-%{release}
Requires:         %{name} = %{version}-%{release}
%description devel
Development package for fsverity-utils. This package includes the
libfsverity header and library files.

%prep
%oreon_sha256

%autosetup -p1

%build
%set_build_flags
%make_build CFLAGS="$CFLAGS -g" USE_SHARED_LIB=1

%install
%set_build_flags
%make_install PREFIX=/usr LIBDIR=%{_libdir}  CFLAGS="$CFLAGS -g" USE_SHARED_LIB=1
find %{buildroot} -type f -name "*.a" -delete

%files
%doc README.md
%{_bindir}/fsverity
%{_mandir}/man1/fsverity.1.gz

%files -n libfsverity
%license LICENSE
%{_libdir}/libfsverity.so.0

%files devel
%{_includedir}/libfsverity.h
%{_libdir}/libfsverity.so
%{_libdir}/pkgconfig/libfsverity.pc

