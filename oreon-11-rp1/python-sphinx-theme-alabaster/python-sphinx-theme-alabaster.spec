%global source0_hash c00dca57bca26fa62a6d7d0a9fcce65f3e026e9bfe33e9c538fd3fbb2144fd9e

Name:           python-sphinx-theme-alabaster
Version:        1.0.0
Release:        %autorelease
Summary:        Configurable sidebar-enabled Sphinx theme

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/alabaster
Source:        https://files.pythonhosted.org/packages/source/a/alabaster/alabaster-1.0.0.tar.gz
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

# Upstream lists no runtime dependencies,
# but alabaster/support.py imports from pygments.
# This is fine, as the module is only used for pygments.
# This BuildRequires is necessary for a successful import check.
BuildRequires:  python%{python3_pkgversion}-pygments

%global _description %{expand:
Alabaster is a visually (c)lean, responsive, configurable theme for the Sphinx
documentation system.

It began as a third-party theme, and is still maintained separately,
but as of Sphinx 1.3, Alabaster is an install-time dependency of Sphinx and is
selected as the default theme.}

%description %_description


%package -n     python%{python3_pkgversion}-sphinx-theme-alabaster
Summary:        %{summary}
%py_provides    python%{python3_pkgversion}-alabaster

%description -n python%{python3_pkgversion}-sphinx-theme-alabaster %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n alabaster-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files alabaster


%check
# upstream has no tests
%pyproject_check_import


%files -n python%{python3_pkgversion}-sphinx-theme-alabaster -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
