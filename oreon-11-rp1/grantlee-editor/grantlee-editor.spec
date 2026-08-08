%global source0_hash 1e1f3b086c4701f70ef6d733ec575eb4db386c152582a54e7e6fb3aeb41aeba4

Name:    grantlee-editor
Summary: KMail Theme Editor
Version: 26.04.3
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: perl-generators

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(QGpgmeQt6)

# kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KPim6MessageViewer)
BuildRequires: cmake(KPim6GrantleeTheme)
BuildRequires: cmake(KPim6AkonadiContactWidgets)
BuildRequires: cmake(KPim6IMAP)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

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

%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.contactprintthemeeditor.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.contactthemeeditor.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.headerthemeeditor.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/grantleeditor.*
%{_kf6_bindir}/contactprintthemeeditor
%{_kf6_bindir}/contactthemeeditor
%{_kf6_bindir}/headerthemeeditor
%{_kf6_datadir}/config.kcfg/grantleethemeeditor.kcfg
%{_kf6_datadir}/applications/org.kde.contactprintthemeeditor.desktop
%{_kf6_datadir}/applications/org.kde.contactthemeeditor.desktop
%{_kf6_datadir}/applications/org.kde.headerthemeeditor.desktop

%files libs
%{_kf6_libdir}/libgrantleethemeeditor.so.*


%changelog
%autochangelog

