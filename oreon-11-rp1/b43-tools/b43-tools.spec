%global source0_hash b78b4c0ffb37ba7303d53c7c59b8d912139b2aa1470f747366a213b7bd975996
%global git_commit 2fe10ea6690df9a068cb21cde537236bae784a14
%global git_date 20220704
Name:		b43-tools
Version:	019
Release:        1%{?dist}
Summary:        Tools for the Broadcom 43xx series WLAN chip
License:	GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
URL:		https://bues.ch/cgit/%{name}.git
VCS:		git:https://git.bues.ch/git/%{name}.git
Source0:        https://bues.ch/cgit/%{name}.git/snapshot/%{name}-%{git_commit}.tar.xz
Patch1:		0001-b43-tools-fix-format-security-errors.patch
Patch2:		0002-Use-2to3-to-convert-to-Python3.patch
Patch3:		0003-Explicitly-use-python3.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
Tools for the Broadcom 43xx series WLAN chip.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}
install -p -m 0644 assembler/COPYING COPYING.assembler
install -p -m 0644 assembler/README README.assembler
install -p -m 0644 debug/COPYING COPYING.debug
install -p -m 0644 debug/README README.debug
install -p -m 0644 disassembler/COPYING COPYING.disassembler
install -p -m 0644 ssb_sprom/README README.ssb_sprom
install -p -m 0644 ssb_sprom/COPYING COPYING.ssb_sprom

%build

CFLAGS="%{optflags}" %{make_build} -C assembler
CFLAGS="%{optflags}" %{make_build} -C disassembler
CFLAGS="%{optflags}" %{make_build} -C ssb_sprom
%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm.bin %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-dasm %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-fwconv %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 ssb_sprom/ssb-sprom %{buildroot}%{_bindir}
install -p -m 0755 debug/b43-beautifier %{buildroot}%{_bindir}
install -p -m 0755 debug/b43-fwdump %{buildroot}%{_bindir}
install -d %{buildroot}%{python3_sitelib}
install -p -m 0644 debug/libb43.py %{buildroot}%{python3_sitelib}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
