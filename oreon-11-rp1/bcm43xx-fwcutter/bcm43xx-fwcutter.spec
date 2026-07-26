%global source0_hash 5153c94ab59ed9d3f1a6c4ed4764953be61cefbf27a9c6b04c24cca7d44034ce

Name:           bcm43xx-fwcutter
Version:        006
Release:        38%{?dist}
Summary:        Firmware extraction tool for Broadcom wireless driver

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://bcm43xx.berlios.de/
Source0:        http://download.berlios.de/bcm43xx/%{name}-%{version}.tar.bz2
Source1:	README.Fedora

BuildRequires: make
BuildRequires:  gcc
%description
This package contains the 'bcm43xx-fwcutter' tool which is used to
extract firmware for the Broadcom network devices, from the official
Windows, MacOS or Linux drivers.

See the README.Fedora file shipped in the package's documentation for
instructions on using this tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i -e 's/-O2/$(RPM_OPT_FLAGS)/' Makefile

%build
make
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 bcm43xx-fwcutter $RPM_BUILD_ROOT%{_bindir}/bcm43xx-fwcutter
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0644 bcm43xx-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/bcm43xx-fwcutter
%{_mandir}/man1/*
%doc README README.Fedora COPYING

%changelog
%autochangelog
