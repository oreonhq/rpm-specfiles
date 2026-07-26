%global source0_hash 0477a15fabf030866636c96a702471d8b53edaf14ac1726f2ee434e294be5b42

%global srcname ijson

Name:           python-%{srcname}
Version:        3.3.0
Release:        %autorelease
Summary:        Iterative JSON parser

License:        BSD-3-Clause
URL:            https://github.com/ICRAR/ijson
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  python3dist(setuptools)

%global _description %{expand:
Iterative JSON parser with standard Python iterator interfaces.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
Recommends:     yajl
Recommends:     python3dist(cffi)

# Test dependencies
BuildRequires:  python3dist(cffi)

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Disable tests for unsupported configurations.
sed -i "s/\['python', 'yajl', 'yajl2', 'yajl2_cffi', 'yajl2_c']/\['python', 'yajl2', 'yajl2_cffi']/" test/test_base.py

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:$PWD %{python3} -m unittest discover

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
