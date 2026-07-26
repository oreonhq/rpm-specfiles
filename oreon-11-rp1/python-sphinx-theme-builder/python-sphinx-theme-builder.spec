%global source0_hash bda380fc73be4fd872a79d4148d7fccbac778639f9b6dfff0fdaf9d255f3e493

# This package serves both as a build backend and a tool for theme developers.
# During the Python bootstrap we need the build functionality for python-furo.
# cli extra, needed for the application usage, has got a long chain of
# dependencies leading ultimately to python-django which can be built much
# later in the bootstrap process, hence the bcond to build just the "core" parts.
%bcond bootstrap 0

%global giturl  https://github.com/pradyunsg/sphinx-theme-builder

Name:           python-sphinx-theme-builder
Version:        0.3.2
Release:        %autorelease
Summary:        Streamline the Sphinx theme development workflow

# Most of the code is MIT.  However,
# src/sphinx_theme_builder/_internal/passthrough.py is BSD-3-Clause.
License:        MIT AND BSD-3-Clause
URL:            https://sphinx-theme-builder.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/sphinx-theme-builder-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
%{!?with_bootstrap:BuildOption(generate_buildrequires): -x cli tests/requirements.txt}
BuildOption(install): -l sphinx_theme_builder

BuildRequires:  help2man

%description
A tool for authoring Sphinx themes with a simple (opinionated) workflow.

%package     -n python3-sphinx-theme-builder
Summary:        Streamline the Sphinx theme development workflow

%description -n python3-sphinx-theme-builder
A tool for authoring Sphinx themes with a simple (opinionated) workflow.

%if %{without bootstrap}
%pyproject_extras_subpkg -n python3-sphinx-theme-builder cli
%{_bindir}/stb
%{_mandir}/man1/stb.1*
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sphinx-theme-builder-%{version} -p1

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

# Skip test packages not available in Fedora
sed -i '/pytest-/d' tests/requirements.txt

%install -a
%if %{without bootstrap}
# Install a man page
mkdir -p %{buildroot}%{_mandir}/man1
%{py3_test_envvars} help2man -N --version-string=%{version} \
  -n 'Streamline the Sphinx theme development workflow' \
  %{buildroot}%{_bindir}/stb > %{buildroot}%{_mandir}/man1/stb.1
%else
# without cli there's no use of the binary file
rm %{buildroot}%{_bindir}/stb
%endif

%check
%if %{without bootstrap}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-sphinx-theme-builder -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
