%global source0_hash 4282854ef58258b201cc911fa7451b3d9836d3e5e6dac8bcb0972e9777962850
%global         gituser         unixfreak0037
%global         gitname         officeparser
%global         commit          42c2d40372fe271f2039ca1adc145d2aef8c9545
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
Name:           officeparser
Version:        1.0.1
Release:        1%{?dist}
Summary:        Parse the format of OLE compound documents used by MS Office applications
License:        MIT
URL:            https://github.com/%{gituser}/%{gitname}
Source0:        https://github.com/%{gituser}/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch1:         https://patch-diff.githubusercontent.com/raw/unixfreak0037/officeparser/pull/19.patch#/officeparser-01_python3_compatibiity.patch
Patch2:         officeparser-02_python3_xrange.patch
Patch3:         officeparser-03_default_help.patch
Patch4:         officeparser-04_string_conversion.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Python script officeparser.py that parses the format of OLE compound documents
used by Microsoft Office applications. Some useful features of this script
include: macro extraction, embedded file extraction, format analysis.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{gitname}-%{commit}

# Change implicit "env python" to explicit versioned python shebang
# https://fedoraproject.org/wiki/Features/SystemPythonExecutablesUseSystemPython
sed 's|^#!/usr/bin/env python|#!%{__python3}|' officeparser.py > officeparser.py.new
touch -r officeparser.py officeparser.py.new &&
mv officeparser.py.new officeparser.py

%build

%install
install -D officeparser.py %{buildroot}%{_bindir}/officeparser.py
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
