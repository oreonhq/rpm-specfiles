%global source0_hash 4399db39573e59218ca8bc03b0adf7d1ebdddb7cf87f6e6f55390ab4fa0edaad

Name:    kidentitymanagement
Version: 26.04.3
Release: 1%{?dist}
Summary: The KIdentityManagement Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(KF6KirigamiAddons)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       kpimtextedit-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libkpimidentities5.po -execdir mv {} libkpimidentities6.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6IdentityManagementQuick.so.*
%{_kf6_libdir}/libKPim6IdentityManagementCore.so.*
%{_kf6_libdir}/libKPim6IdentityManagementWidgets.so.*
%{_kf6_qmldir}/org/kde/kidentitymanagement/


%files devel
%{_datadir}/dbus-1/interfaces/kf6_org.kde.pim.IdentityManager.xml
%{_includedir}/KPim6/KIdentityManagementCore/
%{_includedir}/KPim6/KIdentityManagementQuick/
%{_includedir}/KPim6/KIdentityManagementWidgets/
%{_kf6_libdir}/cmake/KPim6IdentityManagementCore/
%{_kf6_libdir}/cmake/KPim6IdentityManagementQuick/
%{_kf6_libdir}/cmake/KPim6IdentityManagementWidgets/
%{_kf6_libdir}/libKPim6IdentityManagementCore.so
%{_kf6_libdir}/libKPim6IdentityManagementWidgets.so
%{_kf6_libdir}/libKPim6IdentityManagementQuick.so

%files doc

%changelog
%autochangelog

