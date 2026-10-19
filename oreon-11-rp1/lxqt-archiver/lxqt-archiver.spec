%global source0_hash 948655705e8e6a9c4c57f2d09b1134b4b23739c8cac0c39b09b04fb15d5375ef
Name:          lxqt-archiver
Summary:        A simple & lightweight desktop-agnostic Qt file archiver
Version:       1.3.0
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           https://lxqt.github.io/
Source0:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:       %{name}.appdata.xml
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(fm-qt6)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  json-glib-devel
BuildRequires:  libappstream-glib
BuildRequires:  libexif-devel
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt)
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-archiver-l10n -f %{oreon_filedir}/lxqt-archiver-l10n.list

%changelog

%autochangelog
