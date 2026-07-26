%global source0_hash 92a680125c75bb9d419d36335bdce78510ff74d3b892b3573729a19cae18752d

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests %[!(0%{?rhel} >= 10)]
%endif

Name:    libkeduvocdocument
Summary: Library to parse, convert, and manipulate KVTML files
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/education/libkeduvocdocument/
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches
# master branch

BuildRequires: make
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6KIO)

%if 0%{?tests}
BuildRequires: xorg-x11-server-Xvfb
%endif

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
Requires:       kdeedu-data >= %{majmin_ver}

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

%autosetup -p1

%build
%cmake_kf6 \
  -DQT_MAJOR_VERSION=6 \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
# FIXME/TODO: make macros better to not have to do this when using xvfb-run
echo "%ctest" > ./rpm-check.sh
chmod +x ./rpm-check.sh
xvfb-run -a \
./rpm-check.sh
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS README 
%license LICENSES/*
%{_kf6_libdir}/libKEduVocDocument.so.5*

%files devel
%{_includedir}/libkeduvocdocument/
%{_kf6_libdir}/libKEduVocDocument.so
%license COPYING-CMAKE-SCRIPTS 
%{_kf6_libdir}/cmake/libkeduvocdocument/

%changelog
%autochangelog
