%global source0_hash 6fbfd33ca5e18897d75bbd530a853ca577e202b57dc8e67b06a5f0547e64eed6

%global forgeurl    https://github.com/dns-lexicon/dns-lexicon
%global forgeversion 3.21.1
Version:            %{forgeversion}
%forgemeta

%global pypi_name dns-lexicon

%if 0%{?rhel} >= 8
# EPEL is currently missing dependencies used by the extras metapackages
# EPEL is currently missing dependencies used by the tests
%bcond_with tests
%bcond_with extras
%else
%bcond_without tests
%bcond_without extras
%endif

# disable tests for now
%bcond_without tests

Name:           python-%{pypi_name}
Release:        6%{?dist}
Summary:        Manipulate DNS records on various DNS providers in a standardized/agnostic way

License:        MIT
URL:            %{forgeurl}
# pypi releases don't contain necessary data to run the tests
Source0:        %{forgesource}
Source1:        create-local-tld-cache.py
Patch:          python-dns-lexicon-tox-config.patch
BuildArch:      noarch

BuildRequires:  python3-devel

# epel is missing full poetry and light packages needed for tests
%if 0%{?rhel >= 8}
#Patch:		disable-poetry-light.patch
%endif

# required to run the test suite
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-vcr
BuildRequires:  python3-pytest-xdist
BuildRequires:  publicsuffix-list
BuildRequires:  python3-tldextract
%endif

%description
Lexicon provides a way to manipulate DNS records on multiple DNS providers in a
standardized way. Lexicon has a CLI but it can also be used as a python
library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

# Both packages install a Python module named lexicon
# TODO: Remove this once resolved upstream (see upstream #222)
Conflicts:      python3-lexicon

# These "extras" were previously present in upstream lexicon but are not there
# anymore.
# {{{
%if %{with extras}
Obsoletes: python3-%{pypi_name}+easyname < 3.4
Provides: python3dist(%{pypi_name}[easyname]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[easyname]) = %{version}

Obsoletes: python3-%{pypi_name}+gratisdns < 3.4
Provides: python3dist(%{pypi_name}[gratisdns]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[gratisdns]) = %{version}

Obsoletes: python3-%{pypi_name}+henet < 3.4
Provides: python3dist(%{pypi_name}[henet]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[henet]) = %{version}

Obsoletes: python3-%{pypi_name}+hetzner < 3.4
Provides: python3dist(%{pypi_name}[hetzner]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[hetzner]) = %{version}

# lexicon 3.6.0 removed the xmltodict dependency (and the "plesk" extra)
Obsoletes: python3-%{pypi_name}+plesk < 3.6
Provides: python3dist(%{pypi_name}[plesk]) = %{version}
Provides: python%{python3_version}dist(%{pypi_name}[plesk]) = %{version}
%endif
# }}}

%description -n python3-%{pypi_name}
Lexicon provides a way to manipulate DNS records on multiple DNS providers in a
standardized way. Lexicon has a CLI but it can also be used as a python
library.

This is the Python 3 version of the package.

%package -n     python3-%{pypi_name}+gransy
Summary:        Meta-package for python3-%{pypi_name} and gransy provider
%{?python_provide:%python_provide python3-%{pypi_name}+gransy}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}+gransy
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the gransy provider.

%package -n     python3-%{pypi_name}+localzone
Summary:        Meta-package for python3-%{pypi_name} and localzone provider
%{?python_provide:%python_provide python3-%{pypi_name}+localzone}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}+localzone
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the localzone provider.

%package -n     python3-%{pypi_name}+oci
Summary:        Meta-package for python3-%{pypi_name} and oci provider
%{?python_provide:%python_provide python3-%{pypi_name}+oci}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}+oci
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the oci provider.

%package -n     python3-%{pypi_name}+route53
Summary:        Meta-package for python3-%{pypi_name} and Route 53 provider
%{?python_provide:%python_provide python3-%{pypi_name}+route53}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}+route53
This package installs no files. It requires python3-%{pypi_name} and all
dependencies necessary to use the Route 53 provider.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -f uv.lock

%generate_buildrequires
%if %{with extras}
%pyproject_buildrequires -r -t -e light -x gransy,localzone,oci,route53
%else
%pyproject_buildrequires -r
%endif

%build
# remove shebang
sed -i '1d' src/lexicon/_private/cli.py
%pyproject_wheel

%if %{with tests}
%check
export TLDEXTRACT_CACHE=%{_builddir}/tldextract-cache

# tldextract tries to fetch "public_suffix_list.dat" from the internet on first
# invocation.
# (see https://github.com/john-kurkowski/tldextract/tree/master#note-about-caching)
# The "publicsuffix-list" package provides that data however we need to use
# that to populate a local cache directory.Most of the work is done via:
#   $ tldextract --update --suffix_list_url "file:///usr/share/publicsuffix/public_suffix_list.dat"
#
# However tldextract uses the "file://" url as cache key while the tests use
# "https://publicsuffix.org/list/public_suffix_list.dat". I did not find a way
# get tldextract to use the https url so a small Python script will handle that.
/usr/bin/python3 %{SOURCE1} %{buildroot}%{python3_sitelib}

# lexicon providers which do not work in Fedora due to missing dependencies:
# - SoftLayerProviderTests
TEST_SELECTOR="not SoftLayerProviderTests"

%if %{without extras}
TEST_SELECTOR+=" and not GransyProviderTests and not LocalzoneProviderTests and not OciProviderTests and not OciInstancePrincipalProviderTests and not Route53ProviderTests"
%endif

# We do not use "--xfail-providers-with-missing-deps" because we want to detect
# missing dependencies unless we already know that a certain provider will not
# work.
%pytest -v -k "${TEST_SELECTOR}" -n auto --dist=loadfile tests/
%endif

%install
%pyproject_install
install -pm 0755 %{buildroot}/%{_bindir}/lexicon %{buildroot}/%{_bindir}/lexicon-%{python3_version}
cd %{buildroot}/%{_bindir}
ln -s lexicon-%{python3_version} lexicon-3

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/lexicon
%{_bindir}/lexicon-3
%{_bindir}/lexicon-%{python3_version}
%{python3_sitelib}/lexicon
%{python3_sitelib}/dns_lexicon-%{version}.dist-info

# Extras meta-packages
# {{{
%if %{with extras}

%files -n python3-%{pypi_name}+gransy
%{?python_extras_subpkg:%ghost %{python3_sitelib}/dns_lexicon-%{version}.dist-info}

%files -n python3-%{pypi_name}+localzone
%{?python_extras_subpkg:%ghost %{python3_sitelib}/dns_lexicon-%{version}.dist-info}

%files -n python3-%{pypi_name}+oci
%{?python_extras_subpkg:%ghost %{python3_sitelib}/dns_lexicon-%{version}.dist-info}

%files -n python3-%{pypi_name}+route53
%{?python_extras_subpkg:%ghost %{python3_sitelib}/dns_lexicon-%{version}.dist-info}

%endif
# }}}

%changelog
%autochangelog
