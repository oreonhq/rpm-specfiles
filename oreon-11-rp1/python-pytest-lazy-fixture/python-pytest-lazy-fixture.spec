%global source0_hash 0e7d0c7f74ba33e6e80905e9bfd81f9d15ef9a790de97993e34213deb5ad10ac
%bcond_without tests
Name:           python-pytest-lazy-fixture
Version:        0.6.3
Release:        1%{?dist}
Summary:        Use fixtures in pytest.mark.parametrize
License:        MIT
URL:            https://github.com/tvorog/pytest-lazy-fixture
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-lazy-fixture/pytest-lazy-fixture-0.6.3.tar.gz
Patch:          Minimal-patch-for-compatibility-with-pytest-8.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-lazy-fixture = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pytest-lazy-fixture
Summary:        Use fixtures in pytest.mark.parametrize
%description -n python3-pytest-lazy-fixture

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-lazy-fixture-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-lazy-fixture usr/lib/python3*/site-packages/pytest_lazy_fixture* usr/lib64/python3*/site-packages/pytest_lazy_fixture* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_lazy_fixture* usr/lib64/python3*/site-packages/pytest_lazy_fixture* usr/bin/*

%check

%if %{with tests}
%pytest
%endif
%files
%files -n python3-pytest-lazy-fixture -f %{oreon_filedir}/python3-pytest-lazy-fixture.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.3-1
- Prepare for Oreon 11 (RP1)
