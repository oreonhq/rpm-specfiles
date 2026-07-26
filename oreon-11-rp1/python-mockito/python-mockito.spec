%global source0_hash 599356409c790bc663d51a076696d59b84789acd013207355d98a47dd040389f

%global pypi_name mockito

Summary:        Python spying framework inspired by Java's Mockito
Name:           python-mockito
Version:        1.5.0
Release:        7%{?dist}
License:        MIT
URL:            https://github.com/kaste/%{pypi_name}-python
Source0:        %{url}/archive/%{version}/%{pypi_name}-python-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

%global _description %{expand:
This spying framework allows to easily create mocks with a very readable syntax.}

%description
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-python-%{version}

%build
%{py3_build}

%check
%pytest

%install
%{py3_install}

%package -n python3-mockito
Summary: %{summary}

%description -n python3-mockito
%{_description}

%files -n python3-mockito
%doc AUTHORS
%doc CHANGES.txt
%doc README.rst
%{python3_sitelib}/mockito/
%{python3_sitelib}/mockito-*.egg-info
%license LICENSE

%changelog
%autochangelog
