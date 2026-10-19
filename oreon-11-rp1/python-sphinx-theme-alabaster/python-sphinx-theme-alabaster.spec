%global source0_hash c00dca57bca26fa62a6d7d0a9fcce65f3e026e9bfe33e9c538fd3fbb2144fd9e
Name:           python-sphinx-theme-alabaster
Version:        1.0.0
Release:        1%{?dist}
Summary:        Configurable sidebar-enabled Sphinx theme
License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/alabaster
Source0:        https://files.pythonhosted.org/packages/source/a/alabaster/alabaster-1.0.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.7
Requires:       python3-sphinx-theme-alabaster = %{version}-%{release}
# /oreon:deps
%description

%package -n     python%{python3_pkgversion}-sphinx-theme-alabaster
Summary:        Configurable sidebar-enabled Sphinx theme
%py_provides    python%{python3_pkgversion}-alabaster
%description -n python%{python3_pkgversion}-sphinx-theme-alabaster

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir alabaster-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_theme_alabaster* usr/lib64/python3*/site-packages/sphinx_theme_alabaster* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-sphinx-theme-alabaster -f %{oreon_filedir}/python3-sphinx-theme-alabaster.list

%changelog

%autochangelog
