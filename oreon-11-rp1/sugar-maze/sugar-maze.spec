%global source0_hash 6bc3b59f4434fa0f8bc73aac9241e9d0e1ea3455317365e67873843544400b31

Name:      sugar-maze
Version:   32
Release:   6%{?dist}
Summary:   Maze game for Sugar
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:   GPL-3.0-or-later
URL:       http://wiki.laptop.org/go/Maze
Source0:   https://download.sugarlabs.org/sources/honey/Maze/Maze-%{version}.tar.bz2
BuildArch: noarch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar

%description
A simple maze game for the XO laptop. You can play by yourself or race
to solve it with your buddies. Up to 3 people can play on a single XO
laptop and lots more can play when shared over the network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Maze-%{version}
# remove olpcgames library
rm -rf olpcgames

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{buildroot}/%{_prefix}
find  %{buildroot}%{sugaractivitydir}Maze.activity/activity.py  -type f -name \* -exec chmod 644 {} \;
mv player.py %{buildroot}%{sugaractivitydir}/Maze.activity/player.py
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Maze.activity/

%find_lang vu.lux.olpc.Maze

%files -f vu.lux.olpc.Maze.lang
%license COPYING
%{sugaractivitydir}/Maze.activity/

%changelog
%autochangelog
