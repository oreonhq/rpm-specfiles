%global source0_hash 36a0a60e422907b2baead8b82cec56008240b7a950678294bb2e1df65e1a6bb3
%global framework kdoctools
%if !0%{?bootstrap}
%global tests 1
%endif
Name:    kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon for generating documentation
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
%global perl_uri_escape perl(URI::Escape)
Requires:       docbook-dtds
Requires:       docbook-style-xsl
# oreon:deps
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  perl(URI::Escape)
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf5-kdoctools-static = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       %{perl_uri_escape}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf5 \
    %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-man %{?_with_html}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test -C %{_target_platform} ARGS="--output-on-failure --timeout 300" ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n kf5-kdoctools-devel -f %{oreon_filedir}/kf5-kdoctools-devel.list

%changelog

%autochangelog
