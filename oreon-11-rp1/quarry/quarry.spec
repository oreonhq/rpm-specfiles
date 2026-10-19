%global source0_hash f40559291ce107ed54f3d0f442aecf28ac6daa3ebeb38220c3a4177ed1deecda
Name:           quarry
Version:        0.2.0
Release:        1%{?dist}
Summary:        A multi-purpose board game GUI
License:        GPL-2.0-or-later
URL:            http://home.gna.org/quarry/
Source0:        http://download.gna.org/quarry/quarry-%{version}.tar.gz
Patch0:         quarry-format-security.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  librsvg2-devel
BuildRequires:  make
BuildRequires:  scrollkeeper
# /oreon:deps
%description
Quarry is a multi-purpose GUI for several board games, at present Go, Amazons
and Reversi. It allows users to play against computer players (third-party
programs, e.g. GNU Go or GRhino) or other humans, view and edit game records.
Future versions will also support Internet game servers and provide certain
features for developers of board game-playing engines for enhancing their
programs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

export CFLAGS="%{optflags} -std=gnu89"
%configure --disable-scrollkeeper-update
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --remove-key Version \
    --delete-original \
    $RPM_BUILD_ROOT%{_datadir}/applications/quarry.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
