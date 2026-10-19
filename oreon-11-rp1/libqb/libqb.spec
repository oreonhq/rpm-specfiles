%global source0_hash 326a69fb5b2ee4479f0db4f98d10d670ad0798b5ded8c4cfd585b765fd8941e8
%bcond_with check
Name:           libqb
Version:        2.0.10
Release:        1%{?dist}
Summary:        Library providing high performance logging, tracing, ipc, and poll
License:        LGPL-2.1-or-later
URL:            https://github.com/ClusterLabs/libqb
Source0:        https://github.com/ClusterLabs/libqb/releases/download/v%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  procps
# /oreon:deps
%description
A "Quite Boring" library that provides high-performance, reusable features for client-server
architecture, such as logging, tracing, inter-process communication (IPC),
and polling.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build

./autogen.sh
%configure --disable-static
%{make_build}
%if 0%{?with_check}
%check

make check V=1
%endif
%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -delete
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     doxygen2man
Summary:        Program to create nicely-formatted man pages from Doxygen XML files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n doxygen2man
This package contains a program to create nicely-formatted man pages from Doxygen XML files

%files -f %{oreon_filedir}/main.list
%files -n libqb-devel -f %{oreon_filedir}/libqb-devel.list
%files -n doxygen2man -f %{oreon_filedir}/doxygen2man.list

%changelog

%autochangelog
