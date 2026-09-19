%global source0_hash f8057fae1c7df8b99116783ef3e94a6a44518d49c72e2e630c24b689c6022630

Name:           fftw2
Version:        2.1.5
Release:        54%{?dist}
Summary:        Fast Fourier Transform library (version 2)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.fftw.org
Source0:        https://www.fftw.org/fftw-%{version}.tar.gz
Patch1:         fftw2-configure.patch
Patch2:         fftw2-texi.patch
BuildRequires:  gcc-gfortran
BuildRequires:  make
%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size. We believe that FFTW, which is free
software, should become the FFT library of choice for most
applications. Our benchmarks, performed on on a variety of platforms,
show that FFTW's performance is typically superior to that of other
publicly available FFT software.

%package        devel
Summary:        Headers, libraries and docs for the FFTW library (version 2)
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains header files and development libraries needed to
develop programs using the FFTW fast Fourier transform library version
2.

%package        static
Summary:        Static version of the FFTW library (version 2)
Requires:       %{name} = %{version}-%{release}

%description    static
This package contains the static linked libraries of the FFTW fast
Fourier transform library (version 2).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -c -n fftw-%{version}
%autopatch -p0
mv fftw-%{version} double
cp -a double single

%build
pushd double
%configure \
    --enable-shared \
%ifarch i386
    --enable-i386-hacks \
%endif
    --enable-threads
%make_build
popd

pushd single
%configure \
    --enable-shared \
    --enable-type-prefix \
    --enable-threads \
    --enable-float
%make_build
popd

%install
pushd double
%make_install
popd

pushd single
%make_install

find %{buildroot} -type f -name "*.la" -delete
rm %{buildroot}%{_infodir}/dir
cp -a doc COPYING AUTHORS COPYRIGHT ChangeLog NEWS README* TODO ..
popd
rm doc/{Makefile*,mdate-sh,stamp-vti,texi2html,texinfo.tex,*.texi,fftw.info*}

%files
%license COPYING
%doc AUTHORS COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/libfftw.so.2*
%{_libdir}/libfftw_threads.so.2*
%{_libdir}/librfftw.so.2*
%{_libdir}/librfftw_threads.so.2*
%{_libdir}/libsfftw.so.2*
%{_libdir}/libsfftw_threads.so.2*
%{_libdir}/libsrfftw.so.2*
%{_libdir}/libsrfftw_threads.so.2*

%files devel
%license COPYING
%doc doc/
%{_includedir}/fftw.h
%{_includedir}/fftw_threads.h
%{_includedir}/rfftw.h
%{_includedir}/rfftw_threads.h
%{_includedir}/sfftw.h
%{_includedir}/sfftw_threads.h
%{_includedir}/srfftw.h
%{_includedir}/srfftw_threads.h
%{_libdir}/libfftw.so
%{_libdir}/libfftw_threads.so
%{_libdir}/librfftw.so
%{_libdir}/librfftw_threads.so
%{_libdir}/libsfftw.so
%{_libdir}/libsfftw_threads.so
%{_libdir}/libsrfftw.so
%{_libdir}/libsrfftw_threads.so
%{_infodir}/fftw.info*

%files static
%license COPYING
%{_libdir}/libfftw.a
%{_libdir}/libfftw_threads.a
%{_libdir}/librfftw.a
%{_libdir}/librfftw_threads.a
%{_libdir}/libsfftw.a
%{_libdir}/libsfftw_threads.a
%{_libdir}/libsrfftw.a
%{_libdir}/libsrfftw_threads.a

%changelog
%autochangelog
