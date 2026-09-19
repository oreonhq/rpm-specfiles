%global source0_hash 81041a3f67b83c090c6741399c18e5063c5d4fee1df482e18ae5831a55750883

Name:           fusion-icon
Version:        0.2.4
Release:        37%{?dist}
Epoch:          1
Summary:        Compiz Fusion panel applet
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch

# https://github.com/compiz-reloaded/fusion-icon/commit/9c598b8
Patch1:         fusion-icon_0001-Fix-typeerror-in-python3.6.patch

BuildRequires:  python3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  desktop-file-utils

Requires:       ccsm
Requires:       gobject-introspection
Requires:       libappindicator-gtk3
Requires:       compizconfig-python
Requires:       python3-gobject
Requires:       python3-qt5
Requires:       xvinfo

Obsoletes: %{name}-gtk < %{epoch}:%{version}-%{release}
%if 0%{?fedora} < 25
Provides:  %{name}-gtk = %{epoch}:%{version}-%{release}
%endif

%description
The Compiz Fusion Icon is a simple panel applet for starting and controlling
Compiz Fusion. Upon launch, it will attempt to start Compiz Fusion
automatically. You may need to select a window decorator, if one does not
appear.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files FusionIcon

mv %{buildroot}%{_datadir}/{metainfo,appdata}/

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/fusion-icon.desktop

%files -f %{pyproject_files}
%license COPYING
%{_bindir}/fusion-icon
%{_datadir}/applications/fusion-icon.desktop
%{_datadir}/appdata/fusion-icon.appdata.xml
%{_datadir}/icons/hicolor/*/apps/fusion-icon.png
%{_datadir}/icons/hicolor/scalable/apps/fusion-icon.svg

%changelog
%autochangelog
