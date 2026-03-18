%global srcname pid

%global common_description %{expand:
pid provides a PidFile class that manages PID files. PidFile features:
  - stale detection
  - locking using fcntl
  - chmod (default is 0o644)
  - chown
  - custom exceptions

PidFile can also be used as a context manager or a decorator.}

Name:           python-%{srcname}
Version:        3.0.4
Release:        5%{?dist}
Summary:        PID file management library

License:        Apache-2.0
URL:            https://github.com/trbs/pid
Source0:        %pypi_source

BuildArch:      noarch

%description %{common_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel

# Test dependencies
BuildRequires:  python3dist(pytest)

%description -n python%{python3_pkgversion}-%{srcname} %{common_description}

%prep
# This needs to have a blank line after because of a bug in the EL6 macros
%autosetup -p1 -n %{srcname}-%{version}

rm -rf %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS CHANGELOG README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.4-5
- Prepare for Oreon 11 (RP1)
