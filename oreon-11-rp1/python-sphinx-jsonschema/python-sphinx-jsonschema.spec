%global source0_hash 6501304887e7cece3139c2cffec9bcb41085a2d60bf02aba61a8fcaa98dcb3f1
%bcond_without doc
%bcond_with tests
Name:           python-sphinx-jsonschema
Version:        1.19.2
Release:        1%{?dist}
Summary:        Sphinx extension to display JSON Schema
License:        GPL-3.0-only
URL:            https://github.com/lnoor/sphinx-jsonschema
Source0:        https://github.com/lnoor/sphinx-jsonschema/archive/v.%{version}/sphinx-jsonschema-%{version}.tar.gz
BuildArch:      noarch
%if %{with doc}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinx-jsonschema = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx-jsonschema
Summary:        Sphinx extension to display JSON Schema
%description -n python3-sphinx-jsonschema

%if %{with doc}
%package        doc
Summary:        Documentation for sphinx-jsonschema
%description    doc
This package contains the documentation for sphinx-jsonschema.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinx-jsonschema-v.%{version}
%oreon_prep
%build

%pyproject_wheel
%if %{with doc}
PYTHONPATH=$PWD make -C docs html
%endif
%install
%pyproject_install
%oreon_autofiles python3-sphinx-jsonschema usr/lib/python3*/site-packages/sphinx_jsonschema* usr/lib64/python3*/site-packages/sphinx_jsonschema* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_jsonschema* usr/lib64/python3*/site-packages/sphinx_jsonschema* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import sphinx-jsonschema
%if %{with tests}
%tox
%endif
%files
%files -n python3-sphinx-jsonschema -f %{oreon_filedir}/python3-sphinx-jsonschema.list
%files -n python-sphinx-jsonschema-doc -f %{oreon_filedir}/python-sphinx-jsonschema-doc.list

%changelog

%autochangelog
