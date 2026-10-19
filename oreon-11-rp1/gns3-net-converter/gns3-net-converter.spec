%global source0_hash 0d189874a299af3853e97e88e41f089cad2949251ef0a68c9b217485ccc76ac6
Name:           gns3-net-converter
Version:        1.3.0
Release:        1%{?dist}
Summary:        Convert old ini-style GNS3 topologies to v1+ JSON format
Patch1:         0001-Explicitly-require-setuptools-utils-get_resource.py-.patch
License:        GPL-3.0-only
URL:            https://pypi.org/project/gns3-net-converter/
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires: python3-configobj
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gns3-net-converter = %{version}-%{release}
# /oreon:deps
%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

GNS3 Converter is designed to convert old ini-style GNS3 topologies (<=0.8.7)
to the newer version v1+ JSON format for use in GNS3 v1+.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
