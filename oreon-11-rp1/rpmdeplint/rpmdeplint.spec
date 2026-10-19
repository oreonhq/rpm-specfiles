%global source0_hash f601775657e40a67513eab00431d121821ea5824ad7851496edbfcfe8bf0c7ec
Name:           rpmdeplint
Version:        2.1
Release:        1%{?dist}
Summary:        Tool to find errors in RPM packages in the context of their dependency graph
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-ci/rpmdeplint
Source0:        https://files.pythonhosted.org/packages/source/r/rpmdeplint/rpmdeplint-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-rpmdeplint = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rpmdeplint = %{version}-%{release}
# /oreon:deps
%package -n       python3-rpmdeplint+docs
Summary:        Metapackage for python3-rpmdeplint docs extras
Requires:       python3-rpmdeplint = %{version}-%{release}
Provides:       python3dist(rpmdeplint[docs]) = %{version}-%{release}

%description -n python3-rpmdeplint+docs
Metapackage for python3-rpmdeplint docs extras.

%package -n       python3-rpmdeplint+tests
Summary:        Metapackage for python3-rpmdeplint tests extras
Requires:       python3-rpmdeplint = %{version}-%{release}
Provides:       python3dist(rpmdeplint[tests]) = %{version}-%{release}

%description -n python3-rpmdeplint+tests
Metapackage for python3-rpmdeplint tests extras.

%package -n       python3-rpmdeplint+dev
Summary:        Metapackage for python3-rpmdeplint dev extras
Requires:       python3-rpmdeplint = %{version}-%{release}
Provides:       python3dist(rpmdeplint[dev]) = %{version}-%{release}

%description -n python3-rpmdeplint+dev
Metapackage for python3-rpmdeplint dev extras.

%description
Rpmdeplint is a tool to find errors in RPM packages in the context of their
dependency graph.

%package -n python3-rpmdeplint
%{?python_provide:%python_provide python3-rpmdeplint}
Summary:        Tool to find errors in RPM packages in the context of their dependency graph
BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  python3-librepo
BuildRequires:  python3-solv
Requires:       python3-librepo
Requires:       python3-solv
%description -n python3-rpmdeplint
Rpmdeplint is a tool to find errors in RPM packages in the context of their
dependency graph.

This package provides a Python 3 API for performing the checks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rpmdeplint-%{version}
%oreon_prep
%build

%pyproject_wheel
make -C docs man
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1/
mv docs/_build/man/rpmdeplint.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles python3-rpmdeplint usr/lib/python3*/site-packages/rpmdeplint* usr/lib64/python3*/site-packages/rpmdeplint* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rpmdeplint* usr/lib64/python3*/site-packages/rpmdeplint* usr/bin/*

%check

%pytest tests/unit/ -k "not TestDependencyAnalyzer"
%files
%files -n python3-rpmdeplint -f %{oreon_filedir}/python3-rpmdeplint.list

%changelog

%autochangelog
