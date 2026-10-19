%global source0_hash 0ce32970cccaaa3e15032781581fe0c9946c388525c5ab52bd59361a66a3f30a
%bcond_with copr
%bcond_with snapshot
%undefine __cmake_in_source_build
%global archive_suffix tar.gz
%global commit 623777f
%global date 20191012
%global extra rc1
%global github_owner raceintospace
%if %{without snapshot} && %{without copr}
%global gittag v%{version}%{?extra}
%global pkgversion %(echo %{gittag} | sed -e 's/^v//' -e 's/-/./g')
%else
%if %{with copr}
%global pkgversion git
%else
%global pkgversion git%{commit}
%endif
%endif
%bcond_with clang
Name:		raceintospace
Version:	2.0.0
Release:        1%{?dist}
Summary:        Race into Space game
License:	GPL-2.0-or-later
URL:		http://www.raceintospace.org/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}%{extra}/%{name}-%{version}%{extra}.%{archive_suffix}
%if %{with clang}
%else
%endif
Requires:	%{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  libappstream-glib
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pandoc
BuildRequires:  physfs-devel
BuildRequires:  protobuf-devel
# /oreon:deps
%description
Relive the 1960s Space Race - be the first country to land a man on the Moon!

Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

%package data
BuildArch:	noarch
Summary:	Race into Space game data
%description data
Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

Contains platform independent game data.

%package doc
BuildArch:	noarch
Summary:	Race into Space game manual
%description doc
Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

Contains game manual

%prep

%if %{with clang}
export CC=clang CXX=clang++
# Clang does not support this option
export CFLAGS=`echo '%optflags' | sed -e 's/ -fstack-clash-protection//'`
export CXXFLAGS="$CFLAGS"
%endif
%autosetup -p1 -n %{name}-%{pkgversion}

%build

%cmake -DBUILD_PHYSFS=OFF -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
pushd doc/manual
pandoc -o manual.html manual.md
popd
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.raceintospace.Raceintospace.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n raceintospace-data -f %{oreon_filedir}/raceintospace-data.list
%files -n raceintospace-doc -f %{oreon_filedir}/raceintospace-doc.list

%changelog

%autochangelog
