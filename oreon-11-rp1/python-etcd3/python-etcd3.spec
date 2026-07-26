%global source0_hash 02cfcf5e608483610ac977eb4b6b31b9522dfbd397c60854c56aa334927cb7f0

%global srcname etcd3

Name:           python-%{srcname}
Version:        0.12.0
Release:        21%{?dist}
Summary:        Python client for the etcd API v3
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/kragniz/python-etcd3
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%global _description %{summary}, supported under python 2.7, 3.4 and 3.5.

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
sed -e 's|grpcio==.*|grpcio==1.26.0|' \
    -e 's|tenacity==.*|tenacity==6.0.0|' -i requirements/base.txt

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
%autochangelog
