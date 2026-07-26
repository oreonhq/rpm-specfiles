%global source0_hash 0dea51046601e4d23dc45a3ec342f1a305baf3bf3328e9ccdae115fe1942f041

Name:			PerceptualDiff
Version:		2.1
Release:		15%{?dist}
Summary:		An image comparison utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:		GPL-2.0-or-later
URL:			https://github.com/myint/perceptualdiff
Source:		%{url}/archive/v%{version}/perceptualdiff-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: freeimage-devel
BuildRequires: libtiff-devel
BuildRequires: libpng-devel

Provides: perceptualdiff = %{version}-%{release}

%description
PerceptualDiff is an image comparison utility that makes use of a 
computational model of the human visual system to compare two images.

This software is released under the GNU General Public License.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n perceptualdiff-%{version}

%build
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_libdir}
find . -name libpdiff.so -exec mv {} %{buildroot}%{_libdir}/libpdiff.so ';'

%files
%doc README.rst
%license LICENSE
%{_bindir}/perceptualdiff
# TODO: fix SONAME
%{_libdir}/libpdiff.so

%changelog
%autochangelog
