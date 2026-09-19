%global source0_hash afc89273a026a7a02691b57b3f1285c4881735fb8b3aa594db87299944f6af94

%global pypi_name sphinxcontrib-pecanwsme

Name:           python-%{pypi_name}
Version:        0.11.0
Release:        6%{?dist}
Summary:        Extension to Sphinx for documenting APIs built with Pecan and WSME

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/dreamhost/sphinxcontrib-pecanwsme
Source0:        https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is an extension to Sphinx (http://sphinx-doc.org/) for documenting APIs
built with the Pecan WSGI object-dispatching web framework and WSME
(Web Services Made Easy).

%package -n python3-%{pypi_name}
Summary:        Extension to Sphinx for documenting APIs built with Pecan and WSME
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires: python3-six
Requires: python3-sphinxcontrib-httpdomain

%description -n python3-%{pypi_name}
This is an extension to Sphinx (http://sphinx-doc.org/) for documenting APIs
built with the Pecan WSGI object-dispatching web framework and WSME
(Web Services Made Easy).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib/pecanwsme
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/*-nspkg.pth

%changelog
%autochangelog
