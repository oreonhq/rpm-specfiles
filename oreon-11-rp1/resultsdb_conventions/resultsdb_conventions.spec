%global source0_hash 8e5130319e2cb65ecbd2ce9676a880ea907eded8c0c1312938bc932b7ebc9387
%global sum     Library defining conventions for ResultsDB results
%global desc    This project defines some agreed conventions for reporting results of \
different types to ResultsDB, and provides code (currently a Python library) \
to help with reporting results that conform to the conventions.
%global forgejo_namespace    quality
%global forgejo_name         resultsdb_conventions
%global forgejo_version      3.0.3
Name:           resultsdb_conventions
Version:        %{forgejo_version}
Release:        1%{?dist}
Summary:        Library defining conventions for ResultsDB results
License:        GPL-3.0-or-later
URL:            https://forge.fedoraproject.org/%{forgejo_namespace}/%{forgejo_name}
Source0:        https://files.pythonhosted.org/packages/source/r/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-resultsdb_conventions = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python%{python3_pkgversion}-resultsdb_conventions
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-resultsdb_conventions}
Obsoletes:      python2-resultsdb_conventions < %{version}-%{release}
%description -n python%{python3_pkgversion}-resultsdb_conventions
%{desc}

%package -n python%{python3_pkgversion}-resultsdb_conventions-fedora
Summary:        %{sum} (Fedora module)
%{?python_provide:%python_provide python%{python3_pkgversion}-resultsdb_conventions-fedora}
Requires:       python%{python3_pkgversion}-resultsdb_conventions
Obsoletes:      python2-resultsdb_conventions-fedora < %{version}-%{release}
%description -n python%{python3_pkgversion}-resultsdb_conventions-fedora
%{desc} This subpackage
contains the resultsdb_conventions.fedora module, which has additional
dependencies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# this is needed for doing sdist, but not for anything else
sed -i -e '/setuptools_git/d' setup.py
sed -i -e 's., "setuptools-scm"..g' pyproject.toml
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/resultsdb_conventions* usr/lib64/python3*/site-packages/resultsdb_conventions* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%tox
%files
%files -n python3-resultsdb_conventions -f %{oreon_filedir}/python3-resultsdb_conventions.list
%files -n python3-resultsdb_conventions-fedora -f %{oreon_filedir}/python3-resultsdb_conventions-fedora.list

%changelog

%autochangelog
