%global source0_hash 009b0f50a952ea501f95bb6b15292f81b319fe4534f95ca6c89d48ae296df3b4

Name:           sndfile-tools
Version:        1.5
Release:        14%{?dist}
Summary:        A collection of programs to do interesting things with sound files

# The entire source is (GPLv2 or GPLv3) except src/jackplay.c, which is
# GPLv2+, and src/resample.c, which is BSD.
# Automatically converted from old format: (GPLv2 or GPLv3) and GPLv2+ and BSD - review is highly recommended.
License:        (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://github.com/libsndfile/%{name}
Source0:        https://github.com/libsndfile/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Missing man page
Source1:        https://raw.githubusercontent.com/libsndfile/%{name}/master/man/sndfile-waveform.1

# Patches from upstream
Patch0:         0001-Zero-initialize-sfinfo-in-resample.c-to-fix-Valgrind.patch
Patch1:         0002-Zero-initialize-SF_INFO-structures-everywhere-else-t.patch
Patch2:         0003-Fix-a-leaked-cairo-context-in-render_to_surface-in-w.patch
Patch3:         0001-Fix-76-in-which-Valgrind-reports-a-leaked-FontConfig.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(fftw3) >= 0.15.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jack)
BuildRequires:  valgrind

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

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# Install missing man page for sndfile-waveform
# Fixed upstream https://github.com/libsndfile/sndfile-tools/commit/9dbeefc470a3391afd3a64cc7f80a45f43f35a13
install -p -m 644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/

%check
result="$(./tests/test-wrapper.sh)"
if echo "${result}" | grep -Ev ': ok$' >/dev/null
then
  exit 1
fi

%files
%license COPYING
%doc README AUTHORS
%{_bindir}/*
%{_pkgdocdir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
