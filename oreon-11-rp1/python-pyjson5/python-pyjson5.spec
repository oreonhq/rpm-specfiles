%global source0_hash 7ccc98586cf87dfeadfa76de8df4c9cb0c3d21d1b559e28812dd9633748d6e25

Name:           python-pyjson5
Version:        2.0.0
Release:        %autorelease
Summary:        JSON5 serializer and parser for Python 3 written in Cython

License:        Apache-2.0 AND MIT AND BSL-1.0
URL:            https://github.com/Kijewski/pyjson5
Source0:        %{pypi_source pyjson5}
Source1:        https://docs.python.org/%{python3_version}/objects.inv
Patch0:         flags.patch

BuildRequires:  python3-devel
BuildRequires:  gcc-c++
# Documentation
BuildRequires:  graphviz
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  texinfo
Provides:       bundled(fast_double_parser)

%global _description %{expand:
The serializer returns ASCII data that can safely be used in an HTML template.}

%description %_description

%package -n     python3-pyjson5
Summary:        %{summary}

%description -n python3-pyjson5 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyjson5-%{version}

cp %{SOURCE1} docs/
sed -i "s|('https://docs.python.org/3.14', None)|('objects.inv', None)|g"  docs/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
ls %_pyproject_wheeldir
TMPDIR="%{_pyproject_builddir}" %{python3} -m pip install --user --no-deps %_pyproject_wheeldir/*.whl
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook pyjson5.texi	
popd	
popd

%install
%pyproject_install
%pyproject_save_files -l pyjson5

mkdir -p %{buildroot}%{_datadir}/help/en/python-pyjson5
install -m644 docs/texinfo/pyjson5.xml %{buildroot}%{_datadir}/help/en/python-pyjson5

%check
%pyproject_check_import
PYTHONPATH="${PYTHONPATH}:%{buildroot}%{python3_sitearch}" %python3 ./scripts/run-tests.py
PYTHONPATH="${PYTHONPATH}:%{buildroot}%{python3_sitearch}" %python3 ./scripts/run-minefield-test.py

%files -n python3-pyjson5 -f %{pyproject_files}
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-pyjson5

%changelog
%autochangelog
