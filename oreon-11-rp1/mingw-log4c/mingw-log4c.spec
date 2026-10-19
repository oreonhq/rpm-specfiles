%global source0_hash 5991020192f52cc40fa852fbf6bbf5bd5db5d5d00aa9905c67f6f0eadeed48ea
%{?mingw_package_header}
Name:		mingw-log4c
Version:	1.2.4
Release:        1%{?dist}
Summary:        Library for logging application messages
License:	LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-MIT
URL:		http://log4c.sourceforge.net/
Source0:        http://downloads.sourceforge.net/log4c/log4c-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

%package -n mingw32-log4c
Summary:	MinGW compiled log4c library for the Win32 target
%description -n mingw32-log4c
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

This package is MinGW compiled log4c library for the Win32 target.

%package -n mingw64-log4c
Summary:	MinGW compiled log4c library for the Win64 target
%description -n mingw64-log4c
Log4c is a C language library for flexible logging to files, syslog and other
destinations. It is modeled after the Log for Java library (log4j),
staying as close to their API as is reasonable.

This package is MinGW compiled log4c library for the Win64 target.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n log4c-%{version}

%build

%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}
%install
%mingw_make_install DESTDIR=%{buildroot}
rm %{buildroot}%{mingw32_sysconfdir}/log4crc.sample
rm %{buildroot}%{mingw64_sysconfdir}/log4crc.sample
rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la
chmod -x %{buildroot}%{mingw32_libdir}/*.def
chmod -x %{buildroot}%{mingw64_libdir}/*.def
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%oreon_autofiles mingw32-log4c usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-log4c usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-log4c -f %{oreon_filedir}/mingw32-log4c.list
%files -n mingw64-log4c -f %{oreon_filedir}/mingw64-log4c.list

%changelog

%autochangelog
