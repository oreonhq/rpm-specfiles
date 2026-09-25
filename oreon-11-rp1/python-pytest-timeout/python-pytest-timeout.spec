%global source0_hash 68c9d82dfe95fa65712e107010c9344e7d8b4afe8c975a7be0d273d939583a93

%global pypi_name pytest_timeout

Name:           python-pytest-timeout
Version:        2.5.0
Release:        1%{?dist}
Summary:        py.test plugin to abort hanging tests

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pytest-timeout
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_timeout/pytest_timeout-2.5.0.tar.gz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%autochangelog
