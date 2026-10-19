%global source0_hash a3c40c6471928383f4abfcb2e8f24012a1f562be2f17b8d672145d5986681a92
%global ver_major 1
%global ver_minor 0
%global ver_patch 24
Name:           gsm
Version:        1.0.24
Release:        1%{?dist}
Summary:        Shared libraries for GSM speech compressor
License:        tu-berlin-2.0
URL:            https://www.quut.com/gsm/
Source0:        https://www.quut.com/gsm/%{name}-%{version}.tar.gz
Patch0:         %{name}-makefile.patch
Patch1:         %{name}-warnings.patch
%global srcver %{ver_major}.%{ver_minor}-pl%{ver_patch}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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

%package        tools
Summary:        GSM speech compressor tools
Requires:       %{name}%{_isa} = %{version}-%{release}
%description    tools
Contains command line utilities for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

%package        devel
Summary:        Header files and development libraries for libgsm
Requires:       %{name}%{_isa} = %{version}-%{release}
%description    devel
Contains header files and development libraries for libgsm, an
implementation of the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
(residual pulse excitation/long term prediction) coding at 13 kbit/s.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -n gsm-%{srcver} -q
%patch -P0 -p1 -b .mk
%patch -P1 -p1 -b .warn

%build

export LDFLAGS="%{?__global_ldflags}"
%make_build all SO_MAJOR=%{ver_major} SO_MINOR=%{ver_minor} SO_PATCH=%{ver_patch}
%install
export LDFLAGS="%{?__global_ldflags}"
mkdir -p %{buildroot}{%{_bindir},%{_includedir}/gsm,%{_libdir},%{_mandir}/{man1,man3}}
%make_install \
	INSTALL_ROOT=%{buildroot}%{_prefix} \
	GSM_INSTALL_INC=%{buildroot}%{_includedir}/gsm \
	GSM_INSTALL_LIB=%{buildroot}%{_libdir} \
	SO_MAJOR=%{ver_major} SO_MINOR=%{ver_minor} SO_PATCH=%{ver_patch}
ln -s gsm/gsm.h %{buildroot}%{_includedir}
echo ".so toast.1" > %{buildroot}%{_mandir}/man1/tcat.1
echo ".so toast.1" > %{buildroot}%{_mandir}/man1/untoast.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

[ -f %{buildroot}%{_libdir}/libgsm.so.%{version} ]
export LDFLAGS="%{?__global_ldflags}"
%{__make} addtst
%files -f %{oreon_filedir}/main.list
%files -n gsm-tools -f %{oreon_filedir}/gsm-tools.list
%files -n gsm-devel -f %{oreon_filedir}/gsm-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.24-1
- Prepare for Oreon 11 (RP1)
