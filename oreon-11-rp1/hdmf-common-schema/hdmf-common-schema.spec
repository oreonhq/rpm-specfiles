%global source0_hash 7582283672d50e43a4bd73dc1e1a079b504e04f34dfb9afb25513a37b5a7590e
Name:           hdmf-common-schema
Version:        1.10.0
Epoch:          1
Release:        1%{?dist}
Summary:        Specifications for pre-defined data structures provided by HDMF
License:        BSD-3-Clause-LBNL
URL:            https://github.com/hdmf-dev/hdmf-common-schema
Source0:        https://github.com/hdmf-dev/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
The HDMF Common specification defines a collection of common, reusable data
structures that build the foundation for the modeling of advanced data formats,
e.g., the Neurodata Without Borders (NWB) (https://www.nwb.org/)
neurophysiology data standard. The HDMF Common schema is integrated with HDMF
(https://github.com/hdmf-dev/hdmf), which provides advanced APIs for reading,
writing, and using HDMF-common data types.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
install -d '%{buildroot}%{_datadir}/hdmf-common-schema'
cp -rp 'common/' '%{buildroot}%{_datadir}/hdmf-common-schema/'
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
