%global source0_hash bf9b793b6fab81e59fb9a373944a5724af279b0faebb2461bb98beb5aa466058
Name:           trackballs-music
Version:        1.4
Release:        1%{?dist}
Summary:        In-game music for Trackballs
License:        GPL-2.0-or-later AND LicenseRef-EFML
URL:            http://sourceforge.net/projects/trackballs
Source0:        http://downloads.sourceforge.net/trackballs/%{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       trackballs >= 1.1.2
# oreon:deps

# /oreon:deps
%description
Some great music to listen to while playing Trackballs.

%prep

%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/trackballs/music
install -p -m 644 *.ogg $RPM_BUILD_ROOT%{_datadir}/trackballs/music
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
