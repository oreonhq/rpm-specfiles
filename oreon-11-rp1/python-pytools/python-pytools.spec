%global source0_hash cc2db25666aa64094d3fb4532aa8a7deaa2da8edd7340fb270ed1807dcc75202

%global srcname pytools

Name:           python-%{srcname}
Version:        2024.1.3
Release:        %autorelease
Summary:        Collection of tools for Python

License:        MIT
URL:            https://pypi.python.org/pypi/pytools
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description \
Pytools is a big bag of things that are "missing" from the Python standard\
library. This is mainly a dependency of my other software packages, and is\
probably of little interest to you unless you use those. If you're curious\
nonetheless, here's what's on offer:\
\
  * A ton of small tool functions such as `len_iterable`, `argmin`,\
    tuple generation, permutation generation, ASCII table pretty printing,\
    GvR's mokeypatch_xxx() hack, the elusive `flatten`, and much more.\
  * Michele Simionato's decorator module\
  * A time-series logging module, `pytools.log`.\
  * Batch job submission, `pytools.batchjob`.\
  * A lexer, `pytools.lex`.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(typing-extensions)
BuildRequires:  python3dist(platformdirs)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst PKG-INFO
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
