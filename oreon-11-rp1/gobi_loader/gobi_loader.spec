%global source0_hash 78bdc255451cde1caa406e146b01a88828480c9c43272de8cffdb61627be754a

Summary:   Firmware loader for Qualcomm Gobi WWAN devices 
Name:      gobi_loader
Version:   0.7
Release:   37%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:   GPL-2.0-only
Source0:   http://www.codon.org.uk/~mjg59/gobi_loader/download/%{name}-%{version}.tar.gz
URL:       http://www.codon.org.uk/~mjg59/gobi_loader

BuildRequires: gcc
BuildRequires: make

%description
gobi_loader is a firmware loader for Qualcomm Gobi USB chipsets. These
devices appear in an uninitialized state when power is applied and require
firmware to be loaded before they can be used as modems. gobi_loader adds
a udev rule that will trigger loading of the firmware and make the modem
usable.

Note that gobi_loader requires firmware images which can't be freely
redistributed. See http://www.codon.org.uk/~mjg59/gobi_loader for more
information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i -e 's|gcc -Wall|gcc %{optflags} %{?__global_ldflags}|' Makefile

%build
make %{?_smp_mflags}

%install
make install prefix=%{buildroot}

%files
%attr(755,root,root) /lib/udev/gobi_loader
%attr(644,root,root) /lib/udev/rules.d/60-gobi.rules
%doc README

%changelog
%autochangelog
