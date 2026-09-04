%global source0_hash e372fd82588ec11ce94ec7e3a1659617feb3f17306df404197e2574d13536d71
%global modname cssselect

%bcond_without tests

Name:           python-cssselect
Version:        1.5.0
Release:        %autorelease
Summary:        Parses CSS3 Selectors and translates them to XPath 1.0

License:        BSD-3-Clause
URL:            https://github.com/scrapy/cssselect
Source0:        https://github.com/scrapy/cssselect/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Cssselect parses CSS3 Selectors and translates them to XPath 1.0 expressions.\
Such expressions can be used in lxml or another XPath engine to find the\
matching elements in an XML or HTML document.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:	python3dist(tox-current-env) >= 0.0.16

%description -n python3-%{modname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%if %{with tests}
%check
%pytest
%endif

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGES AUTHORS

%changelog
%autochangelog
