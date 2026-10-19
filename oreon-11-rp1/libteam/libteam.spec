%global source0_hash a0a0fbf75423cbb835c2fc667e861090c925f9899f162b1d1f893b75c0ad5cfe
Name: libteam
Version: 1.32
Release:        1%{?dist}
Summary:        Library for controlling team network device
License: LGPL-2.0-or-later
URL: http://www.libteam.org
Source0:        http://www.libteam.org/files/libteam-%{version}.tar.gz
Obsoletes: network-scripts-teamd < 1.32-8
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  jansson-devel
BuildRequires:  libdaemon-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  swig
BuildRequires:  systemd
# /oreon:deps
%description
This package contains a library which is a user-space
counterpart for team network driver. It provides an API
to control team network devices.

%package devel
Summary: Libraries and header files for libteam development
Requires: %{name}%{?_isa} = %{version}-%{release}
%package doc
Summary: API documentation for libteam and libteamd
Requires: %{name}%{?_isa} = %{version}-%{release}
%description doc
This package contains libteam and libteamd API documentation

%package -n teamd
Summary: Team network device control daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
%package -n teamd-devel
Summary: Libraries and header files for teamd development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The libteam-devel package contains the header files and libraries
necessary for developing programs using libteam.

%description -n teamd
The teamd package contains team network device control daemon.

%description -n teamd-devel
The teamd-devel package contains the header files and libraries
necessary for developing programs using libteamdctl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

# prepare example dir for -devel
mkdir -p _tmpdoc1/examples
rm examples/python/*.py
cp -p examples/*.c _tmpdoc1/examples

%build

%configure --disable-static
make %{?_smp_mflags}
make html
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name \*.la -delete
rm -rf $RPM_BUILD_ROOT/%{_bindir}/team_*
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d
install -p teamd/dbus/teamd.conf $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d/
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p teamd/redhat/systemd/teamd@.service $RPM_BUILD_ROOT%{_unitdir}
install -p -m 755 utils/bond2team $RPM_BUILD_ROOT%{_bindir}/bond2team
%ldconfig_scriptlets
%oreon_autofiles teamd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles teamd-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libteam-devel -f %{oreon_filedir}/libteam-devel.list
%files -n libteam-doc -f %{oreon_filedir}/libteam-doc.list
%files -n teamd -f %{oreon_filedir}/teamd.list
%files -n teamd-devel -f %{oreon_filedir}/teamd-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.32-13
- Prepare for Oreon 11 (RP1)
