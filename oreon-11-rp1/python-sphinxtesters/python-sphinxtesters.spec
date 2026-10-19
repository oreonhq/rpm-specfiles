%global source0_hash 60bbb160760961836533b1684b53f2d91b8ffbdaa95203c926b3c16018dc8c83
Name:           python-sphinxtesters
Version:        0.2.4
Release:        1%{?dist}
Summary:        Utilities for testing Sphinx extensions
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/matthew-brett/sphinxtesters
VCS:            git:%{url}.git
Source0:        https://github.com/matthew-brett/sphinxtesters/archive/%{version}/sphinxtesters-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.4
Requires:       python3-sphinxtesters = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinxtesters+test
Summary:        Metapackage for python3-sphinxtesters test extras
Requires:       python3-sphinxtesters = %{version}-%{release}
Provides:       python3dist(sphinxtesters[test]) = %{version}-%{release}

%description -n python3-sphinxtesters+test
Metapackage for python3-sphinxtesters test extras.

%package -n       python3-sphinxtesters+doc
Summary:        Metapackage for python3-sphinxtesters doc extras
Requires:       python3-sphinxtesters = %{version}-%{release}
Provides:       python3dist(sphinxtesters[doc]) = %{version}-%{release}

%description -n python3-sphinxtesters+doc
Metapackage for python3-sphinxtesters doc extras.

%description
This package contains utilities for testing Sphinx extensions.

%package -n     python3-sphinxtesters
Summary:        Utilities for testing Sphinx extensions
Requires:       %{py3_dist sphinx}
# oreon:reqs
Requires:       python3dist(sphinx) >= 1.4
# /oreon:reqs
%description -n python3-sphinxtesters
This package contains utilities for testing Sphinx extensions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinxtesters-%{version}
%oreon_prep
%build

%pyproject_wheel
rst2html --no-datestamp README.rst README.html
PYTHONPATH=$PWD sphinx-build doc build
rm -fr build/.{buildinfo,doctrees,nojekyll}
%install
%pyproject_install
%oreon_autofiles python3-sphinxtesters usr/lib/python3*/site-packages/sphinxtesters* usr/lib64/python3*/site-packages/sphinxtesters* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxtesters* usr/lib64/python3*/site-packages/sphinxtesters* usr/bin/*

%check

%pytest -v
%files
%files -n python3-sphinxtesters -f %{oreon_filedir}/python3-sphinxtesters.list

%changelog

%autochangelog
