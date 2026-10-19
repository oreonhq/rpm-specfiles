%global source0_hash e45e4fd342f04b2e00363bc1b68cc375c1cf36041085d3d59caa7a3b7be43836
Name:           radare2
Summary:        The reverse engineering framework
Version:        6.2.2
URL:            https://radare.org/
%global         vcsurl          https://github.com/radareorg/radare2
VCS:            git:%{vcsurl}
%bcond_without     releasetag
%global         gituser         radareorg
%global         gitname         radare2
%global         gitdate         20241119
%global         commit          4eb49d5ad8c99eaecc8850a2f10bad407067c898
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%if %{with releasetag}
Release:        1%{?dist}
Source0:        %{vcsurl}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        1%{?dist}
%endif
Patch1:         radare2-5.6.6-use_openssl.patch
Patch3:         radare2-5.9.0-use_magic.patch
Patch7:           radare2-5.9.8-dec99.patch
Patch8:           https://github.com/radareorg/radare2/pull/23969.patch#/radare2-5.9.8-zlib-cve.patch
Patch9:           https://github.com/radareorg/radare2/pull/23981.patch#/radare2-5.9.8-magic-cve.patch
Patch10:           https://github.com/radareorg/radare2/commit/984ad6ae4ebbc3a01cf1209e05377b5d1d6221f4.patch#/radare2-5.9.8-hfs-cve.patch
License:        LGPL-3.0-or-later AND GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND MIT AND Apache-2.0 AND MPL-2.0 AND Zlib
Requires:       %{name}-common = %{version}-%{release}
Provides:       bundled(spp) = 1.2.0
Provides:       bundled(sdb) = 1.8.6
Provides:       bundled(js0n) = 2018
Provides:       bundled(openbsdregex) = 1.11
Provides:       bundled(tcc) = 0.9.26
Provides:       bundled(binutils) = 2.13
Provides:       bundled(vavrdisasm) = 1.6
Provides:       bundled(grub2) = 1.99~beta0
Provides:       bundled(ptrace-wrap) = 20181018
Provides:       bundled(tree-sitter) = 0.17.2
Provides:       bundled(mpc) = 0.8.7
Provides:       bundled(yxml) = 20201108
Provides:       bundled(quickjs-ng) = 0.7.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  sed
# /oreon:deps
%description
The radare2 is a reverse-engineering framework that is multi-architecture,
multi-platform, and highly scriptable.  Radare2 provides a hexadecimal
editor, wrapped I/O, file system support, debugger support, diffing
between two functions or binaries, and code analysis at opcode,
basic block, and function levels.

%package devel
Summary:        Development files for the radare2 package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       file-devel
Requires:       openssl-devel
%description devel
Development files for the radare2 package. See radare2 package for more
information.

%package common
Summary:        Arch-independent SDB files for the radare2 package
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description common
Arch-independent SDB files used by radare2 package. See radare2 package for more
information

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with releasetag}
# Build from git release version
%autosetup -p 1 -n %{gitname}-%{version}
%else
# Build from git commit
%autosetup -p 1 -n %{gitname}-%{commit}
# Rename internal "version-git" to "version"
sed -i -e "s|%{version}-git|%{version}|g;" configure configure.acr
%endif
# Removing zip/lzip files because we use system dependencies
# version of libzip on rhel7 is too old, use the embedded one instead

# Remove lx4 files because we use system dependencies
rm -rf shlr/lz4/{deps.mk,LICENSE,lz4.*,Makefile,README.md}
# Remove xxhash files because we use system dependencies
rm -f libr/hash/xxhash.c libr/hash/xxhash.h
# Remove magic files because we use system dependencies
awk 'BEGIN {p=1} /#if USE_LIB_MAGIC/ {p=2; next} p==2 && /#else/ {p=0} p>0 {print}' libr/magic/magic.c > libr/magic/magic.c.stripped
awk 'BEGIN {p=1} /#if !USE_LIB_MAGIC/ {p=0; next} p==2 && /#else/ {p=0} p>0 {print}' libr/magic/ascmagic.c > libr/magic/ascmagic.c.stripped
rm -rf libr/magic/*.c
mv libr/magic/magic.c.stripped libr/magic/magic-libmagic.c
mv libr/magic/ascmagic.c.stripped libr/magic/ascmagic-libmagic.c
# Remove openssl files because we use system dependencies
# rm -f libr/hash/{md4,md5,sha1,sha2}.[ch]

# Webui contains pre-build and/or minimized versions of JS libraries without source code
# Consider installing the web-interface from https://github.com/radare/radare2-webui
rm -rf ./shlr/www/*
echo "The radare2 source usually comes with a pre-built version of the web-interface, but without the source code." > ./shlr/www/README.Fedora
echo "This has been removed in the Fedora package to follow the Fedora Packaging Guidelines." >> ./shlr/www/README.Fedora
echo "Available under https://github.com/radare/radare2-webui" >> ./shlr/www/README.Fedora

# On RHEL8 the shabeng for "/usr/bin/env -S" is mangled wrongly as "/usr/bin/-S"
sed -i -e "s|/usr/bin/env -S r2|/usr/bin/r2|" ./scripts/licenses.r2.js

%build

%meson \
    -Duse_sys_magic=true \
    -Duse_sys_zip=false \
    -Duse_sys_zlib=true \
    -Duse_sys_lz4=true \
    -Duse_sys_xxhash=true \
    -Duse_ssl=true \
    -Duse_libuv=true \
%ifarch s390x
    -Ddebugger=false \
%endif
    -Duse_sys_capstone=true \
    -Denable_tests=false \
    -Denable_r2r=false \
    -Dwant_threads=false     # multithreading doesn't work well with Iaito package
%meson_build
%install
%meson_install
mkdir -p %{buildroot}/%{_datadir}/%{name}/%{version}/www
cp ./shlr/www/README.Fedora %{buildroot}/%{_datadir}/%{name}/%{version}/www/README.Fedora
rm %{buildroot}/%{_datadir}/doc/%{name}/fortunes.fun
mkdir -p %{buildroot}%{_libdir}/%{name}/%{version}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n radare2-devel -f %{oreon_filedir}/radare2-devel.list
%files -n radare2-common -f %{oreon_filedir}/radare2-common.list

%changelog

%autochangelog
