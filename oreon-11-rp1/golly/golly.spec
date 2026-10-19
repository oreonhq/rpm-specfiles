%global source0_hash 5835cde428153f9b840ba94a4359e5cb26eb302e7ac01a097cd7f5a5c8303611
Name:       golly
Version:    5.0
Release:        1%{?dist}
Summary:        Cellular automata simulator (includes Conway's Game of Life)
License:    GPL-2.0-or-later AND Python-2.0.1
URL:        https://golly.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
Patch1:     golly-4.3-lua-dyn.patch
Patch2:     golly-4.3-python.patch
Recommends:     golly-data = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL2-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lua-devel
BuildRequires:  python3-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
Golly is an open source application for exploring Conway's Game of
Life and other cellular automata.  Golly supports unbounded universes
with up to 256 states.  Golly supports multiple algorithms, including
Bill Gosper's super fast hashlife algorithm.  Many different types of
CA are included: John von Neumann's 29-state CA, Wolfram's 1D rules,
WireWorld, Generations, Langton's Loops, Paterson's Worms, etc.

%package data
Summary:    Data for %{name}
License:    GPL-2.0-or-later AND Python-2.0.1 AND CC-BY-SA-3.0
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch
%description data
This package contains data for %{name}: Help, rules, patterns and scripts.

%package devel
Summary:    Development files for Golly cellular automata simulator
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch
%description devel
Development files for Golly celluar automata simulator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-src -p 1
# fix permissions - no normal files should have execute permissions set
find . -type f -exec chmod 644 {} \;
# remove bundled lua
rm -rf lua

%build

pushd gui-wx
export GOLLYDIR=%{_datadir}/%{name}
%make_build -f makefile-gtk
popd
chrpath --delete golly bgolly
convert gui-wx/icons/appicon48.ico golly.png
cat <<EOF >golly.desktop
[Desktop Entry]
Name=Golly
GenericName=Golly cellular automata simulator
Exec=golly
Icon=golly
Terminal=false
Type=Application
Categories=GNOME;Game;LogicGame;
EOF
%install
install -d %{buildroot}%{_bindir}/
install -m 755 golly bgolly %{buildroot}%{_bindir}/
for d in gui-wx/bitmaps Help Patterns Rules Scripts
do
  find $d -type d -exec install -d %{buildroot}%{_datadir}/%{name}/{} \;
  find $d -type f -exec install -m 644 {} %{buildroot}%{_datadir}/%{name}/{} \;
done
rm %{buildroot}%{_datadir}/%{name}/Help/Lexicon/*.pl
mv docs/* .
rmdir docs
install -D -p -m 644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n golly-data -f %{oreon_filedir}/golly-data.list
%files -n golly-devel -f %{oreon_filedir}/golly-devel.list

%changelog

%autochangelog
