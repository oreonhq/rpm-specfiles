%global source0_hash 0e7d0c7f74ba33e6e80905e9bfd81f9d15ef9a790de97993e34213deb5ad10ac

# Enabled by default
%bcond_without tests

Name:           python-pytest-lazy-fixture
Version:        0.6.3
Release:        %autorelease
Summary:        Use fixtures in pytest.mark.parametrize

# spdx
License:        MIT
URL:            https://github.com/tvorog/pytest-lazy-fixture
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-lazy-fixture/pytest-lazy-fixture-0.6.3.tar.gz

# Minimal patch for compatibility with pytest 8.
# Downstream only patch, upstream seems dead.
# https://github.com/TvoroG/pytest-lazy-fixture/issues/65#issuecomment-1915829980
Patch:          Minimal-patch-for-compatibility-with-pytest-8.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Use fixtures in pytest.mark.parametrize.}

%description %_description

%package -n python3-pytest-lazy-fixture
Summary:        %{summary}

%description -n python3-pytest-lazy-fixture %_description

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -N -n pytest-lazy-fixture-%{version}

%if 0%{?rhel} == 0 || 0%{?rhel} > 10
%patch -P 0 -p1
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_lazyfixture

%check
%if %{with tests}
%pytest
%endif

%files -n python3-pytest-lazy-fixture -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.3-1
- Prepare for Oreon 11 (RP1)
