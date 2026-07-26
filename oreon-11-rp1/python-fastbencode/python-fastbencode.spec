%global source0_hash 98c5152ea30f103fc4b3d7b62a3e510cb87bf899a54775b619719a967749e295

%global pypi_name fastbencode

Name:           python-%{pypi_name}
Version:        0.3.2
Release:        5%{?dist}
Summary:        Implementation of bencode with optional fast C extensions

License:        GPL-2.0-or-later AND MIT
#fastbencode is licensed under GPLv2+
#_bencode_py.py is licensed under MIT
URL:            https://github.com/breezy-team/fastbencode
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc

%global _description %{expand:
fastbencode is an implementation of the bencode serialization format 
originally used by BitTorrent.
The package includes both a pure-Python version and an optional C extension 
based on Cython.
Both provide the same functionality, but the C extension provides 
significantly better performance.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x cext

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-%{pypi_name}
%license COPYING
%doc README.md
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
