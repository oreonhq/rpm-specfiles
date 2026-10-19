%global source0_hash 5630c24cdeb33b131612f7eb4b1a9934234754f9f388ff8617458d0be6f239a1
%{?mingw_package_header}
%global mingw_pkg_name fftw
%global openmp 0
Name:           mingw-%{mingw_pkg_name}
Version:        3.3.11
Release:        1%{?dist}
Summary:        MinGW Fast Fourier Transform library
License:        GPL-2.0-or-later
URL:            http://www.fftw.org
Source0:        http://www.fftw.org/fftw-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-gfortran
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-gfortran
# /oreon:deps
%description
This package contains the MinGW windows port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        MinGW Fast Fourier Transform library
%description -n mingw32-%{mingw_pkg_name}
This package contains the MinGW win32 port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains cross-compiled libraries and development tools
for Windows.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:        MinGW Fast Fourier Transform library
%description -n mingw32-%{mingw_pkg_name}-static
This package contains the MinGW win32 port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains static cross-compiled library

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        MinGW Fast Fourier Transform library
%description -n mingw64-%{mingw_pkg_name}
This package contains the MinGW win64 port of the FFTW library.

FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains cross-compiled libraries and development tools
for Windows.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:        MinGW Fast Fourier Transform library
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
prec_name[0]=single
prec_name[1]=double
prec_name[2]=long
prec_name[3]=quad
prec_flags[0]=--enable-single
prec_flags[1]=--enable-double
prec_flags[2]=--enable-long-double
prec_flags[3]=--enable-quad-precision
for((iprec=0;iprec<4;iprec++))
do
  export MINGW_BUILDDIR_SUFFIX=${prec_name[iprec]}
  export MINGW_CONFIGURE_ARGS="${BASEFLAGS} ${prec_flags[iprec]}"
  %mingw_configure 
  %mingw_make %{?_smp_mflags}
done
%install
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-fftw -f %{oreon_filedir}/mingw32-fftw.list
%files -n mingw32-fftw-static -f %{oreon_filedir}/mingw32-fftw-static.list
%files -n mingw64-fftw -f %{oreon_filedir}/mingw64-fftw.list
%files -n mingw64-fftw-static -f %{oreon_filedir}/mingw64-fftw-static.list

%changelog

%autochangelog
