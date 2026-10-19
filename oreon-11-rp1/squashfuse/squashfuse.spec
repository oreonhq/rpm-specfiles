%global source0_hash 4fda456c0f28f64db7e97f259069e747ffe29dcd13d4e2327350997b32eac914
Name:     squashfuse
Version:  0.6.3
Release:        1%{?dist}
Summary:        FUSE filesystem to mount squashfs archives
License:  BSD-2-Clause
URL:      https://github.com/vasi/squashfuse
Source0:        https://github.com/vasi/squashfuse/archive/%{version}/%{name}-%{version}.tar.gz
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Squashfuse lets you mount SquashFS archives in user-space. It supports almost
all features of the SquashFS format, yet is still fast and memory-efficient.
SquashFS is an efficiently compressed, read-only storage format. Support for it
has been built into the Linux kernel since 2009. It is very common on Live CDs
and embedded Linux distributions.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Libraries and header files for developing applications that use %{name}.

%package libs
Summary: Libraries for %{name}
%description libs
Libraries for running %{name} applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --disable-static --disable-demo
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n squashfuse-devel -f %{oreon_filedir}/squashfuse-devel.list
%files -n squashfuse-libs -f %{oreon_filedir}/squashfuse-libs.list

%changelog

%autochangelog
