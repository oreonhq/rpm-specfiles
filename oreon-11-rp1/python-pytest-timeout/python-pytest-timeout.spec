%global pypi_name pytest_timeout

Name:           python-pytest-timeout
Version:        2.4.0
Release:        6%{?dist}
Summary:        py.test plugin to abort hanging tests

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pytest-timeout
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This is a plugin which will terminate tests after a certain timeout. When doing
so it will show a stack dump of all threads running at the time. This is useful
when running tests under a continuous integration server or simply if you don’t
know why the test suite hangs.}

%description %_description

%package -n     python3-pytest-timeout
Summary:        %{summary}

%description -n python3-pytest-timeout %_description

%prep
%autosetup -p1 -n pytest_timeout-%{version}
# python-ipdb FTBFS currently
sed -i -e '/\s*ipdb$/d' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_timeout

%check
%tox


%files -n python3-pytest-timeout -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.0-6
- Prepare for Oreon 11 (RP1)
