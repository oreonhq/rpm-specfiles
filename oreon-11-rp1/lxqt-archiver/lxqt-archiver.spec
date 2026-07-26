%global source0_hash 948655705e8e6a9c4c57f2d09b1134b4b23739c8cac0c39b09b04fb15d5375ef

Name:          lxqt-archiver
Summary:       A simple & lightweight desktop-agnostic Qt file archiver
Version:       1.3.0
Release:       3%{?dist}
License:       GPL-2.0-or-later
URL:           https://lxqt.github.io/
Source0:       https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:       %{name}.appdata.xml
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(fm-qt6)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: desktop-file-utils
BuildRequires: json-glib-devel
BuildRequires: libexif-devel
BuildRequires: libappstream-glib
BuildRequires: perl

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-archiver
Requires:       lxqt-archiver
%description l10n
This package provides translations for the lxqt-archiver package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/lxqt/translations/%{name}
mkdir -p %{buildroot}%{_metainfodir}/
cp %{SOURCE1} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name} --with-qt

%files
%doc CHANGELOG AUTHORS README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml
%dir %{_datadir}/%{name}

%files l10n -f %{name}.lang
%doc CHANGELOG AUTHORS README.md
%license LICENSE
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}_arn.qm
%{_datadir}/%{name}/translations/%{name}_ast.qm

%changelog
%autochangelog
