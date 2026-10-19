%global source0_hash 60f84d26f922b65951a81cfb37323040927c5f01101a60f9563573016e0a52b8
%global appname KSeExpr
Name: kseexpr
Version: 6.0.0.0
Release:        1%{?dist}
License: GPL-3.0-or-later
Summary:        The embeddable expression engine fork for Krita
URL: https://invent.kde.org/graphics/%{name}
Source0:        https://invent.kde.org/graphics/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  sed
# /oreon:deps
%description
Fork of Disney Animation's SeExpr expression library, that is used in Krita.

This fork was created as part of the GSoC 2020 project, Dynamic Fill Layers
in Krita using SeExpr, to enable the provision of fixes and translations
needed to embed SeExpr into the Krita painting suite.

This version is not ABI-compatible with projects using upstream SeExpr.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%cmake_kf6 \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_PREGENERATED_FILES:BOOL=OFF
%cmake_build
%install
%cmake_install
%find_lang seexpr2 --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kseexpr-devel -f %{oreon_filedir}/kseexpr-devel.list

%changelog

%autochangelog
