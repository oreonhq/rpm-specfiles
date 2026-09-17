%global source0_hash 108f838c2e07ec114048000fad5ea14e55d83a2cb199a8dc0a0138064d2e432e

%global pypi_name conu

Name:           %{pypi_name}
Version:        0.7.1
Release:        31%{?dist}
Summary:        library which makes it easy to write tests for your containers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/fedora-modularity/conu
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
# exclude ppc64 because there is no moby-engine package
# https://bugzilla.redhat.com/show_bug.cgi?id=1547049
ExcludeArch:    ppc64

# for docs

%description
`conu` is a library which makes it easy to write tests for your containers
and is handy when playing with containers inside your code.
It defines an API to access and manipulate containers,
images and provides more, very helpful functions.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-kubernetes
BuildRequires:  python3-docker
BuildRequires:  python3-requests
BuildRequires:  python3-pyxattr
BuildRequires:  python3-six
Requires:       python3-kubernetes
Requires:       python3-docker
Requires:       python3-requests
Requires:       python3-pyxattr
Requires:       python3-six
# these are optional but still recommended
Recommends:     moby-engine
Recommends:     source-to-image
Recommends:     acl
Recommends:     libselinux-utils

%description -n python3-%{pypi_name}
`conu` is a library which makes it easy to write tests for your containers
and is handy when playing with containers inside your code.
It defines an API to access and manipulate containers,
images and provides more, very helpful functions.

%package -n     python3-%{pypi_name}-pytest
Summary:        fixtures which can be utilized via pytest
%{?python_provide:%python_provide python3-%{pypi_name}-pytest}
Requires:       python3-pytest
Requires:       python3-%{pypi_name}

%description -n python3-%{pypi_name}-pytest
fixtures which can be utilized via pytest

%package -n %{pypi_name}-doc
Summary:        conu documentation
BuildRequires:  python3-sphinx

%description -n %{pypi_name}-doc
Documentation for conu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH="${PWD}:${PWD}/docs/" sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%exclude %{python3_sitelib}/tests
%exclude %{python3_sitelib}/fixtures

%files -n python3-%{pypi_name}-pytest
%license LICENSE
%{python3_sitelib}/%{pypi_name}/fixtures/

%files -n %{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
