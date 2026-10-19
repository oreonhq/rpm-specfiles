%global source0_hash 57ccc689cbf4b39c0da3a42daa5374f14a5b5a957fe20768dd4529b8965dd380
Summary:        Turn based role-playing game builder and engine
Name: btbuilder
Version: 0.5.20
Release:        1%{?dist}
License: GPL-3.0-or-later
Url: http://www.identicalsoftware.com/btbuilder
Source0:        http://www.identicalsoftware.com/btbuilder/%{name}-%{version}.tgz
Patch0: btbuilder-boost190.patch
Requires:       %{name}-data = %{version}
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  SDL_mng-devel
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  physfs-devel
# /oreon:deps
%description
Bt Builder is a turn based role-playing game builder and engine in the style
of the old Bard's Tale series. It completely supports the functionality of the
Bard's Tale Construction Set. The eventual goal is to make a game builder that
can implement the three main Bard's Tale games in addition to Construction Set
games.

%package	data
Summary:	%{summary}
Requires:	%{name} = %{version}
BuildArch:      noarch
%description	data
This package contains the data files for Bt Builder.

%prep

%setup -q
%patch 0 -p1

%build

%make_build CFLAGS="%{optflags}"
%install
make prefix=%{buildroot} install
%oreon_autofiles btbuilder-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n btbuilder-data -f %{oreon_filedir}/btbuilder-data.list

%changelog

%autochangelog
