%global source0_hash 0ef0e52b8a9cd932855379197dd8f94047b359ca0a78695144304cb45f87c9eb
%global modname flask
%global srcname flask
%bcond doc 0
Name:           python-%{modname}
Version:        3.1.3
Release:        1%{?dist}
Epoch:          1
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
License:        BSD-3-Clause
URL:            http://flask.pocoo.org/
Source0:        https://files.pythonhosted.org/packages/source/f/flask/flask-3.1.3.tar.gz#/python-flask-3.1.3.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-flask = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{modname}
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
BuildRequires:  make
BuildRequires:  python3-devel
%description -n python3-%{modname}

Python 3 version.

%if %{with doc}
%package doc
Summary:        Documentation for %{name}
%description doc
Documentation and examples for %{name}.
%endif

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
mv %{buildroot}%{_bindir}/%{modname}{,-%{python3_version}}
ln -s %{modname}-%{python3_version} %{buildroot}%{_bindir}/%{modname}-3
ln -sf %{modname}-3 %{buildroot}%{_bindir}/%{modname}
%if %{with doc}
pushd docs
make PYTHONPATH=%{buildroot}/%{python3_sitelib} SPHINXBUILD=sphinx-build-3 html
rm -v _build/html/.buildinfo
popd
%oreon_autofiles main usr/lib/python3*/site-packages/flask* usr/lib64/python3*/site-packages/flask* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%pytest -Wdefault -k 'not test_bad_environ_raises_bad_request'
%files
%files -n python3-flask -f %{oreon_filedir}/python3-flask.list
%files -n python-flask-doc -f %{oreon_filedir}/python-flask-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.3-1
- Prepare for Oreon 11 (RP1)
