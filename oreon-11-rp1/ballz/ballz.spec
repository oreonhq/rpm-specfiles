%global source0_hash cf63c6ed69f1da818fdc221df012035bb88845226b067cb142941738c2a15452

Name:           ballz
Version:        1.0.4
Release:        19%{?dist}
Summary:        B.A.L.L.Z. - platform/puzzle game where you control a rolling ball
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://gitlab.com/groups/ballz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  allegro-devel dumb-devel guichan-devel intltool
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_desktop_files
BuildRequires:  desktop-file-utils
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AppData/
BuildRequires:  libappstream-glib
BuildRequires: make

%description
The game is a platformer with some puzzle elements. You take control
of a ball which is genetically modified by the British secret
service. Your mission is to rescue captured British soldiers from a
prison in Iran.

The game was written in 72 hours for the TINS competition, a
competition similar to Speedhack. The name TINS is an recursive
acronym for 'TINS is not Speedhack'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS README BSD-license ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_mandir}/man6/*

%changelog
%autochangelog
