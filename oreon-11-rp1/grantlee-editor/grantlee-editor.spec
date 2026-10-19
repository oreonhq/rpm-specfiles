%global stable_kf6 stable
%global source0_hash 1e1f3b086c4701f70ef6d733ec575eb4db386c152582a54e7e6fb3aeb41aeba4
Name:    grantlee-editor
Summary:        KMail Theme Editor
Version: 26.04.3
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}
Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6MessageViewer)
BuildRequires:  cmake(KPim6PimCommon)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  perl-generators
# /oreon:deps
%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Conflicts: kdepim-libs < 7:16.12
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.contactprintthemeeditor.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.contactthemeeditor.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.headerthemeeditor.desktop
%files -f %{oreon_filedir}/main.list
%files -n grantlee-editor-libs -f %{oreon_filedir}/grantlee-editor-libs.list

%changelog

%autochangelog

