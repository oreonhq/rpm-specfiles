%global source0_hash b7d9ad1d73b4a33b86dc8e7af5749d33b5e121588ad8bbf499bb63e7901aa5a2

Name:           dolphin-connector
Version:        1.2
Release:        44%{?dist}
Summary:        Simple MySQL C API wrapper for C++

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/poetinha/dolphin-connector
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtool mariadb-connector-c-devel boost-devel
BuildRequires: make

%description
Dolphin Connector is a simple MySQL C API wrapper for C++.

It is originally designed to be as efficient as is possible,
and makes no use of exceptions.

%package devel
Summary: Development files for Dolphin Connector
Requires: %{name} = %{version}-%{release}
Requires: mariadb-connector-c-devel
Requires: boost-devel

%description devel
Dolphin Connector development package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
./autogen.sh

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# cleanup
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -f sample/Makefile*

%ldconfig_scriptlets

%files
%doc ChangeLog LICENSE README TODO
%{_libdir}/libdolphinconn.so.*

%files devel
%doc sample
%{_includedir}/dolphinconn
%{_libdir}/libdolphinconn.so

%changelog
%autochangelog
