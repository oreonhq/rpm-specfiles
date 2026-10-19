%global source0_hash 337f4c703ba31902565faad1cd450cf0312ad5a48dc499661277f287b662b09a
Name:           lv2-eq10q
Version:        2.2
Release:        1%{?dist}
Summary:        LV2 audio plugin suite
License:        GPL-2.0-or-later
URL:            https://eq10q.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/eq10q/eq10q-%{version}.tar.gz
Patch:          lv2-eq10q-2.2-path-and-flags.patch
Patch:          lv2-eq10q-2.2-exp10.patch
Patch:          lv2-eq10q-2.2-cmake-3.5.patch
Patch:          lv2-eq10q-2.2-typefix.patch
Requires:       lv2%{?_isa}
Obsoletes:      lv2-EQ10Q-plugins < 2.2.1
Provides:       lv2-EQ10Q-plugins = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  lv2-devel
BuildRequires:  pkgconfig(gtkmm-2.4)
# /oreon:deps
%description
EQ10Q is an audio plugin bundle using the LV2 standard which implements
powerful and flexible parametric equalizers, compressors, a harmonic enhancer
for bass frequencies and mid/side encoders/decoders.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n eq10q-%{version}

# Get rid of warnings about spurious exec permissions in debuginfo package
find . -type f -perm /0111 -exec chmod -v a-x '{}' '+'

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags
sed -i -e 's|-msse -mfpmath=sse||g' -e 's|-O3||g' CMakeLists.txt

%build

%cmake -DCMAKE_INSTALL_PREFIX="%{_libdir}/lv2"
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
