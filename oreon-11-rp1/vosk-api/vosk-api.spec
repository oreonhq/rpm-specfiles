%global source1_hash f47a996af546884a8e1cb961323b796c5c238c1bbeabaf657bb300b760e431b2
%global source0_hash cc1067bcc599c9a2f5f38d4257caf2ac636ba244f7c965cee20293a41024f70f
%global debug_package %{nil}
%global kaldi_commit 93ef0019b847272a239fbb485ef97f29feb1d587 
Name:           vosk-api
Version:        0.3.50
Release:        3%{?dist}
Summary:        Offline speech recognition toolkit
ExclusiveArch:  x86_64 aarch64 ppc64le
License:        Apache-2.0
URL:            https://alphacephei.com/vosk
Source0:        https://github.com/alphacep/vosk-api/archive/v%{version}/vosk-api-%{version}.tar.gz
Source1:        https://github.com/alphacep/kaldi/archive/%{kaldi_commit}.tar.gz
Patch0: kaldi-fst.patch
Patch1: kaldi-lapack.patch
Patch2: kaldi-openblas.patch
Patch3: vosk-lapack.patch
Patch4: vosk-lib_fst.patch
# oreon:deps
BuildRequires:  blas-devel
BuildRequires:  blas-static
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  lapack-static
BuildRequires:  make
BuildRequires:  openblas-devel
BuildRequires:  openblas-static
BuildRequires:  openfst-devel
BuildRequires:  openfst-tools
BuildRequires:  unzip
# /oreon:deps
%description
Vosk is an offline open source speech recognition toolkit.

%package devel
Summary: Development libraries of vosk-api
%description devel
The vosk-api-devel package contains the header and shared library 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a1
tar -xzf %{SOURCE1}

# Move and setup Kaldi
mv kaldi-%{kaldi_commit} kaldi

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

cd kaldi/tools
mkdir -p OpenBLAS/install/lib
ln -sf %{_includedir}/openblas OpenBLAS/install/include
ln -sf %{_libdir}/* OpenBLAS/install/lib
mkdir -p openfst/include openfst/lib
ln -sf %{_includedir}/fst openfst/include
ln -sf %{_libdir}/* openfst/lib

%build

cd kaldi/src
./configure --mathlib=OPENBLAS_NO_F2C --shared --use-cuda=no
%make_build online2 lm rnnlm
cd %{_builddir}/vosk-api-%{version}/src
%make_build KALDI_ROOT=../kaldi HAVE_OPENBLAS_NO_F2C=1 HAVE_OPENBLAS_CLAPACK=0
%install
install -Dpm 644 %{_builddir}/vosk-api-%{version}/src/vosk_api.h %{buildroot}%{_includedir}/vosk_api.h
install -Dpm 755 %{_builddir}/vosk-api-%{version}/src/libvosk.so %{buildroot}%{_libdir}/libvosk.so
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n vosk-api-devel -f %{oreon_filedir}/vosk-api-devel.list

%changelog

%autochangelog
