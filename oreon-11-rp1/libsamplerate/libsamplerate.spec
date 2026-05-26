# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 3258da280511d24b49d6b08615bbe824d0cacc9842b0e4caf11c52cf2b043893
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary:	Sample rate conversion library for audio data
Name:		libsamplerate
Version:	0.2.2
Release:	12%{?dist}
License:	BSD-2-Clause
URL:		https://libsndfile.github.io/libsamplerate/
Source0:	https://github.com/libsndfile/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	alsa-lib-devel
BuildRequires:	fftw-devel >= 0.15.0
BuildRequires:	gcc
BuildRequires:	libsndfile-devel >= 1.0.6
BuildRequires:	pkgconfig
BuildRequires:	make

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
%oreon_verify_sources
%setup -q


%build
%configure --disable-dependency-tracking --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la


%check
%set_build_flags
export LD_LIBRARY_PATH=`pwd`/src/.libs
%make_build check
unset LD_LIBRARY_PATH


%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/samplerate.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/samplerate.pc
%{_pkgdocdir}/*
%exclude %{_pkgdocdir}/AUTHORS
%exclude %{_pkgdocdir}/README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.2-12
- Prepare for Oreon 11 (RP1)
