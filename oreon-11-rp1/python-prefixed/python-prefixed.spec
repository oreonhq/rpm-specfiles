%global source0_hash d10ac90acfc4cc14d82c1408b330b2fda85ed7cec2206a800d43899f8c385265

%global pypi_name prefixed
%global desc %{expand:
Prefixed provides an alternative implementation of the built-in float which
supports formatted output with SI (decimal) and IEC (binary) prefixes.}

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        9%{?dist}
Summary:        Prefixed alternative numeric library

License:        MPL-2.0
URL:            https://github.com/Rockhopper-Technologies/prefixed
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-devel

%description %{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest

%files -n python3-%{pypi_name}
%doc README*
%license LICENSE
%{python3_sitelib}/prefixed*

%changelog
%autochangelog
