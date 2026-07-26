%global source0_hash 225dee0acfcc71de8c6f7cef9c618e5a9d3e7baa7ae1470b8d076a064033c463

%global pkg_name protego
%global pypi_name protego
%global desc %{expand:
Protego is a pure-Python `robots.txt` parser with support for modern
conventions.}

Name:		python-protego
Version:	0.5.0
Release:	3%{?dist}
Summary:	Pure-Python robots.txt parser with support for modern conventions

License:	BSD-3-Clause
URL:		https://github.com/scrapy/protego
Source0:	%{pypi_source}

BuildArch:	noarch
BuildRequires:	python3dist(pytest)

%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}

%description -n python3-%{pkg_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/protego
%{python3_sitelib}/protego-*.dist-info

%changelog
%autochangelog
