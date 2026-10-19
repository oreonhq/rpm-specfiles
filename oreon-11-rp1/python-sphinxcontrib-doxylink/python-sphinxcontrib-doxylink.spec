%global source0_hash 047f8f4b9dbd104c004cfe24211af38b7a21fd707a103b214b6a5c5af3c4790c
Name:      python-sphinxcontrib-doxylink
Version:   1.13.0
Release:        7%{?dist}
Summary:        A Sphinx extension to link to external Doxygen API documentation
License:   BSD-2-Clause
URL:       https://github.com/sphinx-contrib/doxylink
Source0:        https://github.com/sphinx-contrib/doxylink/archive/refs/tags/%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-sphinxcontrib-doxylink = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-sphinxcontrib-doxylink
Summary:        A Sphinx extension to link to external Doxygen API documentation
%description -n python3-sphinxcontrib-doxylink

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir doxylink-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxcontrib-doxylink usr/lib/python3*/site-packages/sphinxcontrib_doxylink* usr/lib64/python3*/site-packages/sphinxcontrib_doxylink* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxcontrib_doxylink* usr/lib64/python3*/site-packages/sphinxcontrib_doxylink* usr/bin/*

%check

%pyproject_check_import
%{pytest}
%files
%files -n python3-sphinxcontrib-doxylink -f %{oreon_filedir}/python3-sphinxcontrib-doxylink.list

%changelog

%autochangelog
