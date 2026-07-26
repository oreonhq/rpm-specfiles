%global source0_hash none

# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

Name:		0ad-data
Version:	0.28.0
Release:	2%{?dist}
Summary:	The Data Files for 0 AD
# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:	LicenseRef-Callaway-CC-BY-SA
Url:		http://play0ad.com
Source:		http://releases.wildfiregames.com/0ad-%{version}-unix-data.tar.xz
BuildRequires:	unzip
Requires:	dejavu-sans-fonts
Requires:	dejavu-sans-mono-fonts
BuildArch:	noarch

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

%files
%license LICENSE-art.txt LICENSE-audio.txt
%{_datadir}/0ad

%changelog
%autochangelog
