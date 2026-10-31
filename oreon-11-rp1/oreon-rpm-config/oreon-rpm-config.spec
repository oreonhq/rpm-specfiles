%global source0_hash 868a9ebb9f6f4d3eeb5f40a564e5723c348f1696b13d8f7500c58b8e751914e8
%global debug_package %{nil}
%global rrcdir /usr/lib/rpm/redhat

Name: oreon-rpm-config
Version: 345
Release: 4%{?dist}
Summary: Oreon rpm build configuration
License: GPL-1.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic
URL: https://github.com/oreonhq/rpm-specfiles
Source0: macros
Source1: rpmrc
Source2: redhat-hardened-cc1
Source3: redhat-hardened-ld
Source4: redhat-hardened-ld-errors
Source5: redhat-hardened-clang.cfg
Source6: redhat-hardened-clang-ld.cfg
Source7: redhat-annobin-cc1
Source8: redhat-annobin-select-gcc-built-plugin
Source9: redhat-annobin-select-annobin-built-plugin
Source10: redhat-annobin-plugin-select.sh
Source11: macros.fedora-misc-srpm
Source12: macros.mono-srpm
Source13: macros.nodejs-srpm
Source14: macros.ldc-srpm
Source15: macros.valgrind-srpm
Source16: macros.dotnet-srpm
Source17: macros.hare-srpm
Source18: macros.build-constraints
Source19: macros.dwz
Source20: macros.fedora-misc
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

BuildArch: noarch
Provides: redhat-rpm-config = %{version}-%{release}
Provides: system-rpm-config = %{version}-%{release}
Obsoletes: redhat-rpm-config < %{version}-%{release}
Obsoletes: rpmautospec-rpm-macros < 0.6.3-2

BuildRequires: oreon-rpm-macros
BuildRequires: perl-generators

Requires: coreutils
Requires: rpm >= 4.19.91
Requires: dwz >= 0.4
Requires: zip
Requires: %{_bindir}/find
Requires: %{_bindir}/file
Requires: %{_bindir}/grep
Requires: %{_bindir}/sed
Requires: %{_bindir}/xargs
Requires: (annobin-plugin-gcc if gcc)
Requires: (gcc-plugin-annobin if gcc)
Requires: (gpgverify if gnupg2)
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
Still provides redhat-rpm-config so existing BuildRequires keep working.

%prep
%oreon_sha256
%setup -c -T
cp -p %{sources} .

%build

%install
mkdir -p %{buildroot}%{rrcdir}
install -p -m 644 -t %{buildroot}%{rrcdir} macros rpmrc
install -p -m 444 -t %{buildroot}%{rrcdir} redhat-hardened-*
install -p -m 444 -t %{buildroot}%{rrcdir} redhat-annobin-cc1 redhat-annobin-select-gcc-built-plugin redhat-annobin-select-annobin-built-plugin
install -p -m 755 -t %{buildroot}%{rrcdir} redhat-annobin-plugin-select.sh
install -p -m 755 -t %{buildroot}%{rrcdir} config.guess config.sub dist.sh
install -p -m 755 -t %{buildroot}%{rrcdir} brp-ldconfig brp-mangle-shebangs brp-strip-lto
install -p -m 755 -t %{buildroot}%{rrcdir} find-provides find-requires

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.*

mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m 644 -t %{buildroot}%{_fileattrsdir} libsymlink.attr

mkdir -p %{buildroot}%{_rpmluadir}/fedora/rpm
mkdir -p %{buildroot}%{_rpmluadir}/fedora/srpm
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora common.lua

install -p -m 644 %{SOURCE35} .

%triggerin -- annobin-plugin-gcc gcc-plugin-annobin gcc
%{rrcdir}/redhat-annobin-plugin-select.sh
%end

%triggerpostun -- annobin-plugin-gcc gcc-plugin-annobin
%{rrcdir}/redhat-annobin-plugin-select.sh
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
%{rrcdir}/redhat-hardened-cc1
%{rrcdir}/redhat-hardened-clang.cfg
%{rrcdir}/redhat-hardened-clang-ld.cfg
%{rrcdir}/redhat-hardened-ld
%{rrcdir}/redhat-hardened-ld-errors
%{rrcdir}/rpmrc
%attr(0755,-,-) %{rrcdir}/redhat-annobin-plugin-select.sh
%verify(owner group mode) %{rrcdir}/redhat-annobin-cc1
%{rrcdir}/redhat-annobin-select-gcc-built-plugin
%{rrcdir}/redhat-annobin-select-annobin-built-plugin
%{_fileattrsdir}/libsymlink.attr
%{_rpmconfigdir}/macros.d/macros.*-srpm
%{_rpmconfigdir}/macros.d/macros.build-constraints
%{_rpmconfigdir}/macros.d/macros.dwz
%{_rpmconfigdir}/macros.d/macros.fedora-misc
%{_rpmconfigdir}/macros.d/macros.ldconfig
%{_rpmconfigdir}/macros.d/macros.rpmautospec
%{_rpmconfigdir}/macros.d/macros.shell-completions
%{_rpmconfigdir}/macros.d/macros.vpath
%dir %{_rpmluadir}/fedora
%dir %{_rpmluadir}/fedora/srpm
%dir %{_rpmluadir}/fedora/rpm
%{_rpmluadir}/fedora/common.lua
