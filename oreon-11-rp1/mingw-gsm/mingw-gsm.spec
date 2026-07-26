%global source0_hash 725a3768a1e23ab8648b4df9d470aed38eb1635af3cbc8d0b64fef077236f4ce

%{?mingw_package_header}

# Breaks build as native ldflags end up in the cross command line
%undefine _auto_set_build_flags

Name:           mingw-gsm
Version:        1.0.16
Release:        20%{?dist}
Summary:        Shared libraries for GSM speech compressor

License:        MIT
URL:            http://www.quut.com/gsm/
Source:         http://www.quut.com/gsm/gsm-%{version}.tar.gz
# patches from gsm package
Patch1:         gsm-warnings.patch
Patch2:         gsm-64bit.patch
# patch for MinGW (build dll, .exe suffix)
# (stdin/out in tools not supported for now)
Patch3:         gsm-mingw.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc

%global srcver 1.0-pl16

%description
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 162 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

%package -n mingw32-gsm
Summary:        %{summary}

%description -n mingw32-gsm
Contains runtime shared libraries, header files, and development libraries for
libgsm, an implementation of the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP (residual
pulse excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 162 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

This package is MinGW compiled gsm library for the Win32 target.

%package -n mingw32-gsm-tools
Summary:        GSM speech compressor tools
Requires:       mingw32-gsm = %{version}-%{release}

%description -n mingw32-gsm-tools
Contains command line utilities for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

This package are MinGW compiled gsm tools for the Win32 target.

%package -n mingw64-gsm
Summary:        %{summary}

%description -n mingw64-gsm
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 162 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

This package is MinGW compiled gsm library for the Win64 target.

%package -n mingw64-gsm-tools
Summary:        Tools for Free Lossless Audio Codec
Requires:       mingw64-gsm = %{version}-%{release}

%description -n mingw64-gsm-tools
Contains command line utilities for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

This package are MinGW compiled gsm tools for the Win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
pushd gsm-%{srcver}
%patch -P1 -p1 -b .warn
%patch -P2 -p1 -b .64bit
%patch -P3 -p1
popd

%build
cp -a gsm-%{srcver} build_win32
cp -a gsm-%{srcver} build_win64

pushd build_win32
make %{?_smp_mflags} all \
  CC=%mingw32_cc \
  AR=%mingw32_ar \
  RANLIB=%mingw32_ranlib \
  RPM_CFLAGS="%{mingw32_cflags}" \
  RPM_LDFLAGS="%{mingw32_ldflags}"
popd

pushd build_win64
make %{?_smp_mflags} all \
  CC=%mingw64_cc \
  AR=%mingw64_ar \
  RANLIB=%mingw64_ranlib \
  RPM_CFLAGS="%{mingw64_cflags}" \
  RPM_LDFLAGS="%{mingw64_ldflags}"
popd

%install
pushd build_win32
mkdir -p \
  %{buildroot}%{mingw32_bindir} \
  %{buildroot}%{mingw32_mandir}/man1 \
  %{buildroot}%{mingw32_mandir}/man3 \
  %{buildroot}%{mingw32_includedir}/gsm \
  %{buildroot}%{mingw32_libdir}

make install \
  CC=%mingw32_cc \
  AR=%mingw32_ar \
  RANLIB=%mingw32_ranlib \
  INSTALL_ROOT=%{buildroot}%{mingw32_prefix} \
  GSM_INSTALL_BIN=%{buildroot}%{mingw32_bindir} \
  GSM_INSTALL_INC=%{buildroot}%{mingw32_includedir}/gsm \
  GSM_INSTALL_LIB=%{buildroot}%{mingw32_libdir} \
  GSM_INSTALL_MAN=%{buildroot}%{mingw32_mandir}/man3 \
  TOAST_INSTALL_BIN=%{buildroot}%{mingw32_bindir} \
  TOAST_INSTALL_MAN=%{buildroot}%{mingw32_mandir}/man1

# some apps look for this in /usr/include
ln -s gsm/gsm.h %{buildroot}%{mingw32_includedir}
popd

pushd build_win64
mkdir -p \
  %{buildroot}%{mingw64_bindir} \
  %{buildroot}%{mingw64_mandir}/man1 \
  %{buildroot}%{mingw64_mandir}/man3 \
  %{buildroot}%{mingw64_includedir}/gsm \
  %{buildroot}%{mingw64_libdir}

make install \
  CC=%mingw64_cc \
  AR=%mingw64_ar \
  RANLIB=%mingw64_ranlib \
  INSTALL_ROOT=%{buildroot}%{mingw64_prefix} \
  GSM_INSTALL_BIN=%{buildroot}%{mingw64_bindir} \
  GSM_INSTALL_INC=%{buildroot}%{mingw64_includedir}/gsm \
  GSM_INSTALL_LIB=%{buildroot}%{mingw64_libdir} \
  GSM_INSTALL_MAN=%{buildroot}%{mingw64_mandir}/man3 \
  TOAST_INSTALL_BIN=%{buildroot}%{mingw64_bindir} \
  TOAST_INSTALL_MAN=%{buildroot}%{mingw64_mandir}/man1

# some apps look for this in /usr/include
ln -s gsm/gsm.h %{buildroot}%{mingw64_includedir}
popd

%files -n mingw32-gsm
%license gsm-%{srcver}/COPYRIGHT
%doc gsm-%{srcver}/ChangeLog
%doc gsm-%{srcver}/README
%dir %{mingw32_includedir}/gsm
%exclude %{mingw32_mandir}
%exclude %{mingw32_libdir}/libgsm.a
%{mingw32_bindir}/libgsm-1.dll
%{mingw32_libdir}/libgsm.dll.a
%{mingw32_includedir}/gsm.h
%{mingw32_includedir}/gsm/gsm.h

%files -n mingw32-gsm-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-gsm
%license gsm-%{srcver}/COPYRIGHT
%doc gsm-%{srcver}/ChangeLog
%doc gsm-%{srcver}/README
%dir %{mingw64_includedir}/gsm
%exclude %{mingw64_mandir}
%exclude %{mingw64_libdir}/libgsm.a
%{mingw64_bindir}/libgsm-1.dll
%{mingw64_libdir}/libgsm.dll.a
%{mingw64_includedir}/gsm.h
%{mingw64_includedir}/gsm/gsm.h

%files -n mingw64-gsm-tools
%{mingw64_bindir}/*.exe

%changelog
%autochangelog
