%global source0_hash 7e4c02cab220b90d626e0d771070739104d8824598804c848fbbfa8055740eb0
%bcond doc 0%{?fedora}
%global _docdir_fmt %{name}
%global forgeurl https://github.com/pysb/pysb
Name:           python-pysb
Version:        1.16.0
Release:        1%{?dist}
Summary:        Rule-based modeling of biochemical systems as Python programs
License:        BSD-2-Clause
URL:            https://pysb.org/
%forgemeta
Source0:        %{forgeurl}/archive/v%{version}/pysb-%{version}.tar.gz
Patch:          python-pysb-rm-python-mock-usage.diff
BuildArch:      noarch
%if %{with doc}
%endif
# oreon:deps
BuildRequires:  dvipng
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  python3-devel
BuildRequires:  python3-ipython-sphinx
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3dist(numpydoc)
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(latex)
# /oreon:deps
%description

%package -n python3-pysb
Summary: %summary
Requires:       bionetgen
Requires:       bionetgen-perl
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-matplotlib
Requires:       python3-sympy
Requires:       python3-pygraphviz
Requires:       python3-networkx
%{?python_provide:%python_provide python3-pysb}
%description -n python3-pysb

%if %{with doc}
%package doc
Summary:        HTML documentation for %{name}
Requires:       python3-pysb = %{version}-%{release}
Provides:       bundled(jquery)
Obsoletes:      %{name}-docs <= 1.0.1
%description doc
This package contains HTML documentation for %{name}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pysb-%{version} -p1
# https://github.com/pysb/pysb/issues/100
sed -i -e "s|/usr/local/share/BioNetGen|%{perl_vendorlib}/BioNetGen|" \
       -e "s|'c:/Program Files/BioNetGen',||" \
    pysb/bng.py
sed -i -s "1 s|/usr/bin/env python|%{python3}|" pysb/examples/*.py pysb/tools/*.py

# Remove upper bound on sympy version,
# drop requirement on pynose.
sed -r -i "s/'(sympy>=1.6),<1.12'/'\1'/; /'pynose'/d" setup.py

%build

%py3_build
%if %{with doc}
make -C doc html
rm doc/_build/html/.buildinfo
%endif
%install
%py3_install
chmod +x %{buildroot}/%{python3_sitelib}/pysb/examples/run_*.py
chmod +x %{buildroot}/%{python3_sitelib}/pysb/tools/[a-z]*.py
%oreon_autofiles python3-pysb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pysb -f %{oreon_filedir}/python3-pysb.list
%files -n python-pysb-doc -f %{oreon_filedir}/python-pysb-doc.list

%changelog

%autochangelog
