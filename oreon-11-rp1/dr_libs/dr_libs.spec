%global source0_hash b56be5930399b9ea81591a837e0c9ee959a5d57e90dac96e0af37dde1fa0bb7e
%global commit fa931f3285ced10ace628f7f1ac951e1951e7ea6
%global snapdate 20260302
Name:           dr_libs
%global snapinfo %{snapdate}.%{sub %{commit} 1 7}
Version:        0^%{snapinfo}
Release:        1%{?dist}
Summary:        Single-file audio decoding libraries for C/C++
URL:            https://github.com/mackron/dr_libs
License:        Unlicense OR MIT-0
%global dr_flac_version 0.13.3^%{snapinfo}
%global dr_mp3_version 0.7.3^%{snapinfo}
%global dr_wav_version 0.14.5^%{snapinfo}
Source0:        https://github.com/mackron/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
%global debug_package %{nil}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel
BuildRequires:  pkgconfig(flac)
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development files for dr_libs
BuildArch:      noarch
Provides:       dr_libs-static = %{version}-%{release}
Requires:       dr_flac-devel = %{dr_flac_version}-%{release}
Requires:       dr_flac-static = %{dr_flac_version}-%{release}
Requires:       dr_mp3-devel = %{dr_mp3_version}-%{release}
Requires:       dr_mp3-static = %{dr_mp3_version}-%{release}
Requires:       dr_wav-devel = %{dr_wav_version}-%{release}
Requires:       dr_wav-static = %{dr_wav_version}-%{release}
%description devel
The dr_libs-devel package contains libraries and header files for developing
applications that use dr_libs.

This is a metapackage that requires the -devel packages for all dr_libs
libraries.

%package -n dr_flac-devel
Summary:        FLAC audio decoder
Version:        %{dr_flac_version}
BuildArch:      noarch
Provides:       dr_flac-static = %{dr_flac_version}-%{release}
%description -n dr_flac-devel
FLAC audio decoder.

%package -n dr_mp3-devel
Summary:        MP3 audio decoder
Version:        %{dr_mp3_version}
BuildArch:      noarch
Provides:       dr_mp3-static = %{dr_mp3_version}-%{release}
%description -n dr_mp3-devel
MP3 audio decoder. Based off minimp3 (https://github.com/lieff/minimp3).

%package -n dr_wav-devel
Summary:        WAV audio loader and writer
Version:        %{dr_wav_version}
BuildArch:      noarch
Provides:       dr_wav-static = %{dr_wav_version}-%{release}
%description -n dr_wav-devel
WAV audio loader and writer.

%package doc
Summary:        Documentation for dr_libs
BuildArch:      noarch
%description doc
Documentation for dr_libs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dr_libs-%{commit}

# Omit the "playback" tests. We cannot run these anyway, so we would have to
# skip them, and by not even compiling them, we can avoid a BuildRequires on
# miniaudio.
sed -r -i 's/^([[:blank:]]*)(.*_playback)/\1# \2/' CMakeLists.txt

mkdir -p tests/testvectors/mp3/tests

%conf
%cmake -DDR_LIBS_BUILD_TESTS:BOOL=ON

%build

%cmake_build
%install
install -t '%{buildroot}%{_includedir}' -p -m 0644 -D dr_*.h
%oreon_autofiles dr_flac-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dr_mp3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dr_wav-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

skips='^($.'
skips="${skips}|wav_encoding"
skips="${skips}|mp3_(basic|extract)"
skips="${skips})$"
%ctest --exclude-regex "${skips}"
while read -r version header
do
  grep -E "\\bv$(echo "${version}" | sed -r 's/\./\\./g')\\b" \
      "%{buildroot}%{_includedir}/${header}" >/dev/null
done <<'EOF'
%(printf '%s\n' '%{dr_flac_version}' | sed -r 's/[~^].*//') dr_flac.h
%(printf '%s\n' '%{dr_mp3_version}' | sed -r 's/[~^].*//') dr_mp3.h
%(printf '%s\n' '%{dr_wav_version}' | sed -r 's/[~^].*//') dr_wav.h
EOF
%files -f %{oreon_filedir}/main.list
%files -n dr_libs-devel -f %{oreon_filedir}/dr_libs-devel.list
%files -n dr_flac-devel -f %{oreon_filedir}/dr_flac-devel.list
%files -n dr_mp3-devel -f %{oreon_filedir}/dr_mp3-devel.list
%files -n dr_wav-devel -f %{oreon_filedir}/dr_wav-devel.list
%files -n dr_libs-doc -f %{oreon_filedir}/dr_libs-doc.list

%changelog

%autochangelog
