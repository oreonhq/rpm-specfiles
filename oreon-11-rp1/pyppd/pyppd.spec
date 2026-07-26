%global source0_hash 164a592455c6c404492be811ad26a5fb6bf9220cdfea4d8d35f911a16a69be5c

Summary:       PPD file compressor and generator for CUPS
Name:          pyppd
Version:       1.0.2
Release:       37%{?dist}
URL:           http://pypi.python.org/pypi/pyppd
Source:        http://pypi.python.org/packages/source/p/pyppd/pyppd-%{version}.tar.gz
License:       MIT
BuildRequires: python3-devel
BuildArch:     noarch

%description
This program holds a compressed archive of PostScript Printer
Description files.  It can generate the PPD files on the fly for CUPS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i -e '1s,^#!/usr/bin/env python,#!/usr/bin/python3,' pyppd/pyppd-ppdfile.in

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE.txt
%doc README ISSUES CHANGES.txt
# This directory includes pyppd-ppdfile.in which looks like a script
# but is only a template.  For that reason it is *not* executable.
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}*.dist-info
%{_bindir}/%{name}

%changelog
%autochangelog
