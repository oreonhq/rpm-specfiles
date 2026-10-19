%global source0_hash 5a1fcefcfc40b82e39a2a1947324d48fcd77bd78915602bd22c4cfcc372ba94b
Name:           python-manuel
Version:        1.13.0
Release:        1%{?dist}
Summary:        Build tested documentation
License:        Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://pypi.python.org/pypi/manuel
Source0:        https://github.com/benji-york/manuel/archive/%{version}/manuel-%{version}.tar.gz
Patch0:         %{name}-test.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-manuel = %{version}-%{release}
# /oreon:deps
%description
Manuel lets you mix and match traditional doctests with custom test
syntax.  Several plug-ins are included that provide new test syntax.
You can also create your own plug-ins.

%package -n python3-manuel
Summary:        Build tested documentation
Provides:       bundled(js-jquery)
%description -n python3-manuel
Manuel lets you mix and match traditional doctests with custom test
syntax.  Several plug-ins are included that provide new test syntax.
You can also create your own plug-ins.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir manuel-%{version}
%oreon_prep
%build

%pyproject_wheel
sphinx-build -c sphinx src/manuel docs
rm -fr docs/.buildinfo docs/.doctrees
rst2html --no-datestamp CHANGES.rst CHANGES.html
%install
%pyproject_install
%oreon_autofiles python3-manuel usr/lib/python3*/site-packages/manuel* usr/lib64/python3*/site-packages/manuel* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/manuel* usr/lib64/python3*/site-packages/manuel* usr/bin/*

%check

export PYTHONPATH=$PWD/build/lib
cp -p src/manuel/myst-markdown.md build/lib/manuel
%{python3} -m unittest manuel.tests.test_suite
%files
%files -n python3-manuel -f %{oreon_filedir}/python3-manuel.list

%changelog

%autochangelog
