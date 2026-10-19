%global source0_hash 568416d854d1c1e5eac743c9f56db6fa0d6a8144daa74a799d0556bb6b50e679
%global sover 0
Name:		riemann-c-client
Version:	1.10.5
Release:        1%{?dist}
Summary:        The riemann C client
License:	GPL-2.0-only
Url:		https://github.com/algernon/riemann-c-client
Source0:        https://github.com/algernon/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0000:	riemann-c-client-1.10.5-gcc10_symver.patch
Patch0001:      fix-gnutls-send-recv-when-return-eagain
Patch0002:      fix-gnutls-send-recv-when-return-less-than-expected
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  json-c-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c-devel
# /oreon:deps
%description
This is a C client library for the Riemann monitoring system, providing a
convenient and simple API, high test coverage and a copyleft license,
along with API and ABI stability.

%package devel
Summary:	Development files for riemann-c-client
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	protobuf-c-devel%{?_isa}
Requires:	json-c-devel
%description devel
This package provides files necessary for riemann-c-client development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{name}-%{version}
%patch -P0 -p1 -b.gcc10_symver
%patch -P1 -p1
%patch -P2 -p1
autoreconf -fiv

%build

%configure --disable-static
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/libriemann-client.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n riemann-c-client-devel -f %{oreon_filedir}/riemann-c-client-devel.list

%changelog

%autochangelog
