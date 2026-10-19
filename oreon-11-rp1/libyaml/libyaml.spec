%global source0_hash c642ae9b75fee120b2d96c712538bd2cf283228d2337df2cf2988e3c02678ef4
%global with_mingw 0
Name:       libyaml
Version:    0.2.5
Release:        1%{?dist}
Summary:        YAML 1.1 parser and emitter written in C
License:    MIT
URL:        https://github.com/yaml/libyaml
Source0:        https://github.com/yaml/libyaml/releases/download/%{version}/yaml-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  LibYAML is a YAML parser and
emitter written in C.

%package devel
Summary:   Development files for LibYAML applications
Requires:  libyaml%{?_isa} = %{version}-%{release}, pkgconfig
License:   GPL-2.0-or-later AND MIT
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use LibYAML.

%package -n mingw32-libyaml
Summary: MinGW YAML 1.1 parser and emitter written in C
BuildArch: noarch
%description -n mingw32-libyaml
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  LibYAML is a YAML parser and
emitter written in C.

%package -n mingw64-libyaml
Summary: MinGW YAML 1.1 parser and emitter written in C
BuildArch: noarch
%description -n mingw64-libyaml
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  LibYAML is a YAML parser and
emitter written in C.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n yaml-%{version}

%build

%define _configure ../configure
mkdir build
pushd build
%configure
%make_build all html
popd
%mingw_configure
%mingw_make_build
%install
pushd build
%make_install
popd
%mingw_make_install
rm -f %{buildroot}%{_libdir}/*.{la,a}
soname=$(readelf -d %{buildroot}%{_libdir}/libyaml.so | awk '$2 == "(SONAME)" {print $NF}' | tr -d '[]')
rm -f %{buildroot}%{_libdir}/libyaml.so
echo "INPUT($soname)" > %{buildroot}%{_libdir}/libyaml.so
%oreon_autofiles mingw32-libyaml usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libyaml usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd build
make check
popd
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libyaml-devel -f %{oreon_filedir}/libyaml-devel.list
%files -n mingw32-libyaml -f %{oreon_filedir}/mingw32-libyaml.list
%files -n mingw64-libyaml -f %{oreon_filedir}/mingw64-libyaml.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.5-18
- Import
