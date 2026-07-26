%global source0_hash e162614f917c89132d80a07de7c7597467a9024eaecc86da9b9bf4302a95ea1b

%global pypi_name mechanicalsoup

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        5%{?dist}
Summary:        Python library for automating interaction with websites

License:        MIT
URL:            https://mechanicalsoup.readthedocs.io
Source0:        https://github.com/MechanicalSoup/MechanicalSoup/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
MechanicalSoup automatically stores and sends cookies, follows redirects,
and can follow links and submit forms. It doesn't do JavaScript.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-httpbin)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(requests-mock)

%description -n python3-%{pypi_name}
MechanicalSoup automatically stores and sends cookies, follows redirects,
and can follow links and submit forms. It doesn't do JavaScript.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n MechanicalSoup-%{version}
# No linting
sed -i -e 's/--flake8//g' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
