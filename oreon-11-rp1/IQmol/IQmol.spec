%global source0_hash none

Name:           IQmol
Version:        3.2.0
Release:        4%{?dist}
Summary:        A free open-source molecular editor and visualization package
# Automatically converted from old format: BSD and GPLv2+ and GPLv3+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://iqmol.org
Source0:        https://github.com/nutjunkie/IQmol3/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch in correct fragment and QChem interface setting directory
Patch1:         IQmol3-fragdir.patch
# Don't mess with OpenBabel's directories
Patch4:         IQmol-2.13-openbabel.patch
# Fix CMake build
Patch5:         IQmol-3.2.0-cmake.patch
# Use external QMSGBox headers
Patch6:         IQmol-3.2.0-qmsgbox.patch
# Add missing interdependencies
Patch7:         IQmol-3.1.2-builddeps.patch
# and missing links
Patch8:         IQmol3-3.1.2-missinglink.patch
# Fix the desktop icon
Patch9:         IQmol-3.1.4-fixdesktop.patch
# Fix issues in source
Patch10:        https://github.com/nutjunkie/IQmol3/pull/26.patch
# Fix missing file error
Patch11:        https://github.com/nutjunkie/IQmol3/pull/27.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  armadillo-devel
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  desktop-file-utils
BuildRequires:  gl2ps-devel
BuildRequires:  highfive-devel
BuildRequires:  libarchive-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libssh2-devel
BuildRequires:  libQGLViewer-qt5-devel >= 2.9.1-1
BuildRequires:  libzstd-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  openbabel-devel
BuildRequires:  openssl-devel
BuildRequires:  OpenMesh-devel
BuildRequires:  QMsgBox-qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  cmake

%description
IQmol is a free open-source molecular editor and visualization
package. It offers a range of features including a molecular editor,
surface generation (orbitals and densities) and animations
(vibrational modes and reaction pathways).

%package samples
Summary:       Sample structures for IQmol
BuildArch:     noarch

%description samples
This package contains samples for IQmol.

%prep
%setup -q -n IQmol3-%{version}
%patch 1 -p1 -b .fragdir
%patch 4 -p1 -b .openbabel
%patch 5 -p1 -b .cmakebuild
%patch 6 -p1 -b .qmsgbox
#patch 7 -p1 -b .builddeps
%patch 8 -p1 -b .missinglink
%patch 9 -p1 -b .fixdesktop
%patch 10 -p1 -b .capitalization
%patch 11 -p1 -b .amber

# Get rid of bundled gl2ps
rm src/Viewer/gl2ps.{h,C}
# and of QMsgBox
rm src/Util/QMsgBox.{h,C}
# and of OpenMesh
rm -rf src/OpenMesh/

# The bundled FindOpenBabel file is wrong
\rm cmake/FindOpenBabel3.cmake

# Clean up MacOS file system junk
find . -name .DS_Store -delete

%build
# The IQmol build is based on libraries but the objects should be linked to the binary
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmake_install
install -D -p -m 755 %{__cmake_builddir}/IQmol %{buildroot}%{_bindir}/IQmol
mkdir -p %{buildroot}%{_datadir}/IQmol
cp -pr share/* %{buildroot}%{_datadir}/IQmol/
install -D -p -m 644 resources/IQmol.png %{buildroot}%{_datadir}/pixmaps/IQmol.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ resources/iqmol.desktop

%files
%license LICENSE
%doc README.md
%{_datadir}/applications/iqmol.desktop
%{_datadir}/pixmaps/IQmol.png
%{_datadir}/IQmol/
%{_bindir}/IQmol

%files samples
%license LICENSE
%doc samples/*

%changelog
%autochangelog
