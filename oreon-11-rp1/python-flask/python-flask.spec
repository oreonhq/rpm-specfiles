%global source0_hash 0ef0e52b8a9cd932855379197dd8f94047b359ca0a78695144304cb45f87c9eb

%global modname flask
%global srcname flask

%bcond doc 0

Name:           python-%{modname}
Version:        3.1.3
Release:        %autorelease
Epoch:          1
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions

License:        BSD-3-Clause
URL:            http://flask.pocoo.org/
Source0:        https://files.pythonhosted.org/packages/source/f/flask/flask-3.1.3.tar.gz#/python-flask-3.1.3.tar.gz

BuildArch:      noarch

%global _description \
Flask is called a “micro-framework” because the idea to keep the core\
simple but extensible. There is no database abstraction layer, no form\
validation or anything else where different libraries already exist\
that can handle that. However Flask knows the concept of extensions\
that can add this functionality into your application as if it was\
implemented in Flask itself. There are currently extensions for object\
relational mappers, form validation, upload handling, various open\
authentication technologies and more.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  make
BuildRequires:  python3-devel

%description -n python3-%{modname} %{_description}

Python 3 version.

%if %{with doc}
%package doc
Summary:        Documentation for %{name}

%description doc
Documentation and examples for %{name}.
%endif

%pyproject_extras_subpkg -n python3-%{modname} async
%generate_buildrequires
# -t picks test.txt by default which contains too tight pins
%pyproject_buildrequires -x async -g tests %{?with_doc:-g docs}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}
# Allow to use python-sphinx>=9
sed -i 's/sphinx<9/sphinx/g' pyproject.toml

rm -rf examples/flaskr/
rm -rf examples/minitwit/
# Do some shuffling to work on f42 and epel10
sed -i 's|license = "BSD-3-Clause"|license = {file = "LICENSE.txt"}|' pyproject.toml
sed -i '/^license-files = \["LICENSE.txt"\]/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

mv %{buildroot}%{_bindir}/%{modname}{,-%{python3_version}}
ln -s %{modname}-%{python3_version} %{buildroot}%{_bindir}/%{modname}-3
ln -sf %{modname}-3 %{buildroot}%{_bindir}/%{modname}

%if %{with doc}
pushd docs
# PYTHONPATH to prevent "'Flask' must be installed to build the documentation."
make PYTHONPATH=%{buildroot}/%{python3_sitelib} SPHINXBUILD=sphinx-build-3 html
rm -v _build/html/.buildinfo
popd
%endif

%check
%pytest -Wdefault -k 'not test_bad_environ_raises_bad_request'

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGES.rst README.md
%{_bindir}/%{modname}
%{_bindir}/%{modname}-3
%{_bindir}/%{modname}-%{python3_version}

%if %{with doc}
%files doc
%license LICENSE.txt
%doc docs/_build/html examples
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.3-1
- Prepare for Oreon 11 (RP1)
