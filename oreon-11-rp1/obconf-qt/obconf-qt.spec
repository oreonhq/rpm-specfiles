%global source0_hash a0aec1ddcedef9db994cb4e90dd78c9b12962febf7dd3b5f7344ae3abb9f591c

Name:           obconf-qt
Version:        0.16.6
Release:        2%{?dist}
Summary:        A configuration editor for the OpenBox window manager

License:        GPL-2.0-only
URL:            https://github.com/lxde/obconf-qt
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:  perl
BuildRequires:  libSM-devel
BuildRequires:  libICE-devel

Requires:       hicolor-icon-theme
Requires:       openbox

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for obconf-qt
Requires:       obconf-qt
%description l10n
This package provides translations for the obconf-qt package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DPULL_TRANSLATIONS=NO
%cmake_build

%install
%cmake_install

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%files l10n -f %{name}.lang
%license COPYING
%doc AUTHORS README.md

%changelog
%autochangelog
