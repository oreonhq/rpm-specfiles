%global source0_hash add1433fcaa9861b59426d8db236e51047752b47fd788575ee0fe2dc3af3926e

Name:           gnome-chemistry-utils
Version:        0.14.17
Release:        54%{?dist}
Summary:        A set of chemical utilities

#openbabel/* is GPLv2+
License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            http://www.nongnu.org/gchemutils/
Source0:        http://download.savannah.nongnu.org/releases/gchemutils/0.14/%{name}-%{version}.tar.xz
Patch0:         %{name}-%{version}-gnm11242.patch
Patch1:         %{name}-%{version}-10041.patch
Patch2:         remove-gnome-common.patch
Patch3:         %{name}-%{version}-porting_openbabel3.patch
Patch4:         gdk-use-x11-backend.patch
Patch5:         0001-Use-yelp-instead-of-gnome-doc-utils.patch
Patch6:         %{name}-fix_pointer_types.patch

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  libGLU-devel
BuildRequires:  make
BuildRequires:  man-pages-reader
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(bodr) >= 5
BuildRequires:  pkgconfig(chemical-mime-data) >= 0.1.94
BuildRequires:  pkgconfig(lasem-0.6) >= 0.6.0
BuildRequires:  pkgconfig(libgoffice-0.10) >= 0.10.12
BuildRequires:  pkgconfig(libspreadsheet-1.12) >= 1.11.6
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:  yelp-tools

# https://gitlab.gnome.org/GNOME/goffice/-/issues/70
ExcludeArch:    %{ix86}

Requires:       gchem3d%{?_isa} = %{version}-%{release}
Requires:       gchemcalc%{?_isa} = %{version}-%{release}
Requires:       gchempaint%{?_isa} = %{version}-%{release}
Requires:       gchemtable%{?_isa} = %{version}-%{release}
Requires:       gcrystal%{?_isa} = %{version}-%{release}
Requires:       gspectrum%{?_isa} = %{version}-%{release}

%description
This is a meta-package for applications in the GNOME Chemistry Utils suite:

* A 3D molecular structure viewer (GChem3D).
* A Chemical calculator (GChemCalc).
* A 2D structure editor (GChemPaint).
* A periodic table of the elements application (GChemTable).
* A crystalline structure editor (GCrystal).
* A spectra viewer (GSpectrum).

%package        libs
Summary:        GNOME Chemistry Utils libraries
Requires:       bodr
Requires:       chemical-mime-data

%description    libs
This package contains common libraries for the GNOME Chemistry Utils suite.

%package        gnumeric
Summary:        Gnome Chemistry Utils plugin for Gnumeric
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    gnumeric
This package is a set of chemical utils. Several programs are available:
* A 3D molecular structure viewer (GChem3D).
* A Chemical calculator (GChemCalc).
* A 2D structure editor (GChemPaint).
* A periodic table of the elements application (GChemTable).
* A crystalline structure editor (GCrystal).
* A spectra viewer (GSpectrum).
This package contains a plugin adding a few chemistry-related functions to
gnumeric.

%package -n     gchem3d
Summary:        3D molecular structure viewer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n gchem3d
This package contains GChem3D, a 3D molecular structure viewer that is part of
the GNOME Chemistry Utils.

%package -n     gchemcalc
Summary:        Chemical calculator
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n gchemcalc
This package contains GChemCalc, a chemical calculator that is part of
the GNOME Chemistry Utils.

%package -n     gchempaint
Summary:        2D chemical structure editor
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       gnome-icon-theme

%description -n gchempaint
This package contains GChemPaint, a 2D chemical structure editor that is part of
the GNOME Chemistry Utils.

%package -n     gchemtable
Summary:        Periodic table of the chemical elements
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n gchemtable
This package contains GChemTable, an application for displaying the periodic
table of the chemical elements. It's part of the GNOME Chemistry Utils.

%package -n     gcrystal
Summary:        Crystalline structure editor
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       gnome-icon-theme

%description -n gcrystal
This package contains GCrystal, a crystalline structure editor that is part of
the GNOME Chemistry Utils.

%package -n     gspectrum
Summary:        Spectrum viewer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n gspectrum
This package contains GSpectrum, a spectrum viewer that is part of
the GNOME Chemistry Utils.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mkdir -p m4
autoreconf -ivf -I %{_datadir}/gettext/m4

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-update-databases \
           --disable-scrollkeeper \
           --disable-silent-rules \
           --disable-schemas-compile \
           openbabel_CFLAGS="`pkg-config --cflags openbabel-3`" \
           openbabel_LIBS="`pkg-config --libs openbabel-3`"
%make_build

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install

desktop-file-validate \
       %{buildroot}%{_datadir}/applications/{gchem3d,gchemcalc,gchempaint,gchemtable,gcrystal,gspectrum}-0.14.desktop

# rename so that the desktop ID does not change for each API bump
for app_id in gchem3d gchemcalc gchempaint gchemtable gcrystal gspectrum; do
    echo $app_id
    mv %{buildroot}%{_datadir}/applications/$app_id-0.14.desktop \
       %{buildroot}%{_datadir}/applications/$app_id.desktop
    desktop-file-edit --set-key=Exec --set-value="env LD_LIBRARY_PATH=%{_libdir}/gchemutils $app_id-0.14" \
       %{buildroot}%{_datadir}/applications/$app_id.desktop
done

%find_lang gchemutils-0.14
%find_lang gchem3d-0.14 --with-gnome
%find_lang gchemcalc-0.14 --with-gnome
%find_lang gchempaint-0.14 --with-gnome
%find_lang gchemtable-0.14 --with-gnome
%find_lang gcrystal-0.14 --with-gnome
%find_lang gspectrum-0.14 --with-gnome

# kill libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# kill intrusive docs
rm -rf %{buildroot}%{_docdir}/gchemutils

# Move private libraries into private directory
mv %{buildroot}%{_libdir}/lib*-0.14.so* %{buildroot}%{_libdir}/gchemutils/

# kill KDE MIME .desktop files
rm -rf %{buildroot}%{_datadir}/mimelnk

# validate the .appdata.xml
mkdir -p %{buildroot}%{_metainfodir}
cp -p %{buildroot}%{_datadir}/appdata/*.appdata.xml %{buildroot}%{_metainfodir}/
rm -rf %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING

%files -n gchem3d -f gchem3d-0.14.lang
%{_bindir}/gchem3d-0.14
%{_bindir}/gchem3d
%{_metainfodir}/gchem3d.appdata.xml
%{_datadir}/applications/gchem3d.desktop
%{_datadir}/icons/hicolor/scalable/apps/gchem3d.svg
%{_mandir}/man1/gchem3d.1*

%files -n gchemcalc -f gchemcalc-0.14.lang
%{_bindir}/gchemcalc-0.14
%{_bindir}/gchemcalc
%{_metainfodir}/gchemcalc.appdata.xml
%{_datadir}/applications/gchemcalc.desktop
%{_datadir}/icons/hicolor/scalable/apps/gchemcalc.svg
%{_mandir}/man1/gchemcalc.1*

%files -n gchempaint -f gchempaint-0.14.lang
%{_bindir}/gchempaint-0.14
%{_bindir}/gchempaint
%{_metainfodir}/gchempaint.appdata.xml
%{_datadir}/applications/gchempaint.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.paint.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.paint.plugins.arrows.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/gchempaint.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-gchempaint.svg
%{_mandir}/man1/gchempaint.1*

%files -n gchemtable -f gchemtable-0.14.lang
%{_bindir}/gchemtable-0.14
%{_bindir}/gchemtable
%{_metainfodir}/gchemtable.appdata.xml
%{_datadir}/applications/gchemtable.desktop
%{_datadir}/icons/hicolor/scalable/apps/gchemtable.svg
%{_mandir}/man1/gchemtable.1*

%files -n gcrystal -f gcrystal-0.14.lang
%{_bindir}/gcrystal-0.14
%{_bindir}/gcrystal
%{_metainfodir}/gcrystal.appdata.xml
%{_datadir}/applications/gcrystal.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.crystal.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/gcrystal.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-gcrystal.svg
%{_mandir}/man1/gcrystal.1*

%files -n gspectrum -f gspectrum-0.14.lang
%{_bindir}/gspectrum-0.14
%{_bindir}/gspectrum
%{_metainfodir}/gspectrum.appdata.xml
%{_datadir}/applications/gspectrum.desktop
%{_datadir}/icons/hicolor/scalable/apps/gspectrum.svg
%{_mandir}/man1/gspectrum.1*

%files libs -f gchemutils-0.14.lang
%license COPYING
%{_libdir}/gchemutils/
%{_libdir}/goffice/*/plugins/gchemutils
%{_libexecdir}/babelserver
%{_datadir}/gchemutils/
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.gschema.xml
%{_datadir}/mime/packages/gchemutils.xml

%files gnumeric
%{_libdir}/gnumeric/*/plugins/gchemutils/

%changelog
%autochangelog
