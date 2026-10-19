%global source0_hash 4aeb97aea2b58224029dc2b23d7d064cfa990cb4fb8c4da440bcbe9c95bc5d2d
Name:		orc
Version:	0.4.44
Release:        1%{?dist}
Summary:        The Oil Run-time Compiler
License:	BSD-2-Clause AND BSD-3-Clause
URL:		http://cgit.freedesktop.org/gstreamer/orc/
Source0:        http://gstreamer.freedesktop.org/src/orc/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  python3-hotdoc
# /oreon:deps
%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package doc
Summary:	Documentation for Orc
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for Orc.

%package devel
Summary:	Development files and libraries for Orc
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-compiler
Requires:	pkgconfig
%description devel
This package contains the files needed to build packages that depend
on orc.

%package compiler
Summary:	Orc compiler
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
%description compiler
The Orc compiler, to produce optimized code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -D default_library=shared -D hotdoc=enabled
%meson_build
%install
%meson_install
find %{buildroot}/%{_libdir} -name \*.a -delete
rm -rf %{buildroot}/%{_libdir}/orc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n orc-doc -f %{oreon_filedir}/orc-doc.list
%files -n orc-devel -f %{oreon_filedir}/orc-devel.list
%files -n orc-compiler -f %{oreon_filedir}/orc-compiler.list

%changelog

%autochangelog
