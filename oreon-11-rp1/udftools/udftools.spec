Summary: Linux UDF Filesystem userspace utilities
Name: udftools
Version: 2.3
Release: 13%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://sourceforge.net/projects/linux-udf/
Source: https://github.com/pali/udftools/releases/download/%{version}/udftools-%{version}.tar.gz
Patch1: udftools-2.3-backported_fixes.patch
BuildRequires: make
BuildRequires: readline-devel, ncurses-devel
BuildRequires: autoconf, automake, libtool, perl-Carp
BuildRequires: udev
Requires: udev

%description
Linux UDF Filesystem userspace utilities.


%prep
%autosetup -p1

%build
#./bootstrap #not in the tarball anymore, lets use pregenerated autotools
##export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing --std=gnu99"
%configure
%make_build
##%%{__make} %%{?_smp_mflags}

%install
%make_install
#./libtool --finish %%{buildroot}%%{_libdir} #causes failure and is probably unneeded, we dont ship a library
rm -rf %{buildroot}%{_bindir}/udffsck


%files
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%{_pkgdocdir}/*
%{_mandir}/man?/*
%{_udevrulesdir}/80-pktsetup.rules


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3-13
- Prepare for Oreon 11 (RP1)
