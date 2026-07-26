%global source0_hash 20222a84e3b4246c36b8a0b74834bb5674026ffdb8b9093a76aaf01560ad4815

Name: libresample
Version: 0.1.3
Summary: A real-time library for audio sampling rate conversion
Release: 48%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: https://ccrma.stanford.edu/~jos/resample/Free_Resampling_Software.html
Source0: http://ccrma.stanford.edu/~jos/gz/libresample-%{version}.tgz
Source1: libresample.pc
Patch1: libresample_shared-libs.patch
BuildRequires: cmake >= 2.4
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: make

%description
A real-time library for audio sampling rate conversion providing
several useful features relative to resample-1.7 on which it is based:

    * It should build "out of the box" on more platforms, including
      Linux, Solaris, and Mac OS X (using the included configure
      script). There is also a Visual C++ project file for building
      under Windows.

    * Input and output signals are in memory (as opposed to sound
      files).

    * Computations are in floating-point (instead of fixed-point).

    * Filter table increased by a factor of 32, yielding more accurate
      results, even without linear interpolation (which also makes it
      faster).

    * Data can be processed in small chunks, enabling time-varying
      resampling ratios (ideal for time-warping applications and
      supporting an ``external clock input'' in software).

    * Easily applied to any number of simultaneous data channels 

%package devel
Summary: Development files for libresample
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libresample.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
mkdir pkgconfig
cp %{SOURCE1} pkgconfig/

%build
%configure

%make_build VERBOSE=1

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mkdir -p %{buildroot}%{_includedir}
cp tests/resample-sndfile %{buildroot}%{_bindir}/
cp libresample.so.0 %{buildroot}%{_libdir}/
cp include/libresample.h %{buildroot}%{_includedir}/
cp libresample.so %{buildroot}%{_libdir}/
cp pkgconfig/libresample.pc %{buildroot}%{_libdir}/pkgconfig/

%check
export LD_LIBRARY_PATH=.
make tests

%ldconfig_scriptlets

%files
%doc LICENSE.txt README.txt
%{_bindir}/resample-sndfile
%{_libdir}/libresample.so.0

%files devel
%doc README.txt
%license LICENSE.txt
%{_includedir}/libresample.h
%{_libdir}/libresample.so
%{_libdir}/pkgconfig/libresample.pc

%changelog
%autochangelog
