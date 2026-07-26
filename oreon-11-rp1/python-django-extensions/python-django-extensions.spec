%global source0_hash 3c88cbe14d3e60c88b4f49f185798647ba30d31235e74bb99ac2ab60bbfee808

# Build doc by default
%bcond_without doc

%global srcname django-extensions
%global modname django_extensions

Name:           python-%{srcname}
Version:        4.1
Release:        %autorelease
Summary:        Extensions for Django

License:        GPL-3.0-or-later
URL:            https://github.com/django-extensions/django-extensions
# PyPI tarball doesn't contain some requirements files
# Source0:        %%{pypi_source %%{srcname}}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{with doc}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
BuildRequires:  make
%endif

%global _description %{expand:
Django Extensions is a collection of custom extensions for the Django
Framework.}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%package -n python%{python3_pkgversion}-%{srcname}-doc
Summary:        Documentation for %{srcname}
Suggests:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}-doc %{_description}
This package contains the documentation for %{srcname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
# Remove commands incompatible with Python 3.12
%if 0%{?python3_version_nodots} >= 312
# https://github.com/django-extensions/django-extensions/issues/1831
rm django_extensions/management/commands/mail_debug.py
rm tests/management/commands/test_mail_debug.py
# https://github.com/django-extensions/django-extensions/issues/1832
rm django_extensions/management/commands/shell_plus.py
rm -r tests/management/commands/shell_plus_tests/
%endif
# Relax pytest requirement
sed -i 's|pytest<8|pytest|' requirements-dev.txt
# Remove coverage
sed -i /pytest-cov/d requirements-dev.txt
sed -i 's| --cov=.*"|"|' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%if %{with doc}
(cd docs && make html)
%endif

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
# tox.ini invokes make invokes pytest
# call directly so we can disable tests that require network
SELECTOR="not PipCheckerTests"
%if 0%{?el9}
# minor differences in generated HTML
# E   - </span><span class="s2">
# E   + </span><span class="w"><span class="s2">
# E   ?              ++++++++++++++++
SELECTOR+=" and not test_should_highlight_bash_syntax_without_name"
%endif
# >       self.assertEqual(with_no_flag, with_flag)
# E       AssertionError: {'cre[21 chars] 18:50', 'cli_options': 'django_extensions tes[39372 chars]}]}]} != {'cre[21 chars] 18:51', 'cli_optio
SELECTOR+=" and not test_graph_models_relation_fields_only"
%pytest -v django_extensions tests \
  -k "${SELECTOR}" \
  --ignore tests/test_dumpscript.py
# run this separately, see https://github.com/django-extensions/django-extensions/issues/1871
%pytest -v tests/test_dumpscript.py

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md CONTRIBUTING.md README.rst

%if %{with doc}
%files -n python%{python3_pkgversion}-%{srcname}-doc
%license LICENSE
%doc docs/_build/html/*
%endif

%changelog
%autochangelog
