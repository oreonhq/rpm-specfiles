%global source0_hash 2cbbea55a5d6895c9f0116a9a9ce3afb86df383cd05c9d6c1a4238e5e5c8f51d
Name:           log4cpp
Version:        1.1.3
Release:        1%{?dist}
Summary:        C++ logging library
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/log4cpp/
Source0:        http://downloads.sourceforge.net/log4cpp/%{name}-%{version}.tar.gz
Patch0:         log4cpp-1.0-gcc43.patch
Patch1:         log4cpp-1.0-remove-pc-cflags.patch
Patch2:         log4cpp-1.0-fix-doc-dest.patch
Patch3:         log4cpp-1.0-no-snprintf.patch
Patch4:         log4cpp-version-1.1.3.patch
Patch5:         03_aclocal_automake.diff
Patch6:         log4cpp-configure-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
A library of C++ classes for flexible logging to files, syslog, IDSA and
other destinations. It is modeled after the Log for Java library
(http://www.log4j.org), staying as close to their API as is reasonable.

%package devel
Summary:        Header files, libraries and development man pages  %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?el4}%{?el5}
Requires:       pkgconfig
%endif
%description devel
This package contains the header files, static libraries and development
man pages for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary:        Development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description doc
This package contains the development documentation for %{name}.
If you like to documentation to develop programs using %{name},
you will need to install %{name}-devel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n log4cpp
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1 -b .no-snprintf
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
# Delete non-free (but freely distributable) file under Artistic 1.0
# just to be sure we're not using it.
rm -rf src/snprintf.c
#Convert line endings.
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

%build

autoreconf -fi
%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/share/doc/log4cpp-%{version} rpmdocs
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n log4cpp-devel -f %{oreon_filedir}/log4cpp-devel.list
%files -n log4cpp-doc -f %{oreon_filedir}/log4cpp-doc.list

%changelog

%autochangelog
