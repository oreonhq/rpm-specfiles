%global source0_hash 96554481089a9061cffeb68cad15a766c4189604ab9b70c5155cdf8bd89043e0

Name:           inertiablast
Version:        0.93
Release:        12%{?dist}
Summary:        Steal energy pods to defeat the empire
# Almost all is GPLv2+ with some graphics using the other licenses
# Automatically converted from old format: GPLv2+ and CC0 and CC-BY and (CC-BY or GPLv3) - review is highly recommended.
License:        GPL-2.0-or-later AND CC0-1.0 AND LicenseRef-Callaway-CC-BY AND (LicenseRef-Callaway-CC-BY OR GPL-3.0-only)
URL:            http://identicalsoftware.com/inertiablast/

Source0:        %{url}/%{name}-%{version}.tgz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libgamerzilla-devel
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: SDL2-devel
BuildRequires: SDL2_mixer-devel
Requires:      hicolor-icon-theme

%description
The rebellion captured several warships but lack the energy pod to
power the ships. You are part of a risky expedition to steal the energy
pods. Defense systems will attempt to stop you. The energy pods are
often stored in tunnels making them hard to retrieve. The massive weight
of the pod increases the difficultly in getting out.

Inertia Blast is a remake of an C64 game called Thrust.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
\

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/man/man6/%{name}.6*

%changelog
%autochangelog
