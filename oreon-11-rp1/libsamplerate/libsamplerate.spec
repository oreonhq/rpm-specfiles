%global source0_hash 3258da280511d24b49d6b08615bbe824d0cacc9842b0e4caf11c52cf2b043893
Summary:        Sample rate conversion library for audio data
Name:		libsamplerate
Version:	0.2.2
Release:        12%{?dist}
License:	BSD-2-Clause
URL:		https://libsndfile.github.io/libsamplerate/
Source0:        https://github.com/libsndfile/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.

%package devel
Summary:	Development related files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
%description devel
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.
This package contains development files for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-dependency-tracking --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%set_build_flags
export LD_LIBRARY_PATH=`pwd`/src/.libs
%make_build check
unset LD_LIBRARY_PATH
%files -f %{oreon_filedir}/main.list
%files -n libsamplerate-devel -f %{oreon_filedir}/libsamplerate-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.2-12
- Prepare for Oreon 11 (RP1)
