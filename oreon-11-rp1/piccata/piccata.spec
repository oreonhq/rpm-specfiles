%global source0_hash 514d5fbc6c0e8ec7b1267c43223451a5c1300f38abf6b36b810f273391568bc8
Name:          piccata
Version:       2.0.3
Release:        1%{?dist}
Summary:        A simple Python based CoAP (RFC7252) toolkit
License:       MIT
URL:           https://github.com/NordicSemiconductor/piccata
Source0:        https://github.com/NordicSemiconductor/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-piccata = %{version}-%{release}
# /oreon:deps
%description
Piccata is a simple CoAP (RFC7252) toolkit written in Python.

%package -n python3-piccata
Summary:        A simple Python based CoAP (RFC7252) toolkit
%description -n python3-piccata
Piccata is a simple CoAP (RFC7252) toolkit written in Python.

The toolkit provides basic building blocks for using CoAP in an application.
piccata handles messaging between endpoints (retransmission, deduplication)
and request/response matching.

Handling and matching resources, blockwise transfers, etc. is left to the
application but functions to faciliate this are provided.

Piccata uses a transport abstraction to faciliate using the toolkit for
communication over different link types. Transport for a UDP socket is provided.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -rf %{buildroot}/%{python3_sitelib}/tests/
%oreon_autofiles python3-piccata usr/lib/python3*/site-packages/piccata* usr/lib64/python3*/site-packages/piccata* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/piccata* usr/lib64/python3*/site-packages/piccata* usr/bin/*

%files
%files -n python3-piccata -f %{oreon_filedir}/python3-piccata.list

%changelog

%autochangelog
