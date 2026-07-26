%global source0_hash 02aa6ab28722b61197e9a71c0c0220c01013f72e382c833841708ff97566e693

%global owner SciDAVis

# Force out of source build
%undefine __cmake_in_source_build

Name:           scidavis
Version:        2.9.0
Release:        21%{?dist}
Summary:        Application for Scientific Data Analysis and Visualization

License:        GPL-3.0-or-later
URL:            http://scidavis.sourceforge.net/
#Source0:        http://downloads.sourceforge.net/%%{name}/%%{name}-%%{version}.tar.gz
# Main upstream development repository (master, snapshots, releases not yet in sf)
#Source0:        https://github.com/%%{owner}/%%{name}/archive/%%{version}/%%{name}-master.tar.gz
Source0:        https://github.com/%{owner}/%{name}/archive/master/%{name}-%{version}.tar.gz
Patch0:         scidavis-build_w_system_qwtplot3d.patch
# https://github.com/SciDAVis/scidavis/pull/31
Patch1:         scidavis-fix_building_w_liborigin302.patch
# https://github.com/SciDAVis/scidavis/pull/32
Patch2:         scidavis-add_minigzip_includes.patch

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  desktop-file-utils
BuildRequires:  gsl-devel
BuildRequires:  liborigin-devel
BuildRequires:  gl2ps-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  muParser-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qwt5-qt5-devel
BuildRequires:  qwtplot3d-qt5-devel
BuildRequires:  PyQt-builder
BuildRequires:  python3dist(sip)
BuildRequires:  python3-pyqt5-sip
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
BuildRequires:  zlib-devel
BuildRequires:  libappstream-glib
# required for the tests, enable when building locally
#BuildRequires:  xorg-x11-server-Xvfb
#BuildRequires:  unittest-cpp-devel
#BuildRequires:  boost-devel
#BuildRequires:  gtest

Requires:       python3-qt5
Requires:       hicolor-icon-theme
Requires:       kde-filesystem

Recommends:     python3-%{name}

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
# Set python version to 3
export PYTHON=python3
%cmake -DSEARCH_FOR_UPDATES=off -DDOWNLOAD_LINKS=off -DSCRIPTING_MUPARSER=on -DSCRIPTING_PYTHON=on -DORIGIN_IMPORT=on
%cmake_build

%install
%cmake_install
install -pm 644 ChangeLog.md %{buildroot}%{_docdir}/%{name}/

# KDE3 remnant - upstream is aware
rm -rf %{buildroot}%{_datadir}/mimelnk/

# gpl.txt is copied over by the license macro
rm -f %{buildroot}%{_docdir}/%{name}/gpl.txt
rm -f %{buildroot}%{_docdir}/%{name}/license.rtf

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
# Enable testsuite when building locally
#cd test && xvfb-run -a ./unittests

%files
%license gpl.txt LICENSE license.rtf
%{_mandir}/man1/%{name}.1*
%{_docdir}/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/locolor/*/apps/%{name}.*

%files -n python3-%{name}
%{python3_sitearch}/%{name}/

%changelog
%autochangelog
