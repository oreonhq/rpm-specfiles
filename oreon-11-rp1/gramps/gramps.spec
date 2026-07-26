%global source0_hash none

Name:           gramps
Version:        6.0.6
Release:        2%{?dist}
Summary:        Genealogical Research and Analysis Management Programming System

License: GPL-2.0-or-later
URL:            https://gramps-project.org/
Source0:        https://github.com/gramps-project/gramps/archive/v%{version}/gramps-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:	perl(XML::Parser)
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-gobject
BuildRequires:  intltool
BuildRequires:  libappstream-glib

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

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# the script starts with -O, the macros add -sP.  execve(2) treats everything
# after the interpreter as a single argument, so the flags need to be combined
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

# fix the app id to match flathub
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

%files -f %{name}.lang
%license COPYING
%doc AUTHORS COPYING FAQ NEWS TODO example/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.gramps_project.Gramps.desktop
%{_datadir}/mime/packages/org.gramps_project.Gramps.xml
%{_datadir}/icons/hicolor/*/apps/org.gramps_project.Gramps.*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/cs/man1/gramps.1.gz
%{_mandir}/fr/man1/gramps.1.gz
%{_mandir}/nl/man1/gramps.1.gz
%{_mandir}/pl/man1/gramps.1.gz
%{_mandir}/pt_BR/man1/gramps.1.gz
%{_mandir}/sv/man1/gramps.1.gz
%{_metainfodir}/org.gramps_project.Gramps.metainfo.xml
%{python3_sitelib}/gramps*dist-info
%{python3_sitelib}/gramps/__init*
%{python3_sitelib}/gramps/__main*
%{python3_sitelib}/gramps/grampsapp*
%{python3_sitelib}/gramps/gui
%{python3_sitelib}/gramps/test
%{python3_sitelib}/gramps/version*
%{python3_sitelib}/gramps/__pycache__
%dir %{python3_sitelib}/gramps/
%{python3_sitelib}/gramps/cli
%{python3_sitelib}/gramps/gen
%{python3_sitelib}/gramps/plugins

%changelog
%autochangelog
