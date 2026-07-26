%global source0_hash ddcb77d5832070ab5f07bbfc15f404b030e67e06f60d1bb3be8ce8af5f413fdd

Name:           khealthcertificate
Version:        25.12.3
Release:        1%{?dist}
License:        W3C-20150513 AND LGPL-2.0-or-later AND BSD-3-Clause AND CC0-1.0 AND MIT AND Apache-2.0
Summary:        Handling of digital vaccination, test and recovery certificates.
Url:            https://invent.kde.org/pim/khealthcertificate
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: gcc-c++
BuildRequires: openssl-devel
BuildRequires: zlib-devel

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%files
%{_kf6_datadir}/qlogging-categories6/org_kde_khealthcertificate.categories
%{_kf6_libdir}/*.so.*
%{_kf6_qmldir}/org/kde/khealthcertificate/

%license LICENSES/*

%package devel
Summary: Development files for khealthcertificate
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%files devel
%{_includedir}/*
%{_kf6_libdir}/cmake/KHealthCertificate
%{_kf6_libdir}/*.so

%changelog
%autochangelog
