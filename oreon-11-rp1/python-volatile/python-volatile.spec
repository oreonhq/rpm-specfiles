%global source0_hash 88e8268a435ce311ad54704aa57b8888ce619503b08744c573909f5e6b439f5e

%global srcname volatile

Name:           python-%{srcname}
Version:        2.1.0
Release:        21%{?dist}
Summary:        A small extension for the tempfile module
License:        MIT
URL:            https://github.com/mbr/volatile
# pypi_source does not contain the license text
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Temporary files and directories.

Contains replacement for tempfile.NamedTemporaryFile that does not delete the
file on close(), but still unlinks it after the context manager ends, as well as
a mkdtemp-based temporary directory implementation.

- Mostly reuses the stdlib implementations, supporting the same signatures.
- Due to that, uses the OS’s built-in temporary file facilities, no custom
  schemes.
- Tested on Python 2.6+ and 3.3+}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
