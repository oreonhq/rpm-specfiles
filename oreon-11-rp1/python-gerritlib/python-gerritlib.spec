%global source0_hash 0390d5cafe813a7033bdf79f1ca12a80ebbe8331b3dc2eddb96acda17d3ec624

%global pypi_name gerritlib
%global desc A Python library for interacting with Gerrit

%global commit dc754757abd466cbf2cc74bcf5ab7094f53a2426
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%dnl %global gitrelease 20240620git%{shortcommit}
%dnl %global pre ~pre
%global __python3 PBR_VERSION=%{version} %{__python3}

Name:           python-%{pypi_name}
Version:        0.11.0
Release:        8%{?pre:}%{?gitrelease:}%{?dist}
Summary:        Client library for accessing Gerrit
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://opendev.org/opendev/gerritlib/
Source:         https://opendev.org/opendev/gerritlib/archive/%{commit}.tar.gz#/%{pypi_name}-%{commit}.tar.gz

# building from gitea tarball doesn't have the information required to create these
# to refresh, checkout the upstream git commit and run python setup.py sdist
# and extract AUTHORS and ChangeLog files
Source:        AUTHORS
Source:        ChangeLog

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-hacking
BuildRequires:  python3-paramiko

# Test dependencies:
BuildRequires: python3dist(nox)
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(python-subunit)
BuildRequires: python3dist(stestr)

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3-pbr
Requires:       python3-paramiko
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}
sed -i 's/\r//' LICENSE

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# We handle requirements ourselves, remove requirements.txt
rm -rf requirements.txt test-requirements.txt

# building from gitea tarball doesn't have the information required to create these
cp %{SOURCE1} AUTHORS
cp %{SOURCE2} ChangeLog

%build
%py3_build

%install
%py3_install

%check
%{py3_test_envvars} %{python3} -m nox --non-interactive --no-venv -k "tests and not lint" --no-install

%files -n python3-%{pypi_name}
%doc README.rst AUTHORS ChangeLog
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
%autochangelog
