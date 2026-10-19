%global source0_hash 5991020192f52cc40fa852fbf6bbf5bd5db5d5d00aa9905c67f6f0eadeed48ea
Name:       log4c
Version:    1.2.4
Release:        1%{?dist}
Summary:        Library for logging application messages
License:    LicenseRef-Callaway-LGPLv2+
URL:        http://log4c.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:     reinit.patch
Patch1:     format.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

%package devel
Summary:    Header files, libraries and development documentation for %{name}
Requires:   %{name} = %{version}-%{release}
%description devel
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

This package contains development files for %{name}. If you like to develop
programs using %{name}, you will need to install %{name}-devel.

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch
%description doc
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

This package contains %{name} documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build

%configure --enable-doc --enable-test --disable-static
make %{?_smp_mflags}
%install
make install docdir=%{_pkgdocdir} DESTDIR=%{buildroot}
mv %{buildroot}/etc/log4crc.sample %{buildroot}%{_pkgdocdir}/
rm %{buildroot}%{_libdir}/*.la
sed -r -i \
    -e 's|^libdir=/usr/lib(64)?$|libdir=/usr/lib|' \
    -e 's|-L\$libdir ||' \
    -e 's|-I\$includedir ||' %{buildroot}%{_bindir}/log4c-config
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n log4c-devel -f %{oreon_filedir}/log4c-devel.list
%files -n log4c-doc -f %{oreon_filedir}/log4c-doc.list

%changelog

%autochangelog
