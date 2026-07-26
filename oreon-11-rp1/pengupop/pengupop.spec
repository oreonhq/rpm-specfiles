%global source0_hash 4657ba8d17bd9e9d3eadb374d5f54efddee35d0abdcf780aa8103e60cea932cb

Name:           pengupop
Version:        2.2.2
Release:        41%{?dist}
Summary:        Networked Game in the vein of Move/Puzzle Bobble

License:        GPL-2.0-or-later
URL:            http://www.junoplay.com/pengupop
Source0:        http://www.junoplay.com/files/%{name}-%{version}.tar.gz
Patch0: pengupop-c99.patch
Patch1: includes.patch

# Because unistd
ExcludeArch: s390x

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel, zlib-devel, desktop-file-utils

%description
Finally a networked multiplayer game in the vein of the puzzle classic Bust a
Move/Puzzle Bobble. Beat your friends in this addictive game, or play against
a random opponent! The purpose of this game is to shoot colored orbs into your
playfield, so they form groups of three or more. You win if you manage to
remove all orbs. You lose if any orb attaches below the white line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%undefine _fortify_level
%configure
make %{?_smp_mflags} LIBS="-lm"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
cp pengupop.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
        pengupop.desktop

%files
%doc AUTHORS COPYING
%{_bindir}/pengupop
%{_datadir}/applications/pengupop.desktop
%{_datadir}/icons/hicolor/48x48/apps/pengupop.png

%changelog
%autochangelog
