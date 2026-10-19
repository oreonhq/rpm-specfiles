%global source0_hash 3c20ab00909419749061a4cb1a2755f034d10c1f6455adb1f03d7c16dedce711
%global pypi_name aiounittest
Name:           python-%{pypi_name}
Version:        1.5.0
Release:        6%{?dist}
Summary:        Test asyncio code more easily
License:        MIT
URL:            https://github.com/kwarunek/aiounittest
Source0:        https://files.pythonhosted.org/packages/source/a/aiounittest/aiounittest-%{version}.tar.gz
Patch:          https://github.com/kwarunek/aiounittest/pull/29.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aiounittest = %{version}-%{release}
# /oreon:deps
%description
The aiounittest is a helper library to ease your pain (and boilerplate),
when writing tests of asynchronous code (:code:asyncio). You can test:

- synchronous code (same as the :code:unittest.TestCase)
- asynchronous code, it supports syntax with async/await (Python 3.5+) and
  asyncio.coroutine/yield from (Python 3.4)

%package -n     python3-%{pypi_name}
Summary:        Test asyncio code more easily
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-%{pypi_name}
The aiounittest is a helper library to ease your pain (and boilerplate),
when writing tests of asynchronous code (:code:asyncio). You can test:

- synchronous code (same as the :code:unittest.TestCase)
- asynchronous code, it supports syntax with async/await (Python 3.5+) and
  asyncio.coroutine/yield from Python 3.4

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/aiounittest* usr/lib64/python3*/site-packages/aiounittest* usr/bin/*

%check

%pytest -v
%files
%files -n python3-aiounittest -f %{oreon_filedir}/python3-aiounittest.list

%changelog

%autochangelog
