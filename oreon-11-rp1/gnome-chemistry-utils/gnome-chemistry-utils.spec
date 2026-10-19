%global source0_hash add1433fcaa9861b59426d8db236e51047752b47fd788575ee0fe2dc3af3926e
Name:           gnome-chemistry-utils
Version:        0.15
Release:        1%{?dist}
Summary:        A set of chemical utilities
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
ExcludeArch:    %{ix86}
Requires:       gchem3d%{?_isa} = %{version}-%{release}
Requires:       gchemcalc%{?_isa} = %{version}-%{release}
Requires:       gchempaint%{?_isa} = %{version}-%{release}
Requires:       gchemtable%{?_isa} = %{version}-%{release}
Requires:       gcrystal%{?_isa} = %{version}-%{release}
Requires:       gspectrum%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libGLU-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  man-pages-reader
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(bodr)
BuildRequires:  pkgconfig(chemical-mime-data)
BuildRequires:  pkgconfig(lasem-0.6)
BuildRequires:  pkgconfig(libgoffice-0.10)
BuildRequires:  pkgconfig(libspreadsheet-1.12)
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:  yelp-tools
# /oreon:deps
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
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_docdir}/gchemutils
mv %{buildroot}%{_libdir}/lib*-0.14.so* %{buildroot}%{_libdir}/gchemutils/
rm -rf %{buildroot}%{_datadir}/mimelnk
mkdir -p %{buildroot}%{_metainfodir}
cp -p %{buildroot}%{_datadir}/appdata/*.appdata.xml %{buildroot}%{_metainfodir}/
rm -rf %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%oreon_autofiles gchem3d usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gchemcalc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gchempaint usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gchemtable usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gcrystal usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gspectrum usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-chemistry-utils-libs -f %{oreon_filedir}/gnome-chemistry-utils-libs.list
%files -n gnome-chemistry-utils-gnumeric -f %{oreon_filedir}/gnome-chemistry-utils-gnumeric.list
%files -n gchem3d -f %{oreon_filedir}/gchem3d.list
%files -n gchemcalc -f %{oreon_filedir}/gchemcalc.list
%files -n gchempaint -f %{oreon_filedir}/gchempaint.list
%files -n gchemtable -f %{oreon_filedir}/gchemtable.list
%files -n gcrystal -f %{oreon_filedir}/gcrystal.list
%files -n gspectrum -f %{oreon_filedir}/gspectrum.list

%changelog

%autochangelog
