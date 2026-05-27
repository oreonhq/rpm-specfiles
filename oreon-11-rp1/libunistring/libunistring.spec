%global source0_hash none

# This spec file has been automatically updated
Version:	1.1
Release: %{?autorelease}%{!?autorelease:1%{?dist}}
Name: libunistring
Summary: GNU Unicode string library
License: GPL-2.0-or-later OR LGPL-3.0-or-later
URL: https://www.gnu.org/software/libunistring/
Source0: https://ftp.gnu.org/gnu/libunistring/%{name}-%{version}.tar.xz
BuildRequires: gcc
BuildRequires: make
Provides: bundled(gnulib)

%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package devel
Summary: GNU Unicode string library - development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for programs using libunistring.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%configure --disable-static --disable-rpath
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la
# Move staged docs so not picked up by %%doc in main package
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} __doc

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/%{name}.so.5*

%files devel
%doc HACKING DEPENDENCIES THANKS ChangeLog
%doc __doc/*
%{_infodir}/%{name}.info*
%{_libdir}/%{name}.so
%{_includedir}/unistring
%{_includedir}/*.h

%ldconfig_scriptlets

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-1
- Import
