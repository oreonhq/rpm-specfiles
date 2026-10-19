%global source0_hash d08e3895c96aa276963aec9f83f19eeb5e8e777c09935c0d266cfe887311160a
%bcond_without doc
%bcond_with tests
Name:           python-hyperkitty
Version:        1.3.12
Release:        1%{?dist}
Summary:        A web interface to access GNU Mailman v3 archives
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/hyperkitty
Source0:        https://gitlab.com/mailman/hyperkitty/-/archive/%{version}/hyperkitty-%{version}.tar.gz
Patch:          HyperKitty-tox-localdeps.patch
Patch:          hyperkitty-django52.diff
BuildArch:      noarch
%if %{with doc}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hyperkitty = %{version}-%{release}
# /oreon:deps
%package -n       python3-hyperkitty+dev
Summary:        Metapackage for python3-hyperkitty dev extras
Requires:       python3-hyperkitty = %{version}-%{release}
Requires:       python3dist(whoosh) >= 2.5.7
Provides:       python3dist(hyperkitty[dev]) = %{version}-%{release}

%description -n python3-hyperkitty+dev
Metapackage for python3-hyperkitty dev extras.

%package -n       python3-hyperkitty+test
Summary:        Metapackage for python3-hyperkitty test extras
Requires:       python3-hyperkitty = %{version}-%{release}
Requires:       python3dist(whoosh) >= 2.5.7
Requires:       python3dist(beautifulsoup4) >= 4.3.2
Provides:       python3dist(hyperkitty[test]) = %{version}-%{release}

%description -n python3-hyperkitty+test
Metapackage for python3-hyperkitty test extras.

%description

%package -n hyperkitty
Summary:        A web interface to access GNU Mailman v3 archives
Recommends:     python%{python3_version}dist(cmarkgfm)
%description -n hyperkitty

%package -n hyperkitty-doc
Summary:        Documentation for hyperkitty
Suggests:       hyperkitty = %{version}-%{release}
%description -n hyperkitty-doc

This package contains the documentation for hyperkitty.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n hyperkitty-%{version}
# fix shebang
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' \
  example_project/manage.py

%build

%pyproject_wheel
%if %{with doc}
(cd doc && PYTHONPATH=..:${PYTHONPATH} make html)
%endif
%install
%pyproject_install
%oreon_autofiles hyperkitty usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles hyperkitty-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
PYTHONPATH=$(pwd)/src:${PYTHONPATH} \
%tox
%endif
%files
%files -n hyperkitty -f %{oreon_filedir}/hyperkitty.list
%files -n hyperkitty-doc -f %{oreon_filedir}/hyperkitty-doc.list

%changelog

%autochangelog
