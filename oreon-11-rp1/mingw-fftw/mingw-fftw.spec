%global source0_hash 6113262f6e92c5bd474f2875fa1b01054c4ad5040f6b0da7c03c98821d9ae303

%{?mingw_package_header}

%global mingw_pkg_name fftw
%global openmp 0

Name:           mingw-%{mingw_pkg_name}
Version:        3.3.8
Release:        20%{?dist}
Summary:        MinGW Fast Fourier Transform library
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.fftw.org
Source0:        http://www.fftw.org/fftw-%{version}.tar.gz

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-gfortran
BuildRequires:  mingw64-gcc-gfortran
BuildArch:      noarch

%description
This package contains the MinGW windows port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:                %{summary}

%description -n mingw32-%{mingw_pkg_name}
This package contains the MinGW win32 port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains cross-compiled libraries and development tools
for Windows.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:                %{summary}

%description -n mingw32-%{mingw_pkg_name}-static
This package contains the MinGW win32 port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains static cross-compiled library

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:                %{summary}

%description -n mingw64-%{mingw_pkg_name}
This package contains the MinGW win64 port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains cross-compiled libraries and development tools
for Windows.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:                %{summary}

%description -n mingw64-%{mingw_pkg_name}-static
This package contains the MinGW win64 port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains static cross-compiled library

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{mingw_pkg_name}-%{version}

%build

BASEFLAGS="--enable-shared --disable-dependency-tracking --disable-threads"
%if %{openmp}
BASEFLAGS="$BASEFLAGS --enable-openmp"
%endif

# Precisions to build
prec_name[0]=single
prec_name[1]=double
prec_name[2]=long
prec_name[3]=quad

# Corresponding flags
prec_flags[0]=--enable-single
prec_flags[1]=--enable-double
prec_flags[2]=--enable-long-double
prec_flags[3]=--enable-quad-precision

# Loop over precisions
for((iprec=0;iprec<4;iprec++))
do
  export MINGW_BUILDDIR_SUFFIX=${prec_name[iprec]}
  export MINGW_CONFIGURE_ARGS="${BASEFLAGS} ${prec_flags[iprec]}"
  %mingw_configure 
  %mingw_make %{?_smp_mflags}
done

%install
# Precisions to build
prec_name[0]=single
prec_name[1]=double
prec_name[2]=long
prec_name[3]=quad

rm -rf %{buildroot}
for((iprec=0;iprec<4;iprec++))
do
  export MINGW_BUILDDIR_SUFFIX=${prec_name[iprec]}
 %mingw_make install DESTDIR=%{buildroot}
done
rm -f %{buildroot}%{mingw32_infodir}/dir
rm -f %{buildroot}%{mingw64_infodir}/dir
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la

rm -f %{buildroot}%{mingw32_bindir}/fftw*-wisdom*
rm -f %{buildroot}%{mingw64_bindir}/fftw*-wisdom*
rm -rf %{buildroot}%{mingw32_infodir}
rm -rf %{buildroot}%{mingw64_infodir}
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

%files -n mingw32-%{mingw_pkg_name}
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{mingw32_bindir}/libfftw3f-3.dll
%{mingw32_bindir}/libfftw3-3.dll
%{mingw32_bindir}/libfftw3l-3.dll
%{mingw32_libdir}/libfftw3f.dll.a
%{mingw32_libdir}/libfftw3.dll.a
%{mingw32_libdir}/libfftw3l.dll.a
%if %{openmp}
%{mingw32_bindir}/libfftw3f_omp-3.dll
%{mingw32_bindir}/libfftw3_omp-3.dll
%{mingw32_bindir}/libfftw3l_omp-3.dll
%{mingw32_libdir}/libfftw3f_omp.dll.a
%{mingw32_libdir}/libfftw3_omp.dll.a
%{mingw32_libdir}/libfftw3l_omp.dll.a
%endif
%{mingw32_includedir}/fftw3*
%{mingw32_libdir}/pkgconfig/fftw3f.pc
%{mingw32_libdir}/pkgconfig/fftw3.pc
%{mingw32_libdir}/pkgconfig/fftw3l.pc
%{mingw32_libdir}/pkgconfig/fftw3q.pc
%dir %{mingw32_libdir}/cmake/fftw3
%{mingw32_libdir}/cmake/fftw3/FFTW3Config.cmake
%{mingw32_libdir}/cmake/fftw3/FFTW3ConfigVersion.cmake
%{mingw32_libdir}/cmake/fftw3/FFTW3fConfig.cmake
%{mingw32_libdir}/cmake/fftw3/FFTW3fConfigVersion.cmake
%{mingw32_libdir}/cmake/fftw3/FFTW3lConfig.cmake
%{mingw32_libdir}/cmake/fftw3/FFTW3lConfigVersion.cmake
%{mingw32_libdir}/cmake/fftw3/FFTW3qConfig.cmake
%{mingw32_libdir}/cmake/fftw3/FFTW3qConfigVersion.cmake

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libfftw3f.a
%{mingw32_libdir}/libfftw3.a
%{mingw32_libdir}/libfftw3l.a
%{mingw32_libdir}/libfftw3q.a

%files -n mingw64-%{mingw_pkg_name}
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{mingw64_bindir}/libfftw3f-3.dll
%{mingw64_bindir}/libfftw3-3.dll
%{mingw64_bindir}/libfftw3l-3.dll
%{mingw64_libdir}/libfftw3f.dll.a
%{mingw64_libdir}/libfftw3.dll.a
%{mingw64_libdir}/libfftw3l.dll.a
%if %{openmp}
%{mingw64_bindir}/libfftw3f_omp-3.dll
%{mingw64_bindir}/libfftw3_omp-3.dll
%{mingw64_bindir}/libfftw3l_omp-3.dll
%{mingw64_libdir}/libfftw3f_omp.dll.a
%{mingw64_libdir}/libfftw3_omp.dll.a
%{mingw64_libdir}/libfftw3l_omp.dll.a
%endif
%{mingw64_includedir}/fftw3*
%{mingw64_libdir}/pkgconfig/fftw3f.pc
%{mingw64_libdir}/pkgconfig/fftw3.pc
%{mingw64_libdir}/pkgconfig/fftw3l.pc
%{mingw64_libdir}/pkgconfig/fftw3q.pc
%dir %{mingw64_libdir}/cmake/fftw3
%{mingw64_libdir}/cmake/fftw3/FFTW3Config.cmake
%{mingw64_libdir}/cmake/fftw3/FFTW3ConfigVersion.cmake
%{mingw64_libdir}/cmake/fftw3/FFTW3fConfig.cmake
%{mingw64_libdir}/cmake/fftw3/FFTW3fConfigVersion.cmake
%{mingw64_libdir}/cmake/fftw3/FFTW3lConfig.cmake
%{mingw64_libdir}/cmake/fftw3/FFTW3lConfigVersion.cmake
%{mingw64_libdir}/cmake/fftw3/FFTW3qConfig.cmake
%{mingw64_libdir}/cmake/fftw3/FFTW3qConfigVersion.cmake

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libfftw3f.a
%{mingw64_libdir}/libfftw3.a
%{mingw64_libdir}/libfftw3l.a
%{mingw64_libdir}/libfftw3q.a

%changelog
%autochangelog
