%global source0_hash 4f4222820f97ca08c7ea707e4c53e5a3556af4d8f1ab51e0da6ff1627ff433ab
Name:      plotutils
Version:   2.6
Release:        1%{?dist}
Summary:        GNU vector and raster graphics utilities and libraries
License:   GPL-2.0-or-later AND GPL-3.0-or-later
URL:       http://www.gnu.org/software/plotutils/
Source0:        https://mirrors.kernel.org/gnu/plotutils/plotutils-%{version}.tar.gz
Patch0:    plotutils-2.6-png15.patch
Patch1:    plotutils-aarch64.patch
Patch2:    plotutils-werror-format-security.patch
Patch3: plotutils-configure-c99.patch
# oreon:deps
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
The GNU plotutils package contains software for both programmers and
technical users. Its centerpiece is libplot, a powerful C/C++ function
library for exporting 2-D vector graphics in many file formats, both
vector and raster. It can also do vector graphics animations. Besides
libplot, the package contains command-line programs for plotting
scientific data. Many of them use libplot to export graphics

%package devel
Summary:     Headers for developing programs that will use %{name}
Requires:    %{name} = %{version}-%{release}
%description devel
This package contains the header files needed for developing %{name}
applications

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .png15
%patch -P1 -p1 -b .aarch64
%patch -P2 -p1 -b .format-security
%patch -P3 -p1
# Avoid attempting autotools rebuild.
touch -r aclocal.m4 configure*

%build

%set_build_flags
export CFLAGS="$CFLAGS -std=gnu99"
%configure --disable-static --enable-libplotter --enable-libxmi --enable-ps-fonts-in-pcl
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
rm -rf docs-to-include
make install DESTDIR=$RPM_BUILD_ROOT
mkdir docs-to-include
mv ${RPM_BUILD_ROOT}%{_datadir}/ode docs-to-include
mv ${RPM_BUILD_ROOT}%{_datadir}/pic2plot docs-to-include
mv ${RPM_BUILD_ROOT}%{_datadir}/libplot docs-to-include
mv ${RPM_BUILD_ROOT}%{_datadir}/tek2plot docs-to-include
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n plotutils-devel -f %{oreon_filedir}/plotutils-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6-39
- Import
