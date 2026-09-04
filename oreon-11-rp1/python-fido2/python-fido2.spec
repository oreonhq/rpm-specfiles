%global source0_hash 4a85e7cdd985fe94e32006b4f94e7e31c898a257277d7a92728b88e1795a8d42

%global srcname fido2

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        Functionality for FIDO 2.0, including USB device communication

# Main code is BSD
# pyu2f is APLv2
# public_suffix_list.dat is MPLv2
# Automatically converted from old format: BSD and ASL 2.0 and MPLv2.0 - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND Apache-2.0 AND MPL-2.0
URL:            https://github.com/Yubico/python-fido2
Source0:        https://github.com/Yubico/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
Provides library functionality for communicating with a FIDO device over USB\
as well as verifying attestation and assertion signatures.\
\
WARNING: This project is in beta. Expect things to change or break at any time!\
\
This library aims to support the FIDO U2F and FIDO 2.0 protocols for\
communicating with a USB authenticator via the Client-to-Authenticator\
Protocol (CTAP 1 and 2). In addition to this low-level device access, classes\
defined in the fido2.client and fido2.server modules implement higher level\
operations which are useful when interfacing with an Authenticator, or when\
implementing a Relying Party.\
\
For usage, see the examples/ directory.

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary: %summary
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# EL8 has old python-cryptography that makes a few tests fail
# https://github.com/Yubico/python-fido2/issues/111
%{__python3} -m unittest discover -v %{?el8:|| :}

%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%license COPYING*
%doc NEWS README.adoc examples

%changelog
%autochangelog
