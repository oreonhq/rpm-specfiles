%global source0_hash 5a826ed84cc0afa202eb9e44381d7d762f7bdda8e0c23f9f79a7f1f44cf4a895
Name:           python-pytest-console-scripts
Version:        1.4.1
Release:        1%{?dist}
Summary:        Pytest plugin for testing console scripts
License:        MIT
URL:            https://github.com/kvas-it/pytest-console-scripts
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-console-scripts/pytest-console-scripts-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-console-scripts = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-console-scripts
Summary:        Pytest plugin for testing console scripts
Requires:       python3-setuptools
%description -n python3-pytest-console-scripts

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-console-scripts-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-console-scripts usr/lib/python3*/site-packages/pytest_console_scripts* usr/lib64/python3*/site-packages/pytest_console_scripts* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_console_scripts* usr/lib64/python3*/site-packages/pytest_console_scripts* usr/bin/*

%check

%tox
%files
%files -n python3-pytest-console-scripts -f %{oreon_filedir}/python3-pytest-console-scripts.list

%changelog

%autochangelog
