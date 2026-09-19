%global source0_hash none

Name:           trackballs-music
Version:        1.4
Release:        30%{?dist}
Summary:        In-game music for Trackballs
# Automatically converted from old format: GPLv2+ and EFML - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-EFML
URL:            http://sourceforge.net/projects/trackballs
Source0:        http://downloads.sourceforge.net/trackballs/%{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       trackballs >= 1.1.2

%description
Some great music to listen to while playing Trackballs.

%prep
%setup -q -n %{name}

%build
# Nothing to build, music only

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/trackballs/music
install -p -m 644 *.ogg $RPM_BUILD_ROOT%{_datadir}/trackballs/music

%files
%doc GPL.txt README fml.html
%{_datadir}/trackballs/music/*

%changelog
%autochangelog
