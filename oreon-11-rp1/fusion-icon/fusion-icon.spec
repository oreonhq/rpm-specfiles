%global source0_hash 81041a3f67b83c090c6741399c18e5063c5d4fee1df482e18ae5831a55750883
Name:           fusion-icon
Version:        0.2.4
Release:        1%{?dist}
Epoch:          1
Summary:        Compiz Fusion panel applet
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch
Patch1:         fusion-icon_0001-Fix-typeerror-in-python3.6.patch
Requires:       ccsm
Requires:       gobject-introspection
Requires:       libappindicator-gtk3
Requires:       compizconfig-python
Requires:       python3-gobject
Requires:       python3-qt5
Requires:       xvinfo
Obsoletes: %{name}-gtk < %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fusion-icon = %{version}-%{release}
# /oreon:deps
%description
The Compiz Fusion Icon is a simple panel applet for starting and controlling
Compiz Fusion. Upon launch, it will attempt to start Compiz Fusion
automatically. You may need to select a window decorator, if one does not
appear.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mv %{buildroot}%{_datadir}/{metainfo,appdata}/
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/fusion-icon.desktop
%files

%changelog

%autochangelog
