%global pypi_name pytest_timeout

Name:           python-pytest-timeout
Version:        2.4.0
Release:        6%{?dist}
Summary:        py.test plugin to abort hanging tests

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pytest-timeout
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_timeout/pytest_timeout-2.4.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 7e68e90b01f9eff71332b25001f85c75495fc4e3a836701876183c4bcfd0540a
%global source0_file pytest_timeout-2.4.0.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pytest_timeout-2.4.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7e68e90b01f9eff71332b25001f85c75495fc4e3a836701876183c4bcfd0540a" || { echo "oreon: Source0 SHA256 mismatch for pytest_timeout-2.4.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
