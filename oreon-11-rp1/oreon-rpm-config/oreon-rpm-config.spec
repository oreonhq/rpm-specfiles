# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b154b405aae8e92a661805e2eed3c9e0d63403533aa70b556ab52f8836cd3dfd
%global debug_package %{nil}
%global rrcdir /usr/lib/rpm/oreon

Name: oreon-rpm-config
Version: 345
Release: 13%{?dist}
Summary: Oreon rpm build configuration
License: GPL-1.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic
URL: https://github.com/oreonhq/rpm-specfiles
Source0: macros
Source1: rpmrc
Source2: oreon-hardened-cc1
Source3: oreon-hardened-ld
Source4: oreon-hardened-ld-errors
Source5: oreon-hardened-clang.cfg
Source6: oreon-hardened-clang-ld.cfg
Source7: oreon-annobin-cc1
Source8: oreon-annobin-select-gcc-built-plugin
Source9: oreon-annobin-select-annobin-built-plugin
Source10: oreon-annobin-plugin-select.sh
Source11: macros.oreon-misc-srpm
Source12: macros.mono-srpm
Source13: macros.nodejs-srpm
Source14: macros.ldc-srpm
Source15: macros.valgrind-srpm
Source16: macros.dotnet-srpm
Source17: macros.hare-srpm
Source18: macros.build-constraints
Source19: macros.dwz
Source20: macros.oreon-misc
Source21: macros.ldconfig
Source22: macros.vpath
Source23: macros.shell-completions
Source24: macros.rpmautospec
Source25: brp-mangle-shebangs
Source26: find-provides
Source27: find-requires
Source28: dist.sh
Source29: config.guess
Source30: config.sub
Source31: libsymlink.attr
Source32: brp-ldconfig
Source33: brp-strip-lto
Source34: common.lua
Source35: buildflags.md
Source36: macros.oreon-vendor-compat

BuildArch: noarch
Provides: system-rpm-config = %{version}-%{release}
Obsoletes: rpmautospec-rpm-macros < 0.6.3-2
# replaces the base buildroot rpm config, which ships the same macro files
Provides: redhat-rpm-config = %{version}-%{release}
Obsoletes: redhat-rpm-config < %{version}-%{release}

BuildRequires: oreon-rpm-macros

Requires: coreutils
Requires: rpm >= 4.19.91
Requires: dwz >= 0.4
Requires: zip
Requires: %{_bindir}/find
Requires: %{_bindir}/file
Requires: %{_bindir}/grep
Requires: %{_bindir}/sed
Requires: %{_bindir}/xargs
Requires: (gcc-plugin-annobin if gcc)
Requires: efi-srpm-macros
Requires: cmake-srpm-macros
Requires: fonts-srpm-macros
Requires: forge-srpm-macros
Requires: go-srpm-macros
Requires: java-srpm-macros
Requires: kernel-srpm-macros >= 1.0-12
Requires: lua-srpm-macros
Requires: ocaml-srpm-macros
Requires: openblas-srpm-macros
Requires: perl-srpm-macros
Requires: python-srpm-macros >= 3.11-7
Requires: qt6-srpm-macros
Requires: rust-srpm-macros
Requires: package-notes-srpm-macros
Requires: pyproject-srpm-macros
Requires: filesystem-srpm-macros

%description
Distro rpm macros, compiler flags, and build-root policy scripts.

%prep
%oreon_sha256
%setup -c -T
cp -p %{sources} .

%build

%install
mkdir -p %{buildroot}%{rrcdir}
install -p -m 644 -t %{buildroot}%{rrcdir} macros rpmrc
install -p -m 444 -t %{buildroot}%{rrcdir} oreon-hardened-*
install -p -m 444 -t %{buildroot}%{rrcdir} oreon-annobin-cc1 oreon-annobin-select-gcc-built-plugin oreon-annobin-select-annobin-built-plugin
install -p -m 755 -t %{buildroot}%{rrcdir} oreon-annobin-plugin-select.sh
install -p -m 755 -t %{buildroot}%{rrcdir} config.guess config.sub dist.sh
install -p -m 755 -t %{buildroot}%{rrcdir} brp-ldconfig brp-mangle-shebangs brp-strip-lto
install -p -m 755 -t %{buildroot}%{rrcdir} find-provides find-requires

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.*
mkdir -p %{buildroot}%{_sysconfdir}/rpm
ln -s %{_rpmconfigdir}/oreon/macros %{buildroot}%{_sysconfdir}/rpm/macros.oreon-vendor
ln -s %{rrcdir}/rpmrc %{buildroot}%{_sysconfdir}/rpmrc
mv %{buildroot}%{_rpmconfigdir}/macros.d/macros.oreon-vendor-compat %{buildroot}%{_sysconfdir}/rpm/

mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m 644 -t %{buildroot}%{_fileattrsdir} libsymlink.attr

mkdir -p %{buildroot}%{_rpmluadir}/oreon/rpm
mkdir -p %{buildroot}%{_rpmluadir}/oreon/srpm
mkdir -p %{buildroot}%{_rpmluadir}/fedora
install -p -m 644 -t %{buildroot}%{_rpmluadir}/oreon common.lua
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora common.lua
mkdir -p %{buildroot}%{_rpmconfigdir}/redhat
install -p -m 644 oreon-hardened-cc1 %{buildroot}%{_rpmconfigdir}/redhat/redhat-hardened-cc1

install -p -m 644 %{SOURCE35} .

%triggerin -- gcc-plugin-annobin gcc
%{rrcdir}/oreon-annobin-plugin-select.sh
%end

%triggerpostun -- gcc-plugin-annobin
%{rrcdir}/oreon-annobin-plugin-select.sh
%end

%files
%doc buildflags.md
%dir %{rrcdir}
%{rrcdir}/brp-ldconfig
%{rrcdir}/brp-mangle-shebangs
%{rrcdir}/brp-strip-lto
%{rrcdir}/config.guess
%{rrcdir}/config.sub
%{rrcdir}/dist.sh
%{rrcdir}/find-provides
%{rrcdir}/find-requires
%{rrcdir}/macros
%{rrcdir}/oreon-hardened-cc1
%{rrcdir}/oreon-hardened-clang.cfg
%{rrcdir}/oreon-hardened-clang-ld.cfg
%{rrcdir}/oreon-hardened-ld
%{rrcdir}/oreon-hardened-ld-errors
%{rrcdir}/rpmrc
%attr(0755,-,-) %{rrcdir}/oreon-annobin-plugin-select.sh
%verify(owner group mode) %{rrcdir}/oreon-annobin-cc1
%{rrcdir}/oreon-annobin-select-gcc-built-plugin
%{rrcdir}/oreon-annobin-select-annobin-built-plugin
%{_fileattrsdir}/libsymlink.attr
%{_rpmconfigdir}/macros.d/macros.*-srpm
%{_rpmconfigdir}/macros.d/macros.build-constraints
%{_rpmconfigdir}/macros.d/macros.dwz
%{_rpmconfigdir}/macros.d/macros.oreon-misc
%{_rpmconfigdir}/macros.d/macros.ldconfig
%{_rpmconfigdir}/macros.d/macros.rpmautospec
%{_rpmconfigdir}/macros.d/macros.shell-completions
%{_rpmconfigdir}/macros.d/macros.vpath
%{_sysconfdir}/rpm/macros.oreon-vendor
%{_sysconfdir}/rpmrc
%{_sysconfdir}/rpm/macros.oreon-vendor-compat
%dir %{_rpmluadir}/oreon
%dir %{_rpmluadir}/oreon/srpm
%dir %{_rpmluadir}/oreon/rpm
%{_rpmluadir}/oreon/common.lua
%{_rpmluadir}/fedora/common.lua
%{_rpmconfigdir}/redhat/redhat-hardened-cc1
