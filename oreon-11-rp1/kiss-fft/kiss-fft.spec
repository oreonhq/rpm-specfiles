%global source0_hash 205a8f6a448ef12b091f8ac6a514b5091bb5f6b0b543431ed75f673116cf5cbf
%global srcname kissfft
%global srcver 131
%global build_types %{?build_types} float
%global build_types %{?build_types} double
%global build_types %{?build_types} int16_t
%global build_types %{?build_types} int32_t
%bcond_with     tests
Summary:        A Fast Fourier Transform (FFT) library that tries to Keep it Simple, Stupid
Name:           kiss-fft
License:        BSD-3-Clause
Version:        %{srcver}.2.0
Release:        1%{?dist}
URL:            https://github.com/mborgerding/%{srcname}
Source0:        https://github.com/mborgerding/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         %{name}-integer-overflow.patch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  python3
BuildRequires:  python3-numpy
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

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
%files -f %{oreon_filedir}/main.list
%files -n kiss-fft-static -f %{oreon_filedir}/kiss-fft-static.list
%files -n kiss-fft-devel -f %{oreon_filedir}/kiss-fft-devel.list

%changelog

%autochangelog
