%global source0_hash f3b4448904f1656d6d7cd5a557d22fe1c50624eb32ed369f34726beff9ce0589
Name:          ktextaddons
Version:       2.1.2
Release:        1%{?dist}
Summary:        Various text handling addons
License:       CC0-1.0 AND LGPL-2.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:           https://invent.kde.org/libraries/%{name}
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package        qt6
Summary:        Qt6 libraries for %{name}
Requires:       %{name}-common = %{version}-%{release}
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}
%description    qt6-devel
%{summary}.

%package        qt6-doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    qt6-doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        common
Summary:        Translations and documents for %{name}
Obsoletes:      ktextaddons-docs < 1.5.3-1
BuildArch:      noarch
%description    common
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ktextaddons-qt6 -f %{oreon_filedir}/ktextaddons-qt6.list
%files -n ktextaddons-qt6-devel -f %{oreon_filedir}/ktextaddons-qt6-devel.list
%files -n ktextaddons-qt6-doc -f %{oreon_filedir}/ktextaddons-qt6-doc.list
%files -n ktextaddons-common -f %{oreon_filedir}/ktextaddons-common.list

%changelog

%autochangelog
