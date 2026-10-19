%global source0_hash e844b30ae2102c47e0a4fff2f0e0ef05ba0cebb1890aa72276fa12457c39526f
Name:		0ad-data
Version:	0.28.0
Release:        2%{?dist}
Summary:        The Data Files for 0 AD
License:	LicenseRef-Callaway-CC-BY-SA
Url:		http://play0ad.com
Source0:        http://releases.wildfiregames.com/0ad-%{version}-unix-data.tar.xz
Requires:	dejavu-sans-fonts
Requires:	dejavu-sans-mono-fonts
BuildArch:	noarch
# oreon:deps
BuildRequires:  unzip
# /oreon:deps
%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

This package contains the 0ad data files.

%prep

%setup -q -n 0ad-%{version}

%build

pushd binaries/data/mods/public
    mkdir tmp
    pushd tmp
        unzip -x ../public.zip
	cp -a art/LICENSE.txt ../../../../../LICENSE-art.txt
	cp -a audio/LICENSE.txt ../../../../../LICENSE-audio.txt
        rm -fr *
    popd
    rm -fr tmp
popd
%install
%__mkdir_p %{buildroot}%{_datadir}
%__rm -f binaries/data/tools/fontbuilder/fonts/*
%__mv binaries/data %{buildroot}%{_datadir}/0ad
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
