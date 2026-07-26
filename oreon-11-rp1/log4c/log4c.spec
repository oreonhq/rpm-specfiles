%global source0_hash 5991020192f52cc40fa852fbf6bbf5bd5db5d5d00aa9905c67f6f0eadeed48ea

Name:       log4c
Version:    1.2.4
Release:    35%{?dist}
Summary:    Library for logging application messages

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
URL:        http://log4c.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Double free or corruption with multiple log4c_init()/log4c_fini()
# https://bugzilla.redhat.com/show_bug.cgi?id=1095366
# Applied in upstream
Patch0:     reinit.patch
# Applied in upstream
Patch1:     format.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make

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
# example config file below shouldn't live in /etc/
mv %{buildroot}/etc/log4crc.sample %{buildroot}%{_pkgdocdir}/
rm %{buildroot}%{_libdir}/*.la
# munge log4c-config to prevent file conflicts on multilib systems,
# the default paths are not needed in the build flags anyway
sed -r -i \
    -e 's|^libdir=/usr/lib(64)?$|libdir=/usr/lib|' \
    -e 's|-L\$libdir ||' \
    -e 's|-I\$includedir ||' %{buildroot}%{_bindir}/log4c-config

%ldconfig_scriptlets

%files
%dir %{_pkgdocdir}/
%license %{_pkgdocdir}/COPYING
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/NEWS
%{_pkgdocdir}/README
%{_pkgdocdir}/log4crc.sample
%{_libdir}/liblog4c.so.3
%{_libdir}/liblog4c.so.3.*

%files devel
%{_libdir}/liblog4c.so
%{_libdir}/pkgconfig/*.pc
%{_bindir}/*
%{_includedir}/*
%{_datadir}/aclocal/log4c.m4
%{_mandir}/man1/*
%{_mandir}/man3/*

%files doc
%{_pkgdocdir}/html/

%changelog
%autochangelog
