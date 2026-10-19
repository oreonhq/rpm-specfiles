%global source0_hash 7ac1cd7daca7afdda742e15478b1f747fc1f813e496fee71839d1e109e543dca
Name:           rizin
Summary:        UNIX-like reverse engineering framework and command-line tool-set
Version:        0.9.1
Release:        1%{?dist}
URL:            https://rizin.re/
VCS:            https://github.com/rizinorg/rizin
%global         gituser         rizinorg
%global         gitname         rizin
%global         shortversion    %(c=%{version}; echo ${c} | cut -d'.' -f-2)
Source0:        https://github.com/%{gituser}/%{name}/releases/download/v%{version}/%{name}-src-v%{version}.tar.xz
License:        LGPL-3.0-or-later AND GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND MIT AND Apache-2.0 AND MPL-2.0 AND Zlib
Requires:       %{name}-common = %{version}-%{release}
Provides:       bundled(spp) = 1.2.0
Provides:       bundled(sdb) = db7edd4a96a89b6749b677a85d7fa4ee2c6fbbb9
Provides:       bundled(openbsdregex) = 1.11
Provides:       bundled(binutils) = 2.13
Provides:       bundled(vavrdisasm) = 1.6
Provides:       bundled(blake3) = 1.3.1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libmspack)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tree-sitter)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-pyyaml
# /oreon:deps
%description
Rizin is a free and open-source Reverse Engineering framework, providing a
complete binary analysis experience with features like Disassembler,
Hexadecimal editor, Emulation, Binary inspection, Debugger, and more.

Rizin is a fork of radare2 with a focus on usability, working features and code
cleanliness.

%package devel
Summary:        Development files for the rizin package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       file-devel
Requires:       openssl-devel
%description devel
Development files for the rizin package. See rizin package for more
information.

%package common
Summary:        Arch-independent SDB files for the rizin package
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description common
Arch-independent SDB files used by rizin package. See rizin package for more
information

%prep

# Build from git release version
%autosetup -n %{gitname}-v%{version}

%build

%meson \
    -Duse_sys_magic=enabled \
    -Duse_sys_libzip=enabled \
    -Duse_sys_zlib=enabled \
    -Duse_sys_lz4=enabled \
    -Duse_sys_xxhash=enabled \
    -Duse_sys_openssl=enabled \
    -Duse_sys_capstone=enabled \
    -Duse_sys_tree_sitter=enabled \
    -Duse_sys_lzma=enabled \
    -Duse_sys_libmspack=enabled \
    -Duse_sys_libzstd=enabled \
%ifarch s390x
    -Ddebugger=false \
%endif
    -Denable_tests=false \
    -Denable_rz_test=false \
    -Dlocal=disabled \
    -Dpackager="Fedora" \
    -Dpackager_version="%{version}-%{release}"
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n rizin-devel -f %{oreon_filedir}/rizin-devel.list
%files -n rizin-common -f %{oreon_filedir}/rizin-common.list

%changelog

%autochangelog
