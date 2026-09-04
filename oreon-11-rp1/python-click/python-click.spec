%global source0_hash df2fb64b9c3f0b5fbf65f1b69dd164cd2d8e7d5d8f6ee3abdafcff7fe2d63719

%bcond tests 1

Name:           python-click
Epoch:          1
Version:        8.5.0
Release:        %autorelease
Summary:        Simple wrapper around optparse for powerful command line utilities

License:        BSD-3-Clause
URL:            https://github.com/pallets/click
Source0:        https://github.com/pallets/click/archive/refs/tags/8.3.1.tar.gz#/click-8.3.1.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

%global _description \
click is a Python package for creating beautiful command line\
interfaces in a composable way with as little amount of code as necessary.\
It's the "Command Line Interface Creation Kit".  It's highly configurable but\
comes with good defaults out of the box.

%description %{_description}


%package -n     python%{python3_pkgversion}-click
Summary:        %{summary}

%description -n python%{python3_pkgversion}-click %{_description}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n click-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g tests}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files click


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-click -f %pyproject_files
%license LICENSE.txt
%doc README.md CHANGES.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.3.1-1
- Prepare for Oreon 11 (RP1)
