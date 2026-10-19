%global source0_hash 81f8c462f46bc8901618762ae34cf9de93894ff81f41db73c79472fa3baef875
Name:           mt32emu
Version:        2_8_3
Release:        1%{?dist}
Summary:        C/C++ library for emulating Roland MT-32, CM-32L and LAPC-I synthesizer modules
%global version_ %(v=%{version}; tr . _ <<< $v)
License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://munt.sourceforge.net/
Source0:        https://github.com/munt/munt/archive/refs/tags/lib%{name}_%{version}.tar.gz
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
mt32emu is a part of the Munt project. It represents a C/C++ library named
libmt32emu which allows to emulate (approximately) the Roland MT-32, CM-32L and
LAPC-I synthesizer modules.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconf-pkg-config
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n munt-lib%{name}_%{version_}
# Remove other subprojects than mt32emu
rm -rf DOSBox-mt32-patch FreeBSD mt32emu_{alsadrv,smf2wav,qt,win32drv{,_setup}}

%build

%cmake \
    -Dmunt_WITH_MT32EMU_SMF2WAV=FALSE \
    -Dmunt_WITH_MT32EMU_QT=FALSE \
    -Dlibmt32emu_WITH_VERSION_TAGGING=TRUE \
    -Dlibmt32emu_WITH_SYMBOL_VERSIONING=TRUE
%cmake_build
%install
%cmake_install
rm %{buildroot}/%{_docdir}/munt/lib%{name}/COPYING.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n mt32emu-devel -f %{oreon_filedir}/mt32emu-devel.list

%changelog

%autochangelog
