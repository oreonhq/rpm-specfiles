%global source0_hash b1ebf006efd6cecaf08a0daa8445ad16a7a743507400f7c93073ab84aef19e22

Name:          maui-mauikit-texteditor
Version:       4.0.0
Release:       4%{?dist}
License:       BSD-2-Clause AND LGPL-2.1-or-later AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later AND BSD-3-Clause
Summary:       MauiKit Text Editor components
URL:           https://invent.kde.org/maui/mauikit-texteditor/

Source0:       https://download.kde.org/stable/maui/mauikit-texteditor/%{version}/mauikit-texteditor-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Qml)

BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(MauiKit4)

%description
MauiKitTextEditor is a set of QtQuick components providing basic text editing
capabilities.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mauikit-texteditor-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang mauikittexteditor

%files -f mauikittexteditor.lang
%license LICENSES/*
%{_kf6_libdir}/libMauiKitTextEditor4.so.4
%{_kf6_libdir}/libMauiKitTextEditor4.so.%{version}
%{_kf6_qmldir}/org/mauikit/texteditor/

%files devel
%{_kf6_libdir}/cmake/MauiKitTextEditor4/
%{_includedir}/MauiKit4/TextEditor/
%{_kf6_libdir}/libMauiKitTextEditor4.so

%changelog
%autochangelog
