%global source0_hash e4cbbe3698bb812b395770870174be0094bbaeb391105a811f95f42eb182ae02
Name:           arandr
Version:        0.1.11
Release:        1%{?dist}
Summary:        Simple GTK+ XRandR GUI
License:        GPL-3.0-only
URL:            https://christian.amsuess.com/tools/arandr/
Source0:        https://christian.amsuess.com/tools/arandr/files/%{name}-%{version}.tar.gz
Patch0:         0001-Make-ARandR-appear-in-XFCE-Settings-Manager.patch
BuildArch:      noarch
Requires:       python3
Requires:       python3-gobject
Requires:       xrandr
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
# /oreon:deps
%description
ARandR is designed to provide a simple visual front end for XRandR 1.2/1.3.
Relative monitor positions are shown graphically and can be changed in a
drag-and-drop way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
%install
%py3_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/arandr.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
