%global source0_hash 3d6ee056dab91f3b34a3f233de6a15331737848a4cbdb4e0552123d95eed4485
Name:       fann
Summary:        A fast artificial neural network library
Version:    2.2.0
Release:        1%{?dist}
License:    LGPL-2.0-or-later
URL:        http://leenissen.dk/fann/wp/
Source0:        http://downloads.sourceforge.net/fann/fann/2.2.0/FANN-%{version}-Source.tar.gz
Patch0:     fann-2.2.0-pkgconfig.patch
Patch1:     fann-memcorruption.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Fast Artificial Neural Network (FANN) Library is written in ANSI C.
The library implements multilayer feedforward ANNs, up to 150 times faster
than other libraries. FANN supports execution in fixed point, for fast 
execution on systems like the iPAQ.

%package devel
Summary: Development libraries for FANN
Requires: %{name} = %{version}-%{release} pkgconfig
%description devel
This package is only needed if you intend to develop and/or compile programs 
based on the FANN library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n FANN-%{version}-Source
%patch -P0 -p1
%patch -P1 -p1 -b .memcorruption

LIBS=-lm
export LIBS

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake} -DPKGCONFIG_INSTALL_DIR=/%{_lib}/pkgconfig \
	%if "%{?_lib}" == "lib64"
		%{?_cmake_lib_suffix64} \
	%endif
make -C "%{_vpath_builddir}"
%install
make -C "%{_vpath_builddir}" DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n fann-devel -f %{oreon_filedir}/fann-devel.list

%changelog

%autochangelog
