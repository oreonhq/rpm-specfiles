%global source0_hash 92c2605952b219fb589834606e269df7065bd16831bd9726c5fcf6a9ba133bd5
%bcond doc_pdf 1
Name:       python-stdlib-list
Version:    0.12.0
Release:        1%{?dist}
Summary:        A list of Python Standard Libraries
License:    MIT
URL:        https://github.com/pypi/stdlib-list
Source0:        https://github.com/pypi/stdlib-list/archive/v%{version}/stdlib-list-%{version}.tar.gz
BuildArch:  noarch
%global desc %{expand:
This package includes lists of all of the standard libraries for Python.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-stdlib-list = %{version}-%{release}
# /oreon:deps
%package -n       python3-stdlib-list+test
Summary:        Metapackage for python3-stdlib-list test extras
Requires:       python3-stdlib-list = %{version}-%{release}
Provides:       python3dist(stdlib-list[test]) = %{version}-%{release}

%description -n python3-stdlib-list+test
Metapackage for python3-stdlib-list test extras.

%package -n       python3-stdlib-list+lint
Summary:        Metapackage for python3-stdlib-list lint extras
Requires:       python3-stdlib-list = %{version}-%{release}
Provides:       python3dist(stdlib-list[lint]) = %{version}-%{release}

%description -n python3-stdlib-list+lint
Metapackage for python3-stdlib-list lint extras.

%package -n       python3-stdlib-list+doc
Summary:        Metapackage for python3-stdlib-list doc extras
Requires:       python3-stdlib-list = %{version}-%{release}
Provides:       python3dist(stdlib-list[doc]) = %{version}-%{release}

%description -n python3-stdlib-list+doc
Metapackage for python3-stdlib-list doc extras.

%package -n       python3-stdlib-list+dev
Summary:        Metapackage for python3-stdlib-list dev extras
Requires:       python3-stdlib-list = %{version}-%{release}
Provides:       python3dist(stdlib-list[dev]) = %{version}-%{release}

%description -n python3-stdlib-list+dev
Metapackage for python3-stdlib-list dev extras.

%package -n       python3-stdlib-list+support
Summary:        Metapackage for python3-stdlib-list support extras
Requires:       python3-stdlib-list = %{version}-%{release}
Provides:       python3dist(stdlib-list[support]) = %{version}-%{release}

%description -n python3-stdlib-list+support
Metapackage for python3-stdlib-list support extras.

%description %{desc}

%package -n python3-stdlib-list
Summary:        A list of Python Standard Libraries
%description -n python3-stdlib-list %{desc}

%package doc
Summary:   Documentation for python-stdlib-list
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n stdlib-list-%{version}
# We don’t need the HTML theme to build PDF documentation:
sed -r -i 's/, "furo"//' pyproject.toml

%build

%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif
%install
%pyproject_install
%oreon_autofiles python3-stdlib-list usr/lib/python3*/site-packages/stdlib_list* usr/lib64/python3*/site-packages/stdlib_list* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/stdlib_list* usr/lib64/python3*/site-packages/stdlib_list* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-stdlib-list -f %{oreon_filedir}/python3-stdlib-list.list
%files -n python-stdlib-list-doc -f %{oreon_filedir}/python-stdlib-list-doc.list

%changelog

%autochangelog
