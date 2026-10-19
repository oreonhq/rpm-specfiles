%global source0_hash 0e3668def86f65e1e85fa8a898920e6e45b2d213daf5410f0552b82352a17f37
Summary:        Python package with an object-oriented approach to text processing
Name:           pyparsing
Version:        3.3.3
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/pyparsing/pyparsing
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
%bcond doc      1
%bcond tests    1
%bcond extras   %{undefined rhel}
%if %{with doc}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.12
Requires:       python3-pyparsing = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyparsing+diagrams
Summary:        Metapackage for python3-pyparsing diagrams extras
Requires:       python3-pyparsing = %{version}-%{release}
Provides:       python3dist(pyparsing[diagrams]) = %{version}-%{release}

%description -n python3-pyparsing+diagrams
Metapackage for python3-pyparsing diagrams extras.

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.

%package -n python%{python3_pkgversion}-pyparsing
Summary:        Python package with an object-oriented approach to text processing
%description -n python%{python3_pkgversion}-pyparsing
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.

%if %{with doc}
%package        doc
Summary:        Documentation for %{name}
License:        MIT AND MIT-CMU AND GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause AND BSD-2-Clause
%description    doc
The package contains documentation for pyparsing.
%endif

%if %{with extras}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

dos2unix -k examples/*

%build

%pyproject_wheel
%if %{with doc}
pushd docs
sphinx-build -b html . html
popd
%endif
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pyparsing* usr/lib64/python3*/site-packages/pyparsing* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import %{!?with_extras:-e pyparsing.diagram}
%if %{with tests}
%pytest -v %{!?with_extras:-k 'not test_range_check and not testEmptyExpressionsAreHandledProperly' --ignore tests/test_diagram.py}
%endif
%files
%files -n python3-pyparsing -f %{oreon_filedir}/python3-pyparsing.list
%files -n pyparsing-doc -f %{oreon_filedir}/pyparsing-doc.list

%changelog

%autochangelog
