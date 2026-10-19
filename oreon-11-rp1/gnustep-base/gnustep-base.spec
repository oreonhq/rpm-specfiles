%global source0_hash d493ed2ba2a32f559f94e2ae5e339c440ae77d481dff1eb0d51eeac4d9127e33
Name: gnustep-base
Version: 1.31.0
Release:        1%{?dist}
License: GPL-3.0-or-later AND LGPL-2.0-or-later
Summary:        GNUstep Base library package
URL:     https://www.gnustep.org/
Source0:        https://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
Patch0: %{name}-use_system-wide_crypto-policies.patch
Patch1: %{name}-fix_GCC15.patch
Patch2: %{name}-fix_ending_tag_mismatch.patch
Patch3: %{name}-1.31.0-fix_s390x.patch
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: make
Conflicts: libFoundation
# oreon:deps
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  gcc
BuildRequires:  gcc-objc
BuildRequires:  gmp-devel
BuildRequires:  gnustep-make
BuildRequires:  gnutls-devel
BuildRequires:  libcurl-devel
BuildRequires:  libffi-devel
BuildRequires:  libicu-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  texi2html
BuildRequires:  texinfo-tex
# /oreon:deps
%description
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.

%package libs
Summary: GNUStep Base Libraries
Requires: gnustep-make%{?_isa} >= 2.9.2
%description libs
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.
This packages contains the run-time libraries for %{name}.

%package devel
Summary: Header of the GNUstep Base library packes
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files of the gnustep-base package.

%package doc
Summary: Documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnustep-filesystem
%description doc
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.
This package contains the documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N

%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup
%patch -P 2 -p1 -b .backup
%ifarch s390x
%patch -P 3 -p1 -b .backup
%endif

iconv -f iso-8859-1 -t utf-8 ChangeLog.2 -o ChangeLog.2.utf8
mv ChangeLog.2.utf8 ChangeLog.2

%build

ffi_include=$(pkg-config --cflags-only-I libffi | sed -e 's/^\-\I//')
export LDFLAGS="%{__global_ldflags}"
%gnustep_configure --disable-ffcall --with-ffi-include="$ffi_include"
%gnustep_make -n
%install
%gnustep_install -n
mv ${RPM_BUILD_ROOT}%{_bindir}/pl ${RPM_BUILD_ROOT}%{_bindir}/pllist
rm -f Examples/.cvsignore
rm -f Examples/.gdbinit
sed -e "s|GNUSTEP_SYSTEM_LIBRARY=|GNUSTEP_SYSTEM_LIBRARY=$RPM_BUILD_ROOT|" \
    -e "s|GNUSTEP_SYSTEM_HEADERS=|GNUSTEP_SYSTEM_HEADERS=$RPM_BUILD_ROOT|" \
    %{_sysconfdir}/GNUstep/GNUstep.conf >GNUstep.conf
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
export GNUSTEP_CONFIG_FILE=$(pwd)/GNUstep.conf
%gnustep_makedoc
%gnustep_installdoc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnustep-base-libs -f %{oreon_filedir}/gnustep-base-libs.list
%files -n gnustep-base-devel -f %{oreon_filedir}/gnustep-base-devel.list
%files -n gnustep-base-doc -f %{oreon_filedir}/gnustep-base-doc.list

%changelog

%autochangelog
