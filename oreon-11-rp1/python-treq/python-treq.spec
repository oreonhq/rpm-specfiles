%global source0_hash 43e728e12aca2d897c626cf07dc7b4392749b73de050a7d66e086cb3a6e15da9

%global pypi_name treq

%bcond doc 1

Name:           python-%{pypi_name}
Version:        26.7.0
Release:        1%{?dist}
Summary:        A requests-like API built on top of twisted.web's Agent

License:        MIT
URL:            https://github.com/twisted/treq
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-httpbin

%description
treq is an HTTP library inspired by requests but written on top of
Twisted’s Agents.
It provides a simple, higher level API for making HTTP requests
when using Twisted.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
treq is an HTTP library inspired by requests but written on top of
Twisted’s Agents.
It provides a simple, higher level API for making HTTP requests
when using Twisted.

%if %{with doc}
%package -n python-%{pypi_name}-doc
Summary:        treq documentation
%description -n python-%{pypi_name}-doc
Documentation for treq
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_doc:-x docs}

%build
%pyproject_wheel
%if %{with doc}
# generate html docs
export PYTHONPATH=%{python2_sitelib}:%{python3_sitelib}:src
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files treq

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%if %{with doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html
%endif

%changelog
%autochangelog
