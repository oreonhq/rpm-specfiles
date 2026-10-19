%global source0_hash a8d728f0a29de45dc521f18f07297428d56992a742f0cd2701ba86e44d23d5b2
Name:           python-aiofiles
Version:        25.1.0
Release:        1%{?dist}
Summary:        File support for asyncio
License:        Apache-2.0
URL:            https://github.com/Tinche/aiofiles
Source0:        https://files.pythonhosted.org/packages/source/a/aiofiles/aiofiles-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aiofiles = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-aiofiles
Summary:        File support for asyncio
%description -n python3-aiofiles

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n aiofiles-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem dependency-groups.test 'coverage.*'

%if %[ %{defined fc41} || %{defined fc42} || %{defined el10} ]
# Allow older pytest/pytest-asyncio (remove minimum versions)
for dep in pytest pytest-asyncio
do
  tomcli set pyproject.toml lists replace dependency-groups.test \
      "${dep} *>.*" "${dep}"
done
tomcli set pyproject.toml del tool.pytest.ini_options.minversion
%endif

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aiofiles usr/lib/python3*/site-packages/aiofiles* usr/lib64/python3*/site-packages/aiofiles* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aiofiles* usr/lib64/python3*/site-packages/aiofiles* usr/bin/*

%check

%pytest
%files
%files -n python3-aiofiles -f %{oreon_filedir}/python3-aiofiles.list

%changelog

%autochangelog
