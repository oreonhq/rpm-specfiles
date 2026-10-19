%global stable_kf6 stable
%global source0_hash 023c9bb69a98ddb897bc15dd0e526f98817f20acb6cf34068a8382d850003b64
%global kf6_version 6.28.0
%if !0%{?bootstrap}
%global tests %[!(0%{?rhel} >= 10)]
%endif
Name:    libkeduvocdocument
Summary:        Library to parse, convert, and manipulate KVTML files
Version: 26.04.3
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/education/libkeduvocdocument/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if 0%{?tests}
%endif
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
Requires:       kdeedu-data >= %{majmin_ver}
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
A Library to parse, convert, and manipulate KVTML files (and older formats
including kvtml1, csv, etc.).

%package devel
Summary:  Development files for %{name}
License:  GPLv2+ and LGPLv2 and BSD
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  -DQT_MAJOR_VERSION=6 \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
echo "%ctest" > ./rpm-check.sh
chmod +x ./rpm-check.sh
xvfb-run -f ${XDG_RUNTIME_DIR:-/tmp}/.%{name}-xvfb.auth -a \
./rpm-check.sh
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libkeduvocdocument-devel -f %{oreon_filedir}/libkeduvocdocument-devel.list

%changelog

%autochangelog
