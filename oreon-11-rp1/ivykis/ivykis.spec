%global source0_hash 93e3e9b237695437cd63d4aa48a8d9dfd8b39bc28a192a5770d113c4fe9099ef
%global librarydir /%{_lib}
Summary:        Library for asynchronous I/O readiness notification
Name:           ivykis
Version:        0.43.2
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://libivykis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/libivykis/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
ivykis is a library for asynchronous I/O readiness notification.
It is a thin, portable wrapper around OS-provided mechanisms such
as epoll_create(2), kqueue(2), poll(2), poll(7d) (/dev/poll) and
port_create(3C).

ivykis was mainly designed for building high-performance network
applications, but can be used in any event-driven application that
uses poll(2)able file descriptors as its event sources.

%package devel
Summary:        Development files for the ivykis package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description devel
ivykis is a library for asynchronous I/O readiness notification.
This package contains files needed to develop applications using
ivykis.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --libdir=%{librarydir}
%{__make} %{_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{librarydir}/libivykis.{a,la}
%if "%{librarydir}" != "%{_libdir}"
  mkdir -p %{buildroot}%{_libdir}
  mv %{buildroot}%{librarydir}/pkgconfig %{buildroot}%{_libdir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n ivykis-devel -f %{oreon_filedir}/ivykis-devel.list

%changelog

%autochangelog
