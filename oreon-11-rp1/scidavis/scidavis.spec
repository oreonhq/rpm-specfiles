%global source0_hash 856e057a0b7c35956121619f1c427d614766f7c0a26d45fc0c9dc576d99a2f92
%global owner SciDAVis
%undefine __cmake_in_source_build
Name:           scidavis
Version:        2.9.0
Release:        1%{?dist}
Summary:        Application for Scientific Data Analysis and Visualization
License:        GPL-3.0-or-later
URL:            http://scidavis.sourceforge.net/
Source0:        https://github.com/%{owner}/%{name}/archive/master/%{name}-%{version}.tar.gz
Patch0:         scidavis-build_w_system_qwtplot3d.patch
Patch1:         scidavis-fix_building_w_liborigin302.patch
Patch2:         scidavis-add_minigzip_includes.patch
Requires:       python3-qt5
Requires:       hicolor-icon-theme
Requires:       kde-filesystem
Recommends:     python3-%{name}
# oreon:deps
BuildRequires:  PyQt-builder
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gl2ps-devel
BuildRequires:  gsl-devel
BuildRequires:  libappstream-glib
BuildRequires:  liborigin-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  muParser-devel
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-pyqt5-sip
BuildRequires:  python3-qt5-devel
BuildRequires:  python3dist(sip)
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qwt5-qt5-devel
BuildRequires:  qwtplot3d-qt5-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
SciDAVis is a free interactive application aimed at data analysis and
publication-quality plotting. It combines a shallow learning curve and
an intuitive, easy-to-use graphical user interface with powerful
features such as scriptability and extensibility.

%package -n python3-%{name}
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
Summary:        Python 3 bindings for SciDAVis
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:      python2-%{name} < 1.23-5
%description -n python3-%{name}
This module provides SciDAVis bindings to the Python3 programming language.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
# Development builds
#%%setup -q -n %%{name}-master
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
# Set the correct python paths
sed -i 's+pythonconfig.path = "$$INSTALLBASE/../etc"+pythonconfig.path = "$$INSTALLBASE/..%{python3_sitearch}/scidavis"+g' config.pri
sed -i 's+pythonutils.path = "$$INSTALLBASE/share/scidavis"+pythonutils.path = "$$INSTALLBASE/..%{python3_sitearch}/scidavis"+g' config.pri
sed -i 's+set(PYTHON_SCRIPTDIR etc+set(PYTHON_SCRIPTDIR %{python3_sitearch}/scidavis+g' scidavis/CMakeLists.txt
sed -i 's+FILES scidavisrc.py ${CMAKE_CURRENT_BINARY_DIR}/$<CONFIG>/scidavisrc.pyc DESTINATION+FILES scidavisrc.py DESTINATION+g' scidavis/CMakeLists.txt
sed -i 's+FILES scidavisrc.py ${CMAKE_CURRENT_BINARY_DIR}/scidavisrc.pyc DESTINATION+FILES scidavisrc.py DESTINATION+g' scidavis/CMakeLists.txt
sed -i 's+FILES scidavisUtil.py DESTINATION share/scidavis+FILES scidavisUtil.py DESTINATION ${PYTHON_SCRIPTDIR}+g' scidavis/CMakeLists.txt
sed -i 's+PYTHON_CONFIG_PATH="${CMAKE_INSTALL_PREFIX}/etc"+PYTHON_CONFIG_PATH="%{python3_sitearch}/scidavis"+g' libscidavis/CMakeLists.txt
sed -i 's+PYTHON_UTIL_PATH="${CMAKE_INSTALL_PREFIX}/share/scidavis"+PYTHON_UTIL_PATH="%{python3_sitearch}/scidavis"+g' libscidavis/CMakeLists.txt

%build

export PYTHON=python3
%cmake -DSEARCH_FOR_UPDATES=off -DDOWNLOAD_LINKS=off -DSCRIPTING_MUPARSER=on -DSCRIPTING_PYTHON=on -DORIGIN_IMPORT=on
%cmake_build
%install
%cmake_install
install -pm 644 ChangeLog.md %{buildroot}%{_docdir}/%{name}/
rm -rf %{buildroot}%{_datadir}/mimelnk/
rm -f %{buildroot}%{_docdir}/%{name}/gpl.txt
rm -f %{buildroot}%{_docdir}/%{name}/license.rtf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n python3-scidavis -f %{oreon_filedir}/python3-scidavis.list

%changelog

%autochangelog
