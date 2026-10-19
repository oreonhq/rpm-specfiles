%global source0_hash 513cc1682d868e41ba938f0beab14b21d0a056caf7ebe2d9ef1e0830d484c467
Name:       icebreaker
Version:    2.2.2
Release:        1%{?dist}
Summary:        An addictive action-puzzle game involving bouncing penguins
License:    GPL-2.0-or-later
Source0:        https://mattdm.org/icebreaker/2.2.x/icebreaker-%{version}.tar.xz
URL:        http://www.mattdm.org/icebreaker/
Patch:      icebreaker-2.2.2-rename-flock-to-pg_flock.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
IceBreaker is an action-puzzle game in which you must capture penguins from
an Antarctic iceberg so they can be shipped to Finland, where they are
essential to a secret plot for world domination. To earn the highest Geek
Cred, trap them in the smallest space in the shortest time while losing the
fewest lives. IceBreaker was inspired by (but is far from an exact clone of)
Jezzball by Dima Pavlovsky.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build prefix=%{_prefix}
%install
%make_install prefix=%{buildroot}%{_prefix}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications icebreaker.desktop
mkdir %{buildroot}%{_datadir}/metainfo
cp -p metainfo.xml %{buildroot}%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
