%global source0_hash 097707f0de33edf6209635cb7b63c6ca62ba3504b1be6a15a65fc984cabb8672

%global pypi_name pyshark

Name:           python-%{pypi_name}
Version:        0.6
Release:        4%{?dist}
Summary:        Python packet parsing using wireshark dissectors

License:        MIT
URL:            https://github.com/KimiNewt/pyshark
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       wireshark-cli

%description
Python wrapper for tshark that allowing python packet parsing using wireshark
dissectors. It doesn't actually parse any packets, it simply uses tshark's
ability to export XMLs to use its parsing.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-logbook
BuildRequires:  python3-lxml
BuildRequires:  python3-pytest
BuildRequires:  python3-termcolor
BuildRequires:  wireshark-cli
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python wrapper for tshark that allowing python packet parsing using wireshark
dissectors. It doesn't actually parse any packets, it simply uses tshark's
ability to export XMLs to use its parsing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -N requirements.txt

%build
pushd src
%pyproject_wheel
popd

%install
pushd src
%pyproject_install
popd

# TShark is crashing during the tests, need upstream fix
#%%check
#%%pytest tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.dist-info

%changelog
%autochangelog
