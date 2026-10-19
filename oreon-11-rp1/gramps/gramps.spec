%global source0_hash f36069c71449b92636883f69addae38e76fa07ec37d9b3fcb5cac0b38390e314
Name:           gramps
Version:        6.0.8
Release:        1%{?dist}
Summary:        Genealogical Research and Analysis Management Programming System
License: GPL-2.0-or-later
URL:            https://gramps-project.org/
Source0:        https://github.com/gramps-project/gramps/archive/v%{version}/gramps-%{version}.tar.gz
BuildArch:	noarch
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-gobject
Requires:       gtk3
Requires:       pango
Requires:       librsvg2
Requires:       xdg-utils
Requires:       rcs
Requires:	graphviz
Requires:	osm-gps-map-gobject
Requires:       python%{python3_pkgversion}-pyicu
Requires:	gtkspell3
Requires:	libgexiv2
Requires:       python%{python3_pkgversion}-bsddb3
Requires:	gnu-free-serif-fonts
Requires:	gnu-free-mono-fonts
Requires:	gnu-free-fonts-common
Requires:	gnu-free-sans-fonts
Requires:	hicolor-icon-theme
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gramps = %{version}-%{release}
# /oreon:deps
%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep

%setup -q

%build

%pyproject_wheel
%install
%pyproject_install
sed -i -e '1s| \+-||2g' ${RPM_BUILD_ROOT}%{_bindir}/gramps
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/locale
cp -pr build/mo/* ${RPM_BUILD_ROOT}%{_datadir}/locale/
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/mime/packages
cp -p build/data/org.gramps_project.Gramps.xml ${RPM_BUILD_ROOT}%{_datadir}/mime/packages/
mkdir -p ${RPM_BUILD_ROOT}%{_metainfodir}/
cp -p build/data/org.gramps_project.Gramps.metainfo.xml ${RPM_BUILD_ROOT}%{_metainfodir}/
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
cp -p build/data/man/gramps.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/gramps.1.gz
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/doc/gramps/
echo -n %{_datadir} > $RPM_BUILD_ROOT%{python3_sitelib}/gramps/gen/utils/resource-path
appstream-util modify $RPM_BUILD_ROOT%{_metainfodir}/org.gramps_project.Gramps.metainfo.xml \
  id org.gramps_project.Gramps
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_metainfodir}/org.gramps_project.Gramps.metainfo.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gramps/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gramps/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gramps/c.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gramps/d.png 
%find_lang %{name}
desktop-file-install --delete-original  \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications   	\
  build/data/org.gramps_project.Gramps.desktop
%oreon_autofiles main

%files

%changelog

%autochangelog
