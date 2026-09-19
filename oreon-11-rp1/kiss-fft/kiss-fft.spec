%global source0_hash 205a8f6a448ef12b091f8ac6a514b5091bb5f6b0b543431ed75f673116cf5cbf

%global srcname kissfft
%global srcver 131

%global build_types %{?build_types} float
%global build_types %{?build_types} double
%global build_types %{?build_types} int16_t
%global build_types %{?build_types} int32_t

# Tests fail on many arches
%bcond_with     tests

Summary:        A Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid
Name:           kiss-fft
License:        BSD-3-Clause

Version:        %{srcver}.2.0
Release:        1%{?dist}

URL:            https://github.com/mborgerding/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

#Patch from upstream https://github.com/mborgerding/kissfft/commit/1b08316582049c3716154caefc0deab8758506e3
Patch0:         %{name}-integer-overflow.patch

BuildRequires:  cmake

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  python3
# Use cmake28 package on RHEL.
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  cmake28 >= 2.8.5	
%else
BuildRequires:  cmake >= 2.8.5	
%endif
BuildRequires:  fftw-devel
# For tests
%if %{with tests}
BuildRequires:  python3-numpy
%endif

%description
KISS FFT - A mixed-radix Fast Fourier Transform based on the 
principle, "Keep It Simple, Stupid."

There are many great fft libraries already around. Kiss FFT is
not trying to be better than any of them. It only attempts to be
a reasonably efficient, moderately useful FFT that can use fixed
or floating data types and can be incorporated into someone's C
program in a few minutes with trivial licensing.

%package static
Summary:        A Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libraries for KISS FFT - A mixed-radix Fast Fourier Transform based 
on the principle, "Keep It Simple, Stupid."

%package devel
Summary:        A Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Dynamically linked libraries and header files for KISS FFT - A mixed-radix Fast 
Fourier Transform based on the principle, "Keep It Simple, Stupid."

There are many great fft libraries already around. Kiss FFT is
not trying to be better than any of them. It only attempts to be
a reasonably efficient, moderately useful FFT that can use fixed
or floating data types and can be incorporated into someone's C
program in a few minutes with trivial licensing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{srcname}-%{version}

%build
%{set_build_flags}

# Each of the libraries needs to be made separately
for build_type in %{build_types}; do
  mkdir ${build_type}-dynamic
  cd ${build_type}-dynamic
  %cmake .. -DKISSFFT_DATATYPE=${build_type} -DKISSFFT_TEST=ON -DKISSFFT_TOOLS=ON \
  -DKISSFFT_STATIC=OFF -DBUILD_SHARED_LIBS=ON
  %cmake_build
  cd ..
  mkdir ${build_type}-static
  cd ${build_type}-static
  %cmake .. -DKISSFFT_DATATYPE=${build_type} -DKISSFFT_TEST=ON -DKISSFFT_TOOLS=ON \
  -DKISSFFT_STATIC=ON -DBUILD_SHARED_LIBS=OFF
  %cmake_build
  cd ..
done

%install
for build_type in %{build_types}; do
  cd ${build_type}-dynamic
  %cmake_install
  cd ..
  cd ${build_type}-static
  %cmake_install
  cd ..
done

%check
%if %{with tests}
for build_type in %{build_types}; do
  cd ${build_type}-dynamic
  %ctest
  cd ..
  cd ${build_type}-static
  %ctest
  cd ..
done
%endif

%files
%doc README.md TIPS
%license COPYING LICENSES/BSD-3-Clause
%{_libdir}/libkissfft-int16_t.so.%{srcver}*
%{_libdir}/libkissfft-int32_t.so.%{srcver}*
%{_libdir}/libkissfft-float.so.%{srcver}*
%{_libdir}/libkissfft-double.so.%{srcver}*
%{_bindir}/fastconv-int16_t
%{_bindir}/fastconvr-int16_t
%{_bindir}/fft-int16_t
%{_bindir}/psdpng-int16_t
%{_bindir}/fastconv-int32_t
%{_bindir}/fastconvr-int32_t
%{_bindir}/fft-int32_t
%{_bindir}/psdpng-int32_t
%{_bindir}/fastconv-float
%{_bindir}/fastconvr-float
%{_bindir}/fft-float
%{_bindir}/psdpng-float
%{_bindir}/fastconv-double
%{_bindir}/fastconvr-double
%{_bindir}/fft-double
%{_bindir}/psdpng-double

%files static
%{_libdir}/libkissfft-int16_t.a
%{_libdir}/libkissfft-int32_t.a
%{_libdir}/libkissfft-float.a
%{_libdir}/libkissfft-double.a

%files devel
%{_includedir}/%{srcname}
%{_libdir}/libkissfft-int16_t.so
%{_libdir}/libkissfft-int32_t.so
%{_libdir}/libkissfft-float.so
%{_libdir}/libkissfft-double.so
%{_libdir}/cmake/%{srcname}
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
