%global source0_hash 816506b4d9c4a31962f8a6be6d06f0d6bd8f6e35f10e992a342c66d861211a30
ExcludeArch: aarch64 %{ix86} %{power64} s390x
Name:          qcas
Summary:        Qt5 GUI application for Giac
Version:       0.5.4
Release:        1%{?dist}
License:       GPL-3.0-or-later
URL:           https://webusers.imj-prg.fr/~frederic.han/qcas/
Source0:        https://gitlab.math.univ-paris-diderot.fr/han/qcas/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}.appdata.xml
Source3:       %{name}-qt4.desktop
Requires:      %{name}-data = %{version}-%{release}
Requires:       giac%{?_isa} >= 2.0.0
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  giac-devel
BuildRequires:  gmp-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
# /oreon:deps
%description
Minimal Qt5 interface for Giac.

%package        qt4
Summary:        Qt4 GUI application for Giac
BuildRequires:  qt-devel
Requires:      %{name}-data = %{version}-%{release}
Requires:       giac%{?_isa} >= 2.0.0
%description    qt4
Minimal Qt4 interface for Giac.

### This library is used by giacpy ####
%package        -n libqcas
Summary:        Private library of Qcas
Requires:       gcc-gfortran%{?_isa}
BuildRequires:  giac-devel >= 2.0.0
%description    -n libqcas
Private library of Qcas.

%package        -n libqcas-devel
Summary:        Development files of lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
%description    -n libqcas-devel
This package contains libraries and header files for developing
applications that use lib%{name}.
#######################################

%package        data
Summary:        Data files of Qcas
Requires:       giac-doc >= 2.0.0
BuildArch:      noarch
%description    data
Data files of Qcas.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
rm -rf libtommath

%build

mkdir build && pushd build
%{qmake_qt5} ../%{name}.pro \
 QMAKE_CFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_CXXFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_LFLAGS="$RPM_LD_FLAGS"
%make_build
sed -e 's|CONFIG+=staticlib|#CONFIG+=staticlib|g' -i ../lib%{name}.pro
%{qmake_qt5} ../lib%{name}.pro QMAKE_STRIP=echo
%make_build
popd
mkdir build2 && pushd build2
%{qmake_qt4} ../%{name}.pro \
 QMAKE_CFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_CXXFLAGS_RELEASE="$RPM_OPT_FLAGS" \
 QMAKE_LFLAGS="$RPM_LD_FLAGS"
%make_build
popd
%install
pushd build
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ./qcas %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
install -p -m 755 ./lib%{name}.* %{buildroot}%{_libdir}
ln -sf libqcas.so.1.0.0 %{buildroot}%{_libdir}/libqcas.so
ln -sf libqcas.so.1.0.0 %{buildroot}%{_libdir}/libqcas.so.1
ln -sf libqcas.so.1.0.0 %{buildroot}%{_libdir}/libqcas.so.1.0
mkdir -p %{buildroot}%{_includedir}/lib%{name}
install -pm 644 ui_MainWindow.h \
 ../qt/MainWindow.h \
 ../qt/output.h \
 ../qt/CasManager.h \
 ../qt/geometry.h \
 ../qt/config.h \
 ../qt/giacpy.h \
 ../qt/sizeof_void_p.h %{buildroot}%{_includedir}/lib%{name}/
mkdir -p %{buildroot}%{_includedir}/lib%{name}/gui
install -pm 644 ../qt/gui/WizardMatrix.h \
 ../qt/gui/WizardEquation.h \
 ../qt/gui/WizardCatalog.h \
 ../qt/gui/WizardAlgo.h \
 ../qt/gui/spreadsheet.h \
 ../qt/gui/qtmmlwidget.h \
 ../qt/gui/FormalSheet.h \
 ../qt/gui/FormalLineWidgets.h \
 ../qt/gui/FormalLine.h \
 ../qt/gui/CentralTabWidget.h \
 ../qt/gui/prefdialog.h \
 ../qt/gui/plotfunctiondialog.h  %{buildroot}%{_includedir}/lib%{name}/gui/
popd
pushd build2
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ./qcas %{buildroot}%{_bindir}/qcas-qt4
popd
mkdir -p %{buildroot}%{_datadir}/qcas
cp -a qt/doc qt/lang qt/images %{buildroot}%{_datadir}/qcas
install -pm 644 qt/aide_cas %{buildroot}%{_datadir}/qcas
install -pm 644 qt/aide_cas %{buildroot}%{_datadir}/qcas/doc
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 qt/images/icon.png %{buildroot}%{_datadir}/pixmaps/qcas.png
desktop-file-install %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install %{SOURCE3} %{buildroot}%{_datadir}/applications/%{name}-qt4.desktop
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%oreon_autofiles libqcas usr/*/lib*.so.*
%oreon_autofiles libqcas-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qcas-qt4 -f %{oreon_filedir}/qcas-qt4.list
%files -n libqcas -f %{oreon_filedir}/libqcas.list
%files -n libqcas-devel -f %{oreon_filedir}/libqcas-devel.list
%files -n qcas-data -f %{oreon_filedir}/qcas-data.list

%changelog

%autochangelog
