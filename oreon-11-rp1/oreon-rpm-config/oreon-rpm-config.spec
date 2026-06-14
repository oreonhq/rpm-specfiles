%global source0_hash none
%global source_date_epoch_from_changelog 0
%global __oreon_hwcaps_post_install %{nil}
%global __spec_install_post %{?__debug_package:%{__debug_install_post}}%{nil}

#                        TO WHOM IT MAY CONCERN
#
# Don't add patches, dist-git is the upstream repository for this package.

Summary: Oreon-specific rpm configuration files
Name: oreon-rpm-config
Version: 345
Release: 2%{?dist}
# config.guess, config.sub are GPL-3.0-or-later WITH Autoconf-exception-generic
License: GPL-1.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic
URL: https://github.com/oreonhq/rpm-specfiles

Provides: redhat-rpm-config = %{version}-%{release}
Provides: system-rpm-config = %{version}-%{release}
Obsoletes: redhat-rpm-config < %{version}-%{release}

# Core rpm settings
Source0: macros
Source1: rpmrc

# gcc specs files for hardened builds
Source50: redhat-hardened-cc1
Source51: redhat-hardened-ld
Source52: redhat-hardened-ld-errors
# clang config spec files
Source53: redhat-hardened-clang.cfg
Source54: redhat-hardened-clang-ld.cfg

# gcc specs files for annobin builds
Source60: redhat-annobin-cc1
Source61: redhat-annobin-select-gcc-built-plugin
Source62: redhat-annobin-select-annobin-built-plugin
Source63: redhat-annobin-plugin-select.sh

Source100: macros.fedora-misc-srpm
Source102: macros.mono-srpm
Source103: macros.nodejs-srpm
Source104: macros.ldc-srpm
Source105: macros.valgrind-srpm
Source108: macros.dotnet-srpm
Source109: macros.hare-srpm

Source150: macros.build-constraints
Source151: macros.dwz
Source152: macros.fedora-misc
Source155: macros.ldconfig
Source156: macros.vpath
Source157: macros.shell-completions
Source158: macros.rpmautospec
Source159: macros.oreon-opt
Source160: macros.oreon-hwcaps

Source201: brp-mangle-shebangs

Source300: find-provides
Source304: find-requires

Source400: dist.sh

Source500: https://git.savannah.gnu.org/cgit/config.git/plain/config.guess
Source501: https://git.savannah.gnu.org/cgit/config.git/plain/config.sub

Source602: libsymlink.attr

Source700: brp-ldconfig
Source701: brp-strip-lto

Source800: common.lua

Source900: buildflags.md

BuildArch: noarch
BuildRequires: perl-generators
Requires: coreutils

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

Requires: rpm >= 4.19.91
Requires: dwz >= 0.4
Requires: zip
Requires: (annobin-plugin-gcc if gcc)
Requires: (gcc-plugin-annobin if gcc)
Requires: (gpgverify if gnupg2)

Requires: %{_bindir}/find
Requires: %{_bindir}/file
Requires: %{_bindir}/grep
Requires: %{_bindir}/sed
Requires: %{_bindir}/xargs

Conflicts: gcc < 8.0.1-0.22

Obsoletes: rpmautospec-rpm-macros < 0.6.3-2

%global rrcdir /usr/lib/rpm/redhat

%description
Oreon rpm configuration. Sets distro-wide -O3, LTO, and x86_64 tuning macros
while keeping -march=x86-64 so binaries run on all 64-bit cpus. Still provides
redhat-rpm-config for BuildRequires compatibility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -c -T
cp -p %{sources} .

%install
mkdir -p %{buildroot}%{rrcdir}
install -p -m 644 -t %{buildroot}%{rrcdir} macros rpmrc
install -p -m 444 -t %{buildroot}%{rrcdir} redhat-hardened-*
install -p -m 444 -t %{buildroot}%{rrcdir} redhat-annobin-*
install -p -m 755 -t %{buildroot}%{rrcdir} config.*
install -p -m 755 -t %{buildroot}%{rrcdir} dist.sh
install -p -m 755 -t %{buildroot}%{rrcdir} brp-*

install -p -m 755 -t %{buildroot}%{rrcdir} find-*
install -p -m 755 -t %{buildroot}%{rrcdir} brp-*

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.*

mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m 644 -t %{buildroot}%{_fileattrsdir} *.attr

mkdir -p %{buildroot}%{_rpmluadir}/fedora/{rpm,srpm}
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora common.lua

%triggerin -- annobin-plugin-gcc gcc-plugin-annobin gcc
%{rrcdir}/redhat-annobin-plugin-select.sh
%end

%triggerpostun -- annobin-plugin-gcc gcc-plugin-annobin
%{rrcdir}/redhat-annobin-plugin-select.sh
%end

%files
%dir %{rrcdir}
%{rrcdir}/brp-ldconfig
%{rrcdir}/brp-mangle-shebangs
%{rrcdir}/brp-strip-lto
%{rrcdir}/config.*
%{rrcdir}/dist.sh
%{rrcdir}/find-provides
%{rrcdir}/find-requires
%{rrcdir}/macros
%{rrcdir}/redhat-hardened-*
%{rrcdir}/rpmrc
%{_fileattrsdir}/*.attr
%{_rpmconfigdir}/macros.d/macros.*-srpm
%{_rpmconfigdir}/macros.d/macros.build-constraints
%{_rpmconfigdir}/macros.d/macros.dwz
%{_rpmconfigdir}/macros.d/macros.fedora-misc
%{_rpmconfigdir}/macros.d/macros.ldconfig
%{_rpmconfigdir}/macros.d/macros.oreon-hwcaps
%{_rpmconfigdir}/macros.d/macros.oreon-opt
%{_rpmconfigdir}/macros.d/macros.rpmautospec
%{_rpmconfigdir}/macros.d/macros.shell-completions
%{_rpmconfigdir}/macros.d/macros.vpath
%dir %{_rpmluadir}/fedora
%dir %{_rpmluadir}/fedora/srpm
%dir %{_rpmluadir}/fedora/rpm
%{_rpmluadir}/fedora/*.lua

%attr(0755,-,-) %{rrcdir}/redhat-annobin-plugin-select.sh
%verify(owner group mode) %{rrcdir}/redhat-annobin-cc1
%{rrcdir}/redhat-annobin-select-gcc-built-plugin
%{rrcdir}/redhat-annobin-select-annobin-built-plugin

%doc buildflags.md
