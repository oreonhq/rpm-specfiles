%global source0_hash 5b46e74377ed7409c5b75e7a96f95377b095623b689d8522620927964a41499c
Version:	1.4.2
Release:        1%{?dist}
Name: libunistring
Summary:        GNU Unicode string library
License: GPL-2.0-or-later OR LGPL-3.0-or-later
URL: https://www.gnu.org/software/libunistring/
Provides: bundled(gnulib)
Source0:        https://mirrors.kernel.org/gnu/libunistring/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --disable-rpath
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} __doc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libunistring-devel -f %{oreon_filedir}/libunistring-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-1
- Import
