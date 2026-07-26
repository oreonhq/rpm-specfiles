%global source0_hash 6a9b2049cf7b2ac52f85354272db667b4db7b5c1569a5e47fe7273275cfc1b56

%{?python_enable_dependency_generator}

%global modname rply

Name:           python-%{modname}
Version:        0.7.8
Release:        18%{?dist}
Summary:        Port David Beazley's PLY to RPython

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/alex/rply
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3dist(appdirs)

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}
sed -i "s/import py/import pytest/" tests/test_*
sed -i "s/py\.test/pytest/" tests/test_*

%build
%py3_build

%install
%py3_install

%check
pytest-%{python3_version} -v

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
%autochangelog
