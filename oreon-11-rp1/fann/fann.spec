%global source0_hash 3d6ee056dab91f3b34a3f233de6a15331737848a4cbdb4e0552123d95eed4485

Name:       fann
Summary:    A fast artificial neural network library
Version:    2.2.0
Release:    38%{?dist}
License:    LGPL-2.0-or-later
URL:        http://leenissen.dk/fann/wp/

Source:     http://downloads.sourceforge.net/fann/fann/2.2.0/FANN-%{version}-Source.tar.gz
Patch0:     fann-2.2.0-pkgconfig.patch
Patch1:     fann-memcorruption.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: make

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
# TODO: Please submit an issue to upstream (rhbz#2380569)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake} -DPKGCONFIG_INSTALL_DIR=/%{_lib}/pkgconfig \
	%if "%{?_lib}" == "lib64"
		%{?_cmake_lib_suffix64} \
	%endif

make -C "%{_vpath_builddir}"

%install
make -C "%{_vpath_builddir}" DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING.txt
%doc README.txt
%{_libdir}/libdoublefann.so.2
%{_libdir}/libdoublefann.so.2.2.0
%{_libdir}/libfloatfann.so.2
%{_libdir}/libfloatfann.so.2.2.0
%{_libdir}/libfixedfann.so.2
%{_libdir}/libfixedfann.so.2.2.0
%{_libdir}/libfann.so.2
%{_libdir}/libfann.so.2.2.0

%files devel
%{_libdir}/pkgconfig/fann.pc
%{_libdir}/libdoublefann.so
%{_libdir}/libfann.so
%{_libdir}/libfixedfann.so
%{_libdir}/libfloatfann.so
%{_includedir}/*.h

%changelog
%autochangelog
