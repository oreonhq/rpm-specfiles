%global source1_hash 0a9f504dced35c5ffcec2e4c25aed0c49b563c0400364f1773f6da397189e9bf
%global source0_hash fc429b093058bec4878306cbbfb3aa0560ff4a3f166c69504036c507fe72afcc
%global framework syntax-highlighting
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:           kf6-%{framework}
Version:        6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Syntax highlighting engine for Kate syntax definitions
License:        MIT AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(xerces-c)
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6 \
    -DBUILD_TESTING:BOOL=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang_kf6 syntaxhighlighting6_qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%files -f %{oreon_filedir}/main.list
%files -n kf6-syntax-highlighting-devel -f %{oreon_filedir}/kf6-syntax-highlighting-devel.list

%changelog

%autochangelog
