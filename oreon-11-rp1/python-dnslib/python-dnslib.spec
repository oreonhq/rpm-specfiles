%global source0_hash 0400ffdc0e3ff51ac69131511f7df04437bb4f36eb96ec6d69b33fd4b9f2443e

%global pypi_name dnslib

Name:           python-%{pypi_name}
Version:        0.9.26
Release:        2%{?dist}
Summary:        Simple library to encode/decode DNS packets

License:        BSD-2-Clause
URL:            https://github.com/paulc/dnslib
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Simple library to encode/decode DNS wire-format packets.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Simple library to encode/decode DNS wire-format packets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' dnslib/test_decode.py
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dnslib

%check
%pyproject_check_import
VERSIONS=%{python3} ./run_tests.sh

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README

%changelog
%autochangelog
