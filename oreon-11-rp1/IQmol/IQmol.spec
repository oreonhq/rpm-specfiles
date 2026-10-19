%global source0_hash d13812427e8081702da660007984df59eaaa12e1b2872b16178efdf268064242
Name:           IQmol
Version:        3.2.3
Release:        1%{?dist}
Summary:        A free open-source molecular editor and visualization package
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://iqmol.org
Source0:        https://github.com/nutjunkie/IQmol3/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         IQmol3-fragdir.patch
Patch4:         IQmol-2.13-openbabel.patch
Patch5:         IQmol-3.2.0-cmake.patch
Patch6:         IQmol-3.2.0-qmsgbox.patch
Patch7:         IQmol-3.1.2-builddeps.patch
Patch8:         IQmol3-3.1.2-missinglink.patch
Patch9:         IQmol-3.1.4-fixdesktop.patch
Patch10:        https://github.com/nutjunkie/IQmol3/pull/26.patch
Patch11:        https://github.com/nutjunkie/IQmol3/pull/27.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  OpenMesh-devel
BuildRequires:  QMsgBox-qt5-devel
BuildRequires:  armadillo-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gl2ps-devel
BuildRequires:  highfive-devel
BuildRequires:  libQGLViewer-qt5-devel
BuildRequires:  libarchive-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libssh2-devel
BuildRequires:  libzstd-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openbabel-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  yaml-cpp-devel
# /oreon:deps
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

%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%install
%cmake_install
install -D -p -m 755 %{__cmake_builddir}/IQmol %{buildroot}%{_bindir}/IQmol
mkdir -p %{buildroot}%{_datadir}/IQmol
cp -pr share/* %{buildroot}%{_datadir}/IQmol/
install -D -p -m 644 resources/IQmol.png %{buildroot}%{_datadir}/pixmaps/IQmol.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ resources/iqmol.desktop
%oreon_autofiles IQmol-samples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n IQmol-samples -f %{oreon_filedir}/IQmol-samples.list

%changelog

%autochangelog
