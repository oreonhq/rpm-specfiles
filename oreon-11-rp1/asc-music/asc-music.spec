%global source0_hash a36b4e0a1fcc3a34d40c6323e2259057f3b2a9fc14d4c0bb8b3949389dda8424

Name:           asc-music
Version:        1.0
Release:        34%{?dist}
Summary:        Background music for the game asc
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.asc-hq.org/
# transcoded from: http://downloads.sourceforge.net/asc-hq/*.mp3
Source0:        %{name}-%{version}.tar.gz
Buildarch:      noarch
Requires:       asc

%description
Music created by Michael Kievernagel for the game Advanced Strategic Command
(asc).

Note that if you have run asc before installing the music you must remove the
asc cache file: $HOME/.asc/asc.cache, otherwise asc will not find the music.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# nothing todo content only

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/asc/music
install -p -m 644 *.ogg $RPM_BUILD_ROOT%{_datadir}/asc/music

%files
%doc README.fedora
%{_datadir}/asc/music

%changelog
%autochangelog
