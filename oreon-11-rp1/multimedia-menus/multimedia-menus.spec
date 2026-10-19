%global source0_hash d9a8ccf9883c6f512fbf7b1303d00e914522f598b74a7cf52e805283345973f7
Name:           multimedia-menus
Version:        0.4.3
Release:        1%{?dist}
Summary:        Categorization for the GNOME/KDE/MATE Sound&Video/Multimedia menu
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND GPL-1.0-or-later AND LicenseRef-Callaway-LGPLv2 AND LGPL-3.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:            https://pagure.io/multimedia-menus
Source0:        https://pagure.io/multimedia-menus/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       redhat-menus hicolor-icon-theme dconf
# oreon:deps
BuildRequires:  intltool
BuildRequires:  make
# /oreon:deps
%description
Categorized sub-menus for the GNOME/KDE/MATE Audio&Video/Multimedia menu, for
better usability and easy access of multimedia applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make %{_smp_mflags}
%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/desktop-directories/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dconf/db/site.d/
cp -a multimedia-menus.dconf $RPM_BUILD_ROOT%{_sysconfdir}/dconf/db/site.d/00_multimedia-menus
install -p -m 644 multimedia-categories.menu \
  $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged/
cp -a desktop-directories/*.directory \
  $RPM_BUILD_ROOT%{_datadir}/desktop-directories/
cp -ar icons/* $RPM_BUILD_ROOT%{_datadir}/icons/
%oreon_autofiles main

%post

dconf update
%postun

dconf update
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
