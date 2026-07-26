%global source0_hash 23d2d9d457bc62dd737d6f7481588f05c3dc4d023086e6af16e9bdb419788b81

%global pypi_name scitokens

Name:           python-%{pypi_name}
Version:        1.9.7
Release:        1%{?dist}
Summary:        SciToken reference implementation library

License:        Apache-2.0
URL:            https://scitokens.org
Source0:        %pypi_source %{pypi_name}
BuildArch:      noarch
Prefix:         %{_prefix}

# build requirements
BuildRequires:  python3-devel
BuildRequires:  python3dist(wheel)
%if 0%{?rhel} >= 9
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tomli)
%else
# EL8 does not support pyproject-rpm-macros or tomli by default
BuildRequires:  python3-setuptools
%endif

# test requirements
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pyjwt) >= 1.6.1
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)

%description
SciToken reference implementation library

%package -n     python3-%{pypi_name}
Obsoletes:      python3-scitokens < 1.6.2-2
Summary:        %{summary}

%description -n python3-%{pypi_name}
SciToken reference implementation library

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%if 0%{?rhel} >= 9
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?rhel} >= 9
%py3_build_wheel
%else
%py3_build
%endif

%install
%if 0%{?rhel} >= 9
%py3_install_wheel %{pypi_name}-%{version}-*.whl
%else
%py3_install
%endif

%check
%pytest --verbose -ra tests/ --no-network --no-intensive

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/scitokens-admin-create-key
%{_bindir}/scitokens-admin-create-token
%{_bindir}/scitokens-verify-token

%changelog
%autochangelog
