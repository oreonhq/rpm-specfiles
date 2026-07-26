%global source0_hash f2aedd1be781744c6cda18a5cfaaee35e3888ce1efd1c528f66f80a757f2cd99

Name:          piccata
Version:       2.0.2
Release:       %autorelease
Summary:       A simple Python based CoAP (RFC7252) toolkit
License:       MIT
URL:           https://github.com/NordicSemiconductor/piccata
Source0:       %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

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

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files piccata transport

rm -rf %{buildroot}/%{python3_sitelib}/tests/

%files -n python3-piccata -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
