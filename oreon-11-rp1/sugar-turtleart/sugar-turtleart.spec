%global source0_hash 00302988d04b4fa268b7abf6df156c4ad205c8bc1d3cee7a01a3275a182dc69d

Name:    sugar-turtleart
Version: 220
Release: 14%{?dist}
Summary: Turtle Art activity for sugar
License: MIT
URL:     http://sugarlabs.org/go/Activities/Turtle_Art

BuildArch: noarch
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/TurtleArt/TurtleBlocks-%{version}.tar.bz2

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext

Requires: sugar
Requires: sugar-toolkit-gtk3

%description
The Turtle Art activity is an Logo-inspired graphical "turtle" that 
draws colorful  art based on Scratch-like snap-together visual 
programming elements. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TurtleBlocks-%{version}

sed -i 's/python/python3/' setup.py
sed -i 's#/usr/bin/python#/usr/bin/python3#' *.py
sed -i 's#/usr/bin/python#/usr/bin/python3#' collaboration/*py
sed -i 's#env python#env python3#' TurtleArt/*py
sed -i 's#env python#env python3#' turtleblocks

%build
python3 ./setup.py build

%install
mkdir -p %{buildroot}%{sugaractivitydir}
python3 ./setup.py install --prefix=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/TurtleBlocks.activity/

%find_lang org.laptop.TurtleArtActivity

%files -f org.laptop.TurtleArtActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/TurtleBlocks.activity/
%{_datadir}/metainfo/org.laptop.TurtleArtActivity.appdata.xml

%changelog
%autochangelog
