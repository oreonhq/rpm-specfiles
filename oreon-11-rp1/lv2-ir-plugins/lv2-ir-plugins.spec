%global source0_hash 3d5e7f4b2ad53e2f88d949dd74e5189bc3d88261c9969e1d2a3cd1dc583a6532

Name:           lv2-ir-plugins
Version:        1.3.4
Release:        22%{?dist}
Summary:        LV2 Plugin: low-latency, real-time, high performance signal convolver

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://tomszilagyi.github.io/plugins/ir.lv2/
Source0:        https://github.com/tomszilagyi/ir.lv2/archive/%{version}.tar.gz#/ir.lv2-%{version}.tar.gz

# This patch modifies the realtime priority as reported in the source
# Priority should match -P parameter passed to jackd, which defaults to 20
Patch0:         %{name}-realtime-priority.patch
# Fix FTBFS with recent LV2
# Patch sent upstream https://github.com/tomszilagyi/ir.lv2/pull/24
Patch1:         %{name}-lv2.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  zita-convolver-devel >= 3.1
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  gtk2-devel >= 2.20
BuildRequires:  fftw-devel

Requires:       lv2 >= 1.8.1

%description
IR is a low-latency, real time, high performance signal
convolver especially for creating reverb effects. Supports impulse
responses with 1, 2 or 4 channels, in any sound file format supported
by libsndfile.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n ir.lv2-%{version}

# Delete old LV2 include file just to be safe
rm lv2_ui.h

%build
export CPPFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build INSTDIR="%{_libdir}/lv2"

%install
%make_install INSTDIR="%{buildroot}%{_libdir}/lv2"

%files
%doc README.md ChangeLog
%license COPYING
%{_libdir}/lv2/ir.lv2/

%changelog
%autochangelog
