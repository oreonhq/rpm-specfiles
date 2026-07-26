%global source0_hash c2a8da9fc358afe98f93e8562493dd23bc25daad9612f95f4979359348788d1a

%global modname docker-squash

Name:           python-%{modname}
Version:        1.1.0
Release:        14%{?dist}
Summary:        Docker layer squashing tool
License:        MIT
URL:            https://github.com/goldmann/docker-squash
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
# Maintainers, please upstream
Patch0:         python-docker-squash-rm-python-mock-usage.patch

BuildArch:      noarch

%global _description \
Tool to squash layers in Docker images.

%description %_description

%package -n python3-%{modname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  python3-docker
Requires:       python3-six
Requires:       python3-docker

Provides:       python3-docker-scripts = %{version}-%{release}
Obsoletes:      python3-docker-scripts <= 1.0.0-0.2.rc2
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname} %_description

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

%build
%py3_build

%check
py.test-%{python3_version} -v tests/test_unit*.py

%install
%py3_install

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{_bindir}/docker-squash
%{python3_sitelib}/docker_squash/
%{python3_sitelib}/docker_squash-*.egg-info/

%changelog
%autochangelog
