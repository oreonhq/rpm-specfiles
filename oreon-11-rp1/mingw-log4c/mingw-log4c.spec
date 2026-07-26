%global source0_hash 5991020192f52cc40fa852fbf6bbf5bd5db5d5d00aa9905c67f6f0eadeed48ea

%{?mingw_package_header}

Name:		mingw-log4c
Version:	1.2.4
Release:	28%{?dist}
Summary:	Library for logging application messages

# main license is LGPLv2
# src/sd/stack.c under MIT licence
# Automatically converted from old format: LGPLv2 and MIT - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-MIT
URL:		http://log4c.sourceforge.net/
Source0:	http://downloads.sourceforge.net/log4c/log4c-%{version}.tar.gz

BuildArch:	noarch

BuildRequires: make
BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-binutils
BuildRequires:	mingw32-expat

BuildRequires:	mingw64-filesystem >= 95
BuildRequires:	mingw64-gcc
BuildRequires:	mingw64-binutils
BuildRequires:	mingw64-expat

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
# example config file below shouldn't live in /etc/
rm %{buildroot}%{mingw32_sysconfdir}/log4crc.sample
rm %{buildroot}%{mingw64_sysconfdir}/log4crc.sample
# no libtool file
rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la
# .def is not neded to be as executable
chmod -x %{buildroot}%{mingw32_libdir}/*.def
chmod -x %{buildroot}%{mingw64_libdir}/*.def
# no duplicities in documentation
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

%files -n mingw32-log4c
%doc COPYING AUTHORS ChangeLog NEWS README build_win32/log4crc.sample
%{mingw32_bindir}/liblog4c-3.dll
%{mingw32_bindir}/log4c-config
%{mingw32_includedir}/*
%{mingw32_libdir}/liblog4c.dll.a
%{mingw32_libdir}/liblog4c.def
%{mingw32_libdir}/pkgconfig/log4c.pc
%{mingw32_datadir}/aclocal/log4c.m4

%files -n mingw64-log4c
%doc COPYING AUTHORS ChangeLog NEWS README build_win64/log4crc.sample
%{mingw64_bindir}/liblog4c-3.dll
%{mingw64_bindir}/log4c-config
%{mingw64_includedir}/*
%{mingw64_libdir}/liblog4c.dll.a
%{mingw64_libdir}/liblog4c.def
%{mingw64_libdir}/pkgconfig/log4c.pc
%{mingw64_datadir}/aclocal/log4c.m4

%changelog
%autochangelog
