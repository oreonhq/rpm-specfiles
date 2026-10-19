%global source0_hash 2c84db30209190286215daf7c69f6120ccf5982df1ab954c6c552ef584bb2d30
%global pypi_name sphinx-removed-in
Name:           python-sphinx-removed-in
Version:        0.2.3
Release:        1%{?dist}
Summary:        versionremoved and removed-in directives for Sphinx
License:        BSD-3-Clause
URL:            https://github.com/MrSenko/sphinx-removed-in
Source0:        https://github.com/MrSenko/sphinx-removed-in/archive/v%{version}/sphinx-removed-in-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinx-removed-in = %{version}-%{release}
# /oreon:deps
%description
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%package -n     python3-sphinx-removed-in
Summary:        versionremoved and removed-in directives for Sphinx
%description -n python3-sphinx-removed-in
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinx-removed-in-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-removed-in usr/lib/python3*/site-packages/sphinx_removed_in* usr/lib64/python3*/site-packages/sphinx_removed_in* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_removed_in* usr/lib64/python3*/site-packages/sphinx_removed_in* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-sphinx-removed-in -f %{oreon_filedir}/python3-sphinx-removed-in.list

%changelog

%autochangelog
