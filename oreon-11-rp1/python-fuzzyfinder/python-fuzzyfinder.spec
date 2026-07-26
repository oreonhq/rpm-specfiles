%global source0_hash c56d86f110866becad6690c7518f7036c20831c0f82fc87eba8fdb943132f04b

%{?python_enable_dependency_generator}
%global srcname fuzzyfinder

Name:           python-%{srcname}
Version:        2.1.0
Release:        31%{?dist}
Summary:        Fuzzy Finder implemented in Python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/amjith/fuzzyfinder
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description \
%{summary}. Matches partial string entries from a list\
of strings. Works similar to fuzzy finder in SublimeText and\
Vim’s Ctrl-P plugin.

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info/

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-3 -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
