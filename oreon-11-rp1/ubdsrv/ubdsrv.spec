%global source0_hash 3d55d170ebc317e156189ccc927fb48b47841f978172f73c2a711ef5b4647cdc
%global forgeurl https://github.com/ublk-org/ublksrv
%global commit a2f2daa9f02509a008d9304c197f6a2b0da0ad38
Version:       1.8
%forgemeta
Summary:        Userspace block driver server and ublk tool
Name:          ubdsrv
Release:        1%{?dist}
URL:           %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/ublksrv-%{commit}.tar.gz
License:       LGPLv2+ or MIT
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  liburing-devel
BuildRequires:  make
BuildRequires:  pkgconf
# /oreon:deps
%description
This package allows you to write Linux block devices in userspace.  It
contains a library which can be linked to programs that implement
Linux userspace block devices, and also the "ublk" program which can
be used to create, list and delete ublk devices.

%package devel
Summary:       Development tools for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}
Provides:      ublksrv = %{version}-%{release}
%description devel
This package contains development tools for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

autoreconf -f -i
%{configure} --disable-static
make V=1 %{?_smp_mflags}
%install
%{make_install}
rm %{buildroot}%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ubdsrv-devel -f %{oreon_filedir}/ubdsrv-devel.list

%changelog

%autochangelog
