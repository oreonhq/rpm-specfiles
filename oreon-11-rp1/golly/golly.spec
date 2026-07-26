%global source0_hash 51d2478063e7ec50cde2b61381f3c1028604e45182e374cff0e14199822a081d

Name:       golly
Version:    4.3
Release:    4%{?dist}
Summary:    Cellular automata simulator (includes Conway's Game of Life)
# The license for the code is GPLv2+ and for the included python parts Python-2.0.1
#    see  /usr/share/licenses/golly/License.html
# The license for the Life Lexicon (in -data subpackage) is CC-BY-SA-3.0
#    see /usr/share/licenses/golly-data/lex.htm from https://conwaylife.com/ref/lexicon/lex_home.htm
License:    GPL-2.0-or-later AND Python-2.0.1
URL:        https://golly.sourceforge.net/
Source0:    https://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
# patch to use system lua library rather than bundled
Patch1:     golly-4.3-lua-dyn.patch
# patch to avoid using deprecated Python modules
Patch2:     golly-4.3-python.patch

BuildRequires:  gcc-c++
BuildRequires:  wxGTK-devel
BuildRequires:  SDL2-devel
BuildRequires:  python3-devel
BuildRequires:  lua-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
Recommends:     golly-data = %{version}-%{release}

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
# remove RPATH
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
# install binaries
install -d %{buildroot}%{_bindir}/
install -m 755 golly bgolly %{buildroot}%{_bindir}/

# install data files, but not scripts used only for build
for d in gui-wx/bitmaps Help Patterns Rules Scripts
do
  find $d -type d -exec install -d %{buildroot}%{_datadir}/%{name}/{} \;
  find $d -type f -exec install -m 644 {} %{buildroot}%{_datadir}/%{name}/{} \;
done
rm %{buildroot}%{_datadir}/%{name}/Help/Lexicon/*.pl

# move docs to top level of build dir to simplify files section
mv docs/* .
rmdir docs

# install application icon and desktop file
install -D -p -m 644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/golly
%{_bindir}/bgolly
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/Rules
%{_datadir}/%{name}/gui-wx
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%license License.html
%doc ReadMe.html

%files data
%{_datadir}/%{name}/Help
%{_datadir}/%{name}/Patterns
%{_datadir}/%{name}/Rules/*
%{_datadir}/%{name}/Scripts
%exclude %{_datadir}/%{name}/Rules/TableGenerators/
%exclude %{_datadir}/%{name}/Rules/TreeGenerators/
%license License.html
%license Help/Lexicon/lex.htm

%files devel
%{_datadir}/%{name}/Rules/TableGenerators/
%{_datadir}/%{name}/Rules/TreeGenerators/

%changelog
%autochangelog
