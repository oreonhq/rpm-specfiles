%global source0_hash 6c2dfe6ca282d75f66df333869bb0ce7331c01b475db6809ff9d107b7cdfe04b

%global upstream_name sphinxcontrib-httpdomain

Name:           python-%{upstream_name}
Version:        1.8.1
Release:        7%{?dist}
Summary:        Sphinx domain for documenting HTTP APIs
License:        BSD-2-Clause
URL:            http://packages.python.org/sphinxcontrib-httpdomain/
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib-httpdomain/sphinxcontrib-httpdomain-1.8.1.tar.gz
# issue to be filed(?)
Patch4:         0004-httpdomain-bump-domain-data-version.patch
BuildArch:      noarch

%description
Using this Sphinx domain you can document your HTTP API. It includes support 
for generating documentation from Flask routing tables.

%package -n python3-%{upstream_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{upstream_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-sphinx
Requires:       python3-six

%description -n python3-%{upstream_name}
Using this Sphinx domain you can document your HTTP API. It includes support 
for generating documentation from Flask routing tables.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{upstream_name}-%{version}
%patch -P4 -p2
rm -r *.egg-info

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{upstream_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-7
- Prepare for Oreon 11 (RP1)
