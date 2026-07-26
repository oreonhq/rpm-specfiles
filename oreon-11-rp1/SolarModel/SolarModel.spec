%global source0_hash 8110d0be936627941da5905b6b2a77a4887fa51bca3c129d22f757a344ac7431

Name:		SolarModel
Summary: 	Real-time 3D Solar System simulation
Version:	2.1
Release:	43%{?dist}
License:	GPL-1.0-or-later
Source0:	http://downloads.sourceforge.net/solarmodel/%{name}_src_2_1.zip
# Upstream only has these .dat files in the binary zip file for 2.1
# http://downloads.sourceforge.net/solarmodel/SolarModel_bin_2_1.zip
Source1:	config.dat
Source2:	data.dat
Source3:	SolarModel.desktop
Source4:	SolarModel.png
# Use system locations for libraries, headers
# Use RPM_OPT_FLAGS
# Fix swprintf/Linux related issues
Patch0:		SolarModel-2.1-Fedora.patch
# Compile against irrlicht 1.6
Patch1:		SolarModel-2.1-irrlicht1.6.patch
URL:		http://www.ffsoftworks.com/solarmodel.php
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	irrlicht-devel, libXext-devel, libX11-devel, desktop-file-utils

%description
Solar Model provides realtime modeling of the solar system. It allows the user 
to navigate in space, to control time counting (speed-up time flow) and 
estimate real movement of space bodies like planets, dwarf planets and moons; 
estimate its nowadays positions in space. You may select two possible views: 
Solar System view or Milky Way galaxy view. It also allows the user to bind 
the camera to space objects (for example, you can look from the Moon onto Earth 
in real-time flow). 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}_src
%patch -P0 -p1 -b .Fedora
%patch -P1 -p1 -b .irrlicht1.6

for i in _dev/*.txt "_dev/map/*.txt"; do
	sed -i 's/\r//' $i
done
iconv -o _dev/Changelog.txt.iso88591 -f iso88591 -t utf8 _dev/Changelog.txt
mv _dev/Changelog.txt.iso88591 _dev/Changelog.txt

%build
make %{_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 SolarModel %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}
install	-p -m0644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}
install -p -m0644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE3}

%files
%doc _dev/Changelog.txt _dev/License.txt _dev/Readme.txt _dev/map/* _dev/num/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/SolarModel.png

%changelog
%autochangelog
