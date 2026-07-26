%global source0_hash 9f232c21e12aa1ff52690e365b5a0ecfd42cc27a6ec86e1b92ece88f763f4b78

%global pypi_name txaio

Name:           python-%{pypi_name}
Version:        25.12.2
Release:        2%{?dist}
Summary:        Compatibility API between asyncio/Twisted/Trollius

License:        MIT
URL:            https://txaio.readthedocs.io/
Source0:        %{pypi_source}
Patch0:         remove-unpackaged-sphinx-ext.patch
BuildArch:      noarch

%description
Helper library for writing code that runs unmodified on both Twisted and
asyncio.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-test
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pyenchant) >= 1.6.6
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Helper library for writing code that runs unmodified on both Twisted and
asyncio.

%package doc
Summary:        Documentation for txaio

BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-furo
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-design)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinxext-opengraph)
BuildRequires:  python3dist(sphinxcontrib-spelling)
BuildRequires:  python3dist(sphinx-autoapi)
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(linkify-it-py)
BuildRequires:  google-roboto-fonts
Requires:       js-jquery
Requires:       google-roboto-fonts

%description doc
Helper library for writing code that runs unmodified on both Twisted and
asyncio. Documentation in html format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p 1
# Remove upstream's egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Build documentation
cd docs && make html
# Remove buildinfo
rm -rf _build/html/.buildinfo
# Unbundle jquery
rm -f  _build/html/_static/jquery.js
ln -s /usr/share/javascript/jquery/latest/jquery.min.js _build/html/_static/jquery.js

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests
# Checking import of twisted related code will fail because by testing imports of
# asyncio code, txaio gets configured for asyncio and fails to start with twisted.
%pyproject_check_import -e txaio.tx -e txaio.with_twisted

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files doc
%license LICENSE
%doc docs/_build/html

%changelog
%autochangelog
