%global source1_hash 9257dafcf15156b40eef32ed2eecfa7492a0f98e919d2940846f18d16ef3564a
%global source0_hash 009b0f50a952ea501f95bb6b15292f81b319fe4534f95ca6c89d48ae296df3b4
Name:           sndfile-tools
Version:        1.5
Release:        1%{?dist}
Summary:        A collection of programs to do interesting things with sound files
License:        (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://github.com/libsndfile/%{name}
Source0:        https://github.com/libsndfile/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source1:        https://raw.githubusercontent.com/libsndfile/%{name}/master/man/sndfile-waveform.1
Patch0:         0001-Zero-initialize-sfinfo-in-resample.c-to-fix-Valgrind.patch
Patch1:         0002-Zero-initialize-SF_INFO-structures-everywhere-else-t.patch
Patch2:         0003-Fix-a-leaked-cairo-context-in-render_to_surface-in-w.patch
Patch3:         0001-Fix-76-in-which-Valgrind-reports-a-leaked-FontConfig.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  valgrind
# /oreon:deps
%description
Sndfile-tools is a small collection of programs that use libsndfile
and other libraries to do useful things.
Included tools are:
sndfile-generate-chirp
sndfile-jackplay
sndfile-mix-to-mono
sndfile-resample
sndfile-spectrogram
sndfile-waveform

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
install -p -m 644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/
%oreon_autofiles main

%check

result="$(./tests/test-wrapper.sh)"
if echo "${result}" | grep -Ev ': ok$' >/dev/null
then
  exit 1
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
