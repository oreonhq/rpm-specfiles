%global source0_hash none

Name:           lazarus
Summary:        Lazarus Component Library and IDE for Free Pascal

Version:        4.6

%global baserelease 1
Release:        %{baserelease}%{?dist}

# The qt5pas version is taken from lcl/interfaces/qt5/cbindings/Qt5Pas.pro
%global qt5pas_version 2.16
%global qt5pas_release %(relstr="%{version}.%{baserelease}"; relstr=(${relstr//./ }); ((relno=${relstr[0]}*10000 + ${relstr[1]}*100 + ${relstr[2]})); echo "${relno}%{?dist}";)

# The qt6pas version is taken from lcl/interfaces/qt6/cbindings/Qt6Pas.pro
%global qt6pas_version 6.2.10
%global qt6pas_release %{qt5pas_release}

# The IDE itself is licensed under GPLv2+, with minor parts under a modified LGPL.
# The Lazarus Component Library has parts licensed under all the licenses mentioned in the tag.
%global license_doc   GPL-2.0-or-later
%global license_tools GPL-2.0-or-later
%global license_ide   GPL-2.0-or-later AND LGPL-2.0-only WITH Independent-modules-exception
%global license_lcl   GPL-2.0-or-later AND LGPL-2.0-only WITH Independent-modules-exception AND MPL-1.1 AND Apache-2.0
License:        %{license_lcl}

URL:            http://www.lazarus-ide.org/
Source0:        https://downloads.sourceforge.net/project/%{name}/Lazarus%20Zip%20_%20GZip/Lazarus%20%{version}/%{name}-%{version}-0.tar.gz

Source100:      lazarus.appdata.xml

# Lazarus wants to put arch-specific stuff in /usr/share - make it go in /usr/lib istead
Patch0:         0000-Makefile_patch.diff

# -- Build-time dependencies

BuildRequires:  binutils
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  fpc-src
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gtk2-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt6-qtbase-devel

# -- Run-time dependencies.
# Since "lazarus" is a metapackage, it puts strong requirements on the
# default set of sub-packages. Users not interested in the default set
# can omit the metapackage and install individual sub-packages
# as they see fit.

Requires:	%{name}-ide%{?_isa} = %{version}-%{release}
Requires:	%{name}-lcl%{?_isa} = %{version}-%{release}
Requires:	%{name}-lcl-nogui%{?_isa} = %{version}-%{release}
Requires:	%{name}-lcl-gtk2%{?_isa} = %{version}-%{release}
Requires:	%{name}-tools%{?_isa} = %{version}-%{release}

ExclusiveArch:  %{fpc_arches}

%description
Lazarus is an IDE to create (graphical and console) applications with
Free Pascal, the (L)GPLed Pascal and Object Pascal compiler that runs on
Windows, Linux, Mac OS X, FreeBSD and more.

Lazarus is the missing part of the puzzle that will allow you to develop
programs for all of the above platforms in a Delphi-like environment.
The IDE is a RAD tool that includes a form designer.

Unlike Java's "write once, run anywhere" motto, Lazarus and Free Pascal
strive for "write once, compile anywhere". Since the exact same compiler
is available on all of the above platforms you don't need to do any recoding
to produce identical products for different platforms.

In short, Lazarus is a free RAD tool for Free Pascal using its
Lazarus Component Library (LCL).

%package ide
Summary: Lazarus RAD IDE for Free Pascal
License: %{license_ide}

Requires:	%{name}-lcl%{?_isa} = %{version}-%{release}
Requires:	%{name}-tools%{?_isa} = %{version}-%{release}
Recommends:	%{name}-doc = %{version}-%{release}
Recommends:	%{name}-lcl-nogui%{?_isa} = %{version}-%{release}
Recommends:	%{name}-lcl-gtk2%{?_isa} = %{version}-%{release}

Requires: fpc-src
Requires: gdb
Requires: hicolor-icon-theme
Requires: make

%description ide
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package provides the Lazarus RAD IDE.

%package tools
Summary: Lazarus IDE helper programs
License: %{license_tools}
Requires: binutils
Requires: fpc%{?_isa}
Requires: glibc-devel%{?_isa}
Requires: %{name}-lcl%{?_isa} = %{version}-%{release}

%description tools
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package provides helper programs used for building Lazarus projects.

%package doc
Summary: Lazarus IDE documentation
License: %{license_doc}

%description doc
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains documentation and example programs for the Lazarus IDE.

%package lcl
Summary: Lazarus Component Library

%description lcl
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains the common parts of the Lazarus Component Library.

%package lcl-nogui
Summary: Lazarus Component Library - non-graphical components
Requires: %{name}-lcl%{?_isa} = %{version}-%{release}

%description lcl-nogui
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains LCL components for developing non-graphical applications
and command-line tools.

%package lcl-gtk
Summary: Lazarus Component Library - GTK+ widgetset support
Requires: %{name}-lcl%{?_isa} = %{version}-%{release}

Requires: gtk+-devel%{?_isa}

%description lcl-gtk
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains LCL components for developing applications
using the GTK+ widgetset.

%package lcl-gtk2
Summary: Lazarus Component Library - GTK2 widgetset support
Requires: %{name}-lcl%{?_isa} = %{version}-%{release}

Requires: gtk2-devel%{?_isa}

%description lcl-gtk2
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains LCL components for developing applications
using the GTK2 widgetset.

%package lcl-gtk3
Summary: Lazarus Component Library - GTK3 widgetset support
Requires: %{name}-lcl%{?_isa} = %{version}-%{release}

Requires: gtk3-devel%{?_isa}

%description lcl-gtk3
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains LCL components for developing applications
using the GTK3 widgetset.

%package lcl-qt
Summary: Lazarus Component Library - Qt widgetset support
Requires: %{name}-lcl%{?_isa} = %{version}-%{release}

Requires: qt-devel%{?_isa}
Requires: qt4pas-devel%{?_isa}

%description lcl-qt
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains LCL components for developing applications
using the Qt widgetset.

%package lcl-qt5
Summary: Lazarus Component Library - Qt5 widgetset support
Requires: %{name}-lcl%{?_isa} = %{version}-%{release}

Requires: qt5pas-devel%{?_isa} = %{qt5pas_version}-%{qt5pas_release}

%description lcl-qt5
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains LCL components for developing applications
using the Qt5 widgetset.

%package lcl-qt6
Summary: Lazarus Component Library - Qt6 widgetset support
Requires: %{name}-lcl%{?_isa} = %{version}-%{release}

Requires: qt6pas-devel%{?_isa} = %{qt6pas_version}-%{qt6pas_release}

%description lcl-qt6
Lazarus is a cross-platform IDE and component library for Free Pascal.

This package contains LCL components for developing applications
using the Qt6 widgetset.

# Qt5pas start
%package -n     qt5pas
Version:        %{qt5pas_version}
Release:        %{qt5pas_release}
Summary:        Qt5 bindings for Pascal

%description -n qt5pas
Qt5 bindings for Pascal from Lazarus.

%package -n     qt5pas-devel
Version:        %{qt5pas_version}
Release:        %{qt5pas_release}
Summary:        Development files for qt5pas

Requires:       qt5-qtbase-devel%{?_isa}
Requires:       qt5-qtx11extras-devel%{?_isa}
Requires:       qt5pas%{?_isa} = %{qt5pas_version}-%{qt5pas_release}

%description -n qt5pas-devel
The qt5pas-devel package contains libraries and header files for
developing applications that use qt5pas.

# Qt5pas end, Qt6pas start
%package -n     qt6pas
Version:        %{qt6pas_version}
Release:        %{qt6pas_release}
Summary:        Qt6 bindings for Pascal

%description -n qt6pas
Qt6 bindings for Pascal from Lazarus.

%package -n     qt6pas-devel
Version:        %{qt6pas_version}
Release:        %{qt6pas_release}
Summary:        Development files for qt6pas

Requires:       qt6-qtbase-devel%{?_isa}
Requires:       qt6pas%{?_isa} = %{qt6pas_version}-%{qt6pas_release}

%description -n qt6pas-devel
The qt6pas-devel package contains libraries and header files for
developing applications that use qt6pas.
# Qt6pas end

# Instruct fpmake to build in parallel
%global fpmakeopt %{?_smp_build_ncpus:FPMAKEOPT='-T %{_smp_build_ncpus}'}

# Preferred compilation options - enable GDB debuginfo in DWARF format, plus some optimisations
%global fpcopt -g -gl -gw -O3

%prep
%autosetup -c -p1

%build
cd lazarus

# Remove the files for building other packages
rm -rf debian
pushd tools
find install -depth -type d ! \( -path "install/linux/*" -o -path "install/linux" -o -path "install" \) -exec rm -rf '{}' \;
popd

# Re-create the Makefiles
export FPCDIR=%{_datadir}/fpcsrc/
fpcmake -Tall
pushd components
fpcmake -Tall
popd

# Compile some basic targets required by everything else
make registration %{fpmakeopt} OPT='%{fpcopt}'

# Compile lazbuild - required to build other targets
make lazbuild %{fpmakeopt} OPT='%{fpcopt}'

# Compile LCL base (Lazarus Component Library) for the "nogui" widgetset
make lcl %{fpmakeopt} OPT='%{fpcopt}' LCL_PLATFORM=nogui

# Compile extra tools
make tools %{fpmakeopt} OPT='%{fpcopt}'

# Compile the LCL base + extra components for GUI widgetsets
for WIDGETSET in gtk gtk2 gtk3 qt qt5 qt6; do
	make lcl basecomponents bigidecomponents %{fpmakeopt} OPT='%{fpcopt}' LCL_PLATFORM="${WIDGETSET}"
done

# Compile the IDE itself
# TODO: Could try building the IDE with multiple widgetsets, as well!
make bigide %{fpmakeopt} OPT='%{fpcopt}' LCL_PLATFORM=gtk2

# Build Qt5Pas
pushd lcl/interfaces/qt5/cbindings/
	%{qmake_qt5}
	%make_build
popd

# Build Qt6Pas
pushd lcl/interfaces/qt6/cbindings/
	%{qmake_qt6}
	%make_build
popd

%install
make -C lazarus install INSTALL_PREFIX=%{buildroot}%{_prefix} _LIB=%{_lib}

# Remove man page for an executable that is not actually installed.
rm %{buildroot}%{_mandir}/man1/svn2revisioninc.1* || true

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	lazarus/install/%{name}.desktop

install -d %{buildroot}%{_sysconfdir}/lazarus
sed 's#__LAZARUSDIR__#%{_libdir}/%{name}#;s#__FPCSRCDIR__#%{_datadir}/fpcsrc#' \
	lazarus/tools/install/linux/environmentoptions.xml \
	> %{buildroot}%{_sysconfdir}/lazarus/environmentoptions.xml

chmod 755 %{buildroot}%{_libdir}/%{name}/components/lazreport/tools/localize.sh

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 %{SOURCE100} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# -- Install Qt5Pas and Qt6Pas

for QTVER in 5 6; do
	pushd "lazarus/lcl/interfaces/qt${QTVER}/cbindings/"
		%make_install INSTALL_ROOT=%{buildroot}
	popd

	# Since we provide Qt?Pas as a standalone package, remove the .so files bundled in Lazarus dir
	# and replace them with symlinks to the standalone .so.
	for FILEPATH in "%{buildroot}%{_libdir}/%{name}/lcl/interfaces/qt${QTVER}/cbindings/libQt${QTVER}Pas.so"* ; do
		FILENAME="$(basename "${FILEPATH}")"
		ln -sfr "%{buildroot}%{_libdir}/${FILENAME}" "${FILEPATH}"
	done

	# Cannot be done earlier since "make install" expects the tmp/ directory to be present. Sigh.
	rm -rf "%{buildroot}%{_libdir}/%{name}/lcl/interfaces/qt${QTVER}/cbindings/tmp/"
done

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
# No files, but we want to build the "lazarus" metapackage

%files doc
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/docs
%{_libdir}/%{name}/examples

%license lazarus/COPYING.GPL.txt

# -- IDE files

%files ide
%{_libdir}/%{name}

# Exclude -docs files
%exclude %{_libdir}/%{name}/docs
%exclude %{_libdir}/%{name}/examples

# Exclude -lcl files
%exclude %{_libdir}/%{name}/components
%exclude %{_libdir}/%{name}/lcl

# Exclude -tools files
%exclude %{_libdir}/%{name}/lazbuild
%exclude %{_libdir}/%{name}/packager
%exclude %{_libdir}/%{name}/tools

# Exclude some files that belong in the ide/ directory
# but are actually required by lazbuild to run properly.
%exclude %{_libdir}/%{name}/ide/packages/ideconfig
%exclude %{_libdir}/%{name}/ide/packages/idedebugger
%exclude %{_libdir}/%{name}/ide/packages/idepackager
%exclude %{_libdir}/%{name}/ide/packages/ideproject
%exclude %{_libdir}/%{name}/ide/packages/ideutils

%{_bindir}/lazarus-ide
%{_bindir}/startlazarus
%{_datadir}/pixmaps/lazarus.png
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/mime/packages/lazarus.xml
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%{_metainfodir}/%{name}.appdata.xml

%doc lazarus/README.md
%license lazarus/COPYING.txt
%license lazarus/COPYING.LGPL.txt
%license lazarus/COPYING.modifiedLGPL.txt
%{_mandir}/man1/lazarus-ide.1*
%{_mandir}/man1/startlazarus.1*

# -- Tools files

%files tools
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lazbuild
%{_libdir}/%{name}/packager/
%{_libdir}/%{name}/tools/

%dir %{_libdir}/%{name}/ide/
%dir %{_libdir}/%{name}/ide/packages/
%{_libdir}/%{name}/ide/packages/ideconfig
%{_libdir}/%{name}/ide/packages/idedebugger
%{_libdir}/%{name}/ide/packages/idepackager
%{_libdir}/%{name}/ide/packages/ideproject
%{_libdir}/%{name}/ide/packages/ideutils

%{_bindir}/lazbuild
%{_bindir}/lazres
%{_bindir}/lrstolfm
%{_bindir}/updatepofiles

%dir %{_sysconfdir}/lazarus
%config(noreplace) %{_sysconfdir}/lazarus/environmentoptions.xml

%license lazarus/COPYING.GPL.txt
%{_mandir}/man1/lazbuild.1*
%{_mandir}/man1/lazres.1*
%{_mandir}/man1/lrstolfm.1*
%{_mandir}/man1/updatepofiles.1*

# -- LCL files

# Helper macro to reduce repetitions (lcl, basecomponents)
%define lcl_base_files(n:) %{expand:
	%{*} %{_libdir}/%{name}/components/*/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/units/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/lcl/interfaces/%{-n*}/
	%{*} %{_libdir}/%{name}/lcl/units/*/%{-n*}/
}

# Some files are not present for nogui (bigidecomponents)
%define lcl_extra_files(n:) %{expand:
	%{*} %{_libdir}/%{name}/components/*/design/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/design/units/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/include/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/include/intf/%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/lib/*-linux-%{-n*}/
	%{*} %{_libdir}/%{name}/components/*/units/%{-n*}/

	%{*} %{_libdir}/%{name}/components/chmhelp/packages/help/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/chmhelp/packages/idehelp/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/fpcunit/ide/lib/*-linux/%{-n*}/
	%{*} %{_libdir}/%{name}/components/jcf2/IdePlugin/lazarus/lib/*-linux/%{-n*}/
}

# -- LCL base

%files lcl
%license lazarus/COPYING.txt
%license lazarus/COPYING.LGPL.txt
%license lazarus/COPYING.modifiedLGPL.txt
%license %{_libdir}/%{name}/lcl/interfaces/customdrawn/android/ApacheLicense2.0.txt

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/components/
%{_libdir}/%{name}/lcl/
%lcl_base_files -n nogui %exclude
%lcl_base_files  -n gtk %exclude
%lcl_extra_files -n gtk %exclude
%lcl_base_files  -n gtk2 %exclude
%lcl_extra_files -n gtk2 %exclude
%lcl_base_files  -n gtk3 %exclude
%lcl_extra_files -n gtk3 %exclude
%lcl_base_files  -n qt %exclude
%lcl_extra_files -n qt %exclude
%lcl_base_files  -n qt5 %exclude
%lcl_extra_files -n qt5 %exclude
%lcl_base_files  -n qt6 %exclude
%lcl_extra_files -n qt6 %exclude

# -- LCL widgetsets

%files lcl-nogui
%lcl_base_files -n nogui

%files lcl-gtk
%lcl_base_files -n gtk
%lcl_extra_files -n gtk

%files lcl-gtk2
%lcl_base_files -n gtk2
%lcl_extra_files -n gtk2

%files lcl-gtk3
%lcl_base_files -n gtk3
%lcl_extra_files -n gtk3

%files lcl-qt
%lcl_base_files -n qt
%lcl_extra_files -n qt

%files lcl-qt5
%lcl_base_files -n qt5
%lcl_extra_files -n qt5

%files lcl-qt6
%lcl_base_files -n qt6
%lcl_extra_files -n qt6

# -- Qt5pas

%files -n qt5pas
%license lazarus/lcl/interfaces/qt5/cbindings/COPYING.TXT
%doc lazarus/lcl/interfaces/qt5/cbindings/README.TXT
%{_libdir}/libQt5Pas.so.*

%files -n qt5pas-devel
%{_libdir}/libQt5Pas.so

# -- Qt6pas

%files -n qt6pas
%license lazarus/lcl/interfaces/qt6/cbindings/COPYING.TXT
%doc lazarus/lcl/interfaces/qt6/cbindings/README.TXT
%{_libdir}/libQt6Pas.so.*

%files -n qt6pas-devel
%{_libdir}/libQt6Pas.so

%changelog
%autochangelog
