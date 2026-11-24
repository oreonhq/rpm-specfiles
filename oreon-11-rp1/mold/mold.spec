# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1dee837e227b0c3f2661def602ef8ddc0b889ae5b1d28c1ddec5f29e08e5ceb5
%global source1_hash a8e67431172d5bfc61b6704288a94abf941ba6e4860001c9d008cb401ff28ad4
%global source2_hash 3da16118bea951f6a68fca956ef25dbc52605ddcd7070c6fbcfedd39dabfcb20
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond check 0

%ifarch %{ix86}
%global rustflags_debuginfo 1
%endif

Name:           mold
Version:        3.0.0
Release:        %{autorelease}
Summary:        A Modern Linker

%global forgeurl https://github.com/rui314/%{name}
%global tag      v%{version}
%forgemeta

SourceLicense:  MIT
License:        %{shrink:
    MIT AND
    (Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND
    (Apache-2.0 OR MIT) AND
    BSL-1.0 AND
    (MIT OR Apache-2.0) AND
    (MIT-0 OR Apache-2.0) AND
    (Unlicense OR MIT) AND
    Zlib
}
URL:            %{forgeurl}
Source0:        mold-%{version}.tar.gz
Source1:        mold-%{version}-vendor.tar.xz
Source2:        mold-%{version}-Cargo.lock

Patch:          0001-Update-cpp_demangle-to-0.5.1.patch
Patch:          0002-Adjust-dependencies-for-Fedora-Linux.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cargo
BuildRequires:  rustc
BuildRequires:  zlib-devel
BuildRequires:  pkgconf

%if %{with check}
BuildRequires:  binutils-devel
BuildRequires:  gdb
BuildRequires:  glibc-static
%ifarch x86_64
%if 0%{?fedora}
BuildRequires: (glibc32 or glibc-devel(%__isa_name-32))
%endif
%endif
BuildRequires:  libdwarf-tools
BuildRequires:  libstdc++-static
BuildRequires:  llvm
BuildRequires:  perl-interpreter
%endif

Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than the LLVM lld linker.
mold is designed to increase developer productivity by reducing
build time, especially in rapid debug-edit-rebuild cycles.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%autosetup -p1 -n mold-%{version}
cp -f %{SOURCE2} Cargo.lock
tar -xf %{SOURCE1}

%build
export MOLD_LIBDIR="%{_libdir}"
%oreon_cargo_prep vendor
%oreon_cargo_build

%install
DESTDIR="%{buildroot}" PREFIX="%{_prefix}" MOLD_LIBDIR="%{_libdir}" \
  ./install-mold.sh
rm -r "%{buildroot}%{_docdir}/mold"
touch %{buildroot}%{_bindir}/ld

%if %{with check}
%check
export MOLD_LIBDIR="%{_libdir}"
%cargo_test
(cd target/rpm/mold-test/out/test/results &&
  grep --files-with-matches --line-regexp skip */*.status) || :
%endif

%post
if [ "$1" = 1 ]; then
  update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.mold 1
fi

%postun
if [ "$1" = 0 ]; then
  update-alternatives --remove ld %{_bindir}/ld.mold
fi

%files
%license LICENSE
%doc README.md
%ghost %{_bindir}/ld
%{_bindir}/mold
%{_bindir}/ld.mold
%{_libdir}/mold/
%{_libexecdir}/mold/
%{_mandir}/man1/ld.mold.1*
%{_mandir}/man1/mold.1*

%changelog
%autochangelog
