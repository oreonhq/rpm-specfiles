%global source0_hash c8ec5eb3a1dbd54f8285414a710bd023edb501946a48d9f37de8c835b7f44158
%bcond tests 1
Name:           mkdocs-bootstrap
Version:        1.1.1
Release:        1%{?dist}
Summary:        Bootstrap theme for MkDocs
License:        BSD-2-Clause
URL:            http://mkdocs.github.io/mkdocs-bootstrap/
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs-bootstrap/mkdocs-bootstrap-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mkdocs-bootstrap = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import
%if %{with tests}
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
mkdocs new testing
pushd testing
mkdocs build --theme bootstrap
popd
%endif
%files

%changelog

%autochangelog
