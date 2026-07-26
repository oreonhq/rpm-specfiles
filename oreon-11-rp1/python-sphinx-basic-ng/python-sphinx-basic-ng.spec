%global source0_hash 1430e3f9e120f54c0dfb78a7c9b19b0f61f7910ddefff7d9bb457f78d6e350e2

# The documentation and tests need furo.  But to build furo at all, we need
# this package.
%bcond bootstrap 0

%global prerel  beta2
%global giturl  https://github.com/pradyunsg/sphinx-basic-ng

Name:           python-sphinx-basic-ng
Version:        1.0.0
Release:        0.19.%{prerel}%{?dist}
Summary:        Modernized skeleton for Sphinx themes

License:        MIT
URL:            https://sphinx-basic-ng.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}.%{prerel}/sphinx-basic-ng-%{version}.%{prerel}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
%if %{without bootstrap}
BuildOption(generate_buildrequires): -x docs
%endif
BuildOption(install): -l sphinx_basic_ng

%if %{without bootstrap}
BuildRequires:  python-sphinx-doc
BuildRequires:  python3-docs
%endif

%global _description A modernized skeleton for Sphinx themes.

%description
%_description

%package     -n python3-sphinx-basic-ng
Summary:        Modernized skeleton for Sphinx themes

%description -n python3-sphinx-basic-ng
%_description

%if %{without bootstrap}
%package        doc
Summary:        Documentation for %{name}
# This project is MIT.  Other files bundled with the documentation have the
# following licenses:
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/check-solid.svg: MIT
# _static/clipboard.min.js: MIT
# _static/copy-button.svg: MIT
# _static/copybutton.css: MIT
# _static/copybutton.js: MIT
# _static/copybutton_funcs.js: MIT
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/scripts/furo*: MIT
# _static/searchtools.js: BSD-2-Clause
# _static/styles/furo*: MIT
# _static/tabs.css: MIT
# _static/tabs.js: MIT
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        MIT AND BSD-2-Clause

%description    doc
Documentation for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sphinx-basic-ng-%{version}.%{prerel}

%conf
# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

%build -a
%if %{without bootstrap}
# Build documentation
PYTHONPATH=$PWD/src sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}
%endif

%check
# The nox tests require network access, so we do not run them
%pyproject_check_import

%files -n python3-sphinx-basic-ng -f %{pyproject_files}
%doc README.md

%if %{without bootstrap}
%files doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
