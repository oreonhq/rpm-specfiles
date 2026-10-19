%global source1_hash e74c5106fa3d8b7e3855807bf10dca8325f4f141586f6b99058c868873def09a
%global source0_hash 2005cac17520b2771d6f3ddbcedb96da0944f7a2af9bf5c0bfb3dd543b4440a5
%global gitcommit_full c6e6c03143c5b397a9217fae2f6423ccf9c03fb7
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global tools_build convbin pos2kml str2str rnx2rtkp rtkrcv
Name:           rtklib
Version:        2.4.3.b33
Release:        1%{?dist}
Summary:        Program Package for GNSS Positioning
License:        LicenseRef-Callaway-BSD
URL:            http://www.rtklib.com
Source0:        https://github.com/tomojitakasu/RTKLIB/tarball/%{gitcommit_full}/%{name}-%{gitcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/tomojitakasu/RTKLIB/master/readme.txt
Patch0:         rtklib-qt.patch
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtserialport-devel
# /oreon:deps
%description
RTKLIB is an open source program package for standard and precise
positioning with GNSS (global navigation satellite system). RTKLIB
consists of a portable program library and several APs (application
programs) utilizing the library.

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
Include files and mandatory libraries for development.

%package        doc
Summary:        RTKLIB manual
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    doc
Manual for RTKLIB tools.

%package        libs
Summary:        RTKLIB shared library
%description    libs
RTKLIB Shared library.

%package        qt
Summary:        RTKLIB GUI tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    qt
GUI part of RTKLIB tools.

%prep

%setup -q -n tomojitakasu-RTKLIB-%{gitcommit}
# License text not in separate file and not in packaged branch
# https://github.com/tomojitakasu/RTKLIB/issues/540
cp %{SOURCE1} readme_orig.txt
%patch -P0 -p1

sed -e "s|target.path = /usr/lib|target.path = %{buildroot}%{_libdir}|" \
    -e "s|staticlib|sharedlib|" -i src/src.pro
sed -i "s|LDLIBS  = ../../../lib/iers/gcc/iers.a|LDLIBS  = ../../../lib/libiers.a|" app/rnx2rtkp/gcc/makefile
# Correct CLI tools build flags
for i in %{tools_build}; do
    pushd app/$i/gcc
        sed -i "s|-O3|%{optflags}|" makefile
    popd
done

%build

%{qmake_qt5}
%make_build
pushd lib
    %{qmake_qt5}
    %make_build
popd
for i in %{tools_build}; do
    pushd app/$i/gcc
        %make_build
    popd
done
%install
%make_install
mkdir -p %{buildroot}/%{_bindir}
install -pm 755 app/rtknavi_qt/rtknavi_qt %{buildroot}%{_bindir}
install -pm 755 app/rtkget_qt/rtkget_qt %{buildroot}%{_bindir}
install -pm 755 app/rtkplot_qt/rtkplot_qt %{buildroot}%{_bindir}
install -pm 755 app/rtkpost_qt/rtkpost_qt %{buildroot}%{_bindir}
install -pm 755 app/rtklaunch_qt/rtklaunch_qt %{buildroot}%{_bindir}
install -pm 755 app/srctblbrows_qt/srctblbrows_qt %{buildroot}%{_bindir}
install -pm 755 app/strsvr_qt/strsvr_qt %{buildroot}%{_bindir}
install -pm 755 app/rtkconv_qt/rtkconv_qt %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -pm 755 app/convbin/gcc/convbin %{buildroot}%{_bindir}
install -pm 755 app/pos2kml/gcc/pos2kml %{buildroot}%{_bindir}
install -pm 755 app/str2str/gcc/str2str %{buildroot}%{_bindir}
install -pm 755 app/rnx2rtkp/gcc/rnx2rtkp %{buildroot}%{_bindir}
install -pm 755 app/rtkrcv/gcc/rtkrcv %{buildroot}%{_bindir}
install -pm 755 app/rtkrcv/gcc/rtk*.sh %{buildroot}%{_bindir}
install -pm 644 data/P1C1_ALL.DCB %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/P1P2_ALL.DCB %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/P2C2.DCB %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_GSI.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS08.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS_H.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS_HR.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/STA_IGS_MGEX.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/TLE_GNSS_SATNO.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/TLE_GNSS_SIM.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/URL_LIST.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/elmask_sample.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/gnssdatasrc.txt %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/igs10P1565_wocov.snx %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/ngs_abs.pcv %{buildroot}%{_datadir}/%{name}/
install -pm 644 data/stations.pos %{buildroot}%{_datadir}/%{name}/
chrpath --delete %{buildroot}%{_bindir}/*_qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rtklib-devel -f %{oreon_filedir}/rtklib-devel.list
%files -n rtklib-doc -f %{oreon_filedir}/rtklib-doc.list
%files -n rtklib-libs -f %{oreon_filedir}/rtklib-libs.list
%files -n rtklib-qt -f %{oreon_filedir}/rtklib-qt.list

%changelog

%autochangelog
