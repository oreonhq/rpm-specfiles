%global source1_hash e46b8cbec7bf0bd882a16f2d544bb30a84cd6172d91ef16474b6c97357761d52
%global source0_hash b90b42ab222a3034729e517d0c06258abf6bdc28591ec78ad56f24aebbaaed94
%global framework kdoctools
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon for generating documentation
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       docbook-dtds
Requires:       docbook-style-xsl
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  perl(Any::URI::Escape)
BuildRequires:  perl-generators
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-kdoctools-static = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       perl(Any::URI::Escape)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name --with-man --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kdoctools-devel -f %{oreon_filedir}/kf6-kdoctools-devel.list

%changelog

%autochangelog
