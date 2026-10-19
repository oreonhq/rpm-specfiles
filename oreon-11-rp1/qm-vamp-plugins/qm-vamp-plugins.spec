%global source0_hash 875c5e35247b9e4493e16ff704c5472e13f339f8fb9c59a267595221b8b4c66c
%global blaslib openblas
Name:           qm-vamp-plugins
Version:        1.8.0
Release:        1%{?dist}
Summary:        Vamp audio feature extraction plugin
License:        GPL-2.0-or-later
URL:            https://code.soundsoftware.ac.uk/projects/qm-vamp-plugins
Source0:        https://code.soundsoftware.ac.uk/attachments/download/2624/qm-vamp-plugins-1.8.0.tar.gz
Patch0:         qm-vamp-plugins-build.patch
Patch1:         qm-vamp-plugins-1.8.0-unbundle.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  kiss-fft-static
BuildRequires:  make
BuildRequires:  openblas-devel
BuildRequires:  qm-dsp-static
BuildRequires:  vamp-plugin-sdk-devel
# /oreon:deps
%description
qm-vamp-plugins are vamp audio feature extraction plugins from the Centre for
Digital Music at Queen Mary, University of London,
http://www.elec.qmul.ac.uk/digitalmusic/.

This plugin set includes note onset detector, beat and barline tracker, tempo
estimator, key estimator, tonal change detector, structural segmenter, timbral
and rhythmic similarity, wavelet scaleogram, adaptive spectrogram, note
transcription, chromagram, constant-Q spectrogram, and MFCC plugins.

For more information see
http://vamp-plugins.org/plugin-doc/qm-vamp-plugins.html.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# remove atlas binaries
rm -rf build/linux/amd64 build/linux/i686
cp -p build/linux/Makefile.linux32 Makefile
# remove bundled qm-dsp, also with bundled kiss-fft
rm -rf qm-dsp
%patch -P0 -p1 -b .build
%patch -P1 -p1 -b .unbundle

%build

%ifarch %{ix86}
EXTRA_CFLAGS="-msse -mfpmath=sse"
%endif
%ifarch x86_64
EXTRA_CFLAGS="-msse -msse2 -mfpmath=sse"
%endif
CFLAGS="-I%{_includedir}/qm-dsp $EXTRA_CFLAGS %{?optflags}" \
LDFLAGS="%{?__global_ldflags}" \
BLAS_LIBS="-l%{blaslib}" \
make %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{_libdir}/vamp
install -p -m 0644 qm-vamp-plugins.cat %{buildroot}%{_libdir}/vamp/
install -p -m 0644 qm-vamp-plugins.n3 %{buildroot}%{_libdir}/vamp/
install -p -m 0755 qm-vamp-plugins.so %{buildroot}%{_libdir}/vamp/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
