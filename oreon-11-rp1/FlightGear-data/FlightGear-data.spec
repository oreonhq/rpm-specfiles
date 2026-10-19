%global source0_hash 4687f6b143c173d2a6e0924af2a1ee4ee30aebd5f8d64ca7f1a03656eaedfc5d
Name:           FlightGear-data
Summary:        FlightGear base scenery and data files
Version:        2024.1.4
Release:        1%{?dist}
License:        GPL-2.0-or-later
Source0:        https://mirrors.ibiblio.org/flightgear/ftp/release-2024.1/FlightGear-%{version}-data.txz
URL:            https://gitlab.com/flightgear/fgdata
BuildArch:      noarch
Obsoletes:      fgfs-base < 1.9.0-1
# oreon:deps

# /oreon:deps
%description
This package contains the base scenery for FlightGear and must be
installed

%prep
%global oreon_srcdir fgdata_2024_1
%oreon_prep
%build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/flightgear
cp -alf *  $RPM_BUILD_ROOT%{_datadir}/flightgear
find $RPM_BUILD_ROOT/%{_datadir}/flightgear -name '*#*' -exec rm {} \;
find $RPM_BUILD_ROOT/%{_datadir}/flightgear -type f -exec chmod 644 {} \;
for f in Docs/FGShortRef.css Docs/README.kln89.html Docs/FGShortRef.html \
        Docs/README.submodels Docs/README.yasim Docs/README.xmlparticles
do
        sed -i 's/\r//' $RPM_BUILD_ROOT/%{_datadir}/flightgear/$f
done
for d in Aircraft/c172/Panels/Textures/.xvpics \
        Textures/Runway/.xvpics .gitignore
do
        rm -rf $RPM_BUILD_ROOT/%{_datadir}/flightgear/$d
done
for f in Thanks Docs/README.xmlparticles Aircraft/c172p/Models/Immat/immat.xml
do
        path=$RPM_BUILD_ROOT/%{_datadir}/flightgear/$f
        iconv -f iso-8859-1 -t utf-8 -o ${path}.utf8 $path
        mv -f ${path}.utf8 ${path}
done
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
for f in COPYING AUTHORS NEWS README Thanks Docs
do
        mv $RPM_BUILD_ROOT/%{_datadir}/flightgear/$f \
                $RPM_BUILD_ROOT/%{_docdir}/%{name}
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
