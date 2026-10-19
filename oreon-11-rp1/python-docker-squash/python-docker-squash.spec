%global source0_hash 7316fd1fb4d39167ffdc0866494cdcc3ab2c25175b6a0adcf8954300e4b4850c
%global modname docker-squash
Name:           python-%{modname}
Version:        1.2.2
Release:        1%{?dist}
Summary:        Docker layer squashing tool
License:        MIT
URL:            https://github.com/goldmann/docker-squash
Source0:        https://github.com/goldmann/%{modname}/archive/refs/tags/%{version}.tar.gz
Patch0:         python-docker-squash-rm-python-mock-usage.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-docker
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
# /oreon:deps
%description

%package -n python3-%{modname}
Summary:        Docker layer squashing tool
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
%description -n python3-%{modname}

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-docker-squash -f %{oreon_filedir}/python3-docker-squash.list

%changelog

%autochangelog
