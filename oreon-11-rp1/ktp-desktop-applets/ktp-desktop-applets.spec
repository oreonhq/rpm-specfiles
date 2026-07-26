%global source0_hash 59d8c07ed86bb19eb4ff471c0e98dda730ee273f91808d0a01b0365ded6631eb

%undefine __cmake_in_source_build
Name:    ktp-desktop-applets
Summary: KDE Telepathy desktop applets
Version: 23.04.3
Release: 9%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/network/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-kservice-devel

Obsoletes:      telepathy-kde-presence-applet < 0.3.0
Provides:       telepathy-kde-presence-applet = %{version}-%{release}

# not sure where best to put this other than here -- rex
Obsoletes:      telepathy-kde-presence-dataengine < 0.3.0
Provides:       telepathy-kde-presence-dataengine = %{version}-%{release}

Obsoletes:      ktp-contact-applet < 0.5.80
Obsoletes:      ktp-presence-applet < 0.5.80
Provides:       ktp-contact-applet = %{version}-%{release}
Provides:       ktp-presence-applet = %{version}-%{release}

# translations moved here
Conflicts: kde-l10n < 17.03

%description
KDE Telepathy desktop applets, including:
* contacts
* presence

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license COPYING*
%{_kf5_datadir}/plasma/plasmoids/org.kde.person/
%{_kf5_datadir}/plasma/plasmoids/org.kde.ktp-chat/
%{_kf5_datadir}/plasma/plasmoids/org.kde.ktp-contactlist/
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_qmldir}/org/kde/ktpchat/
%{_kf5_qmldir}/org/kde/ktpcontactlist/

%changelog
%autochangelog
