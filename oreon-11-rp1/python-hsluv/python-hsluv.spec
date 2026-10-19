%global source0_hash 2281f946427a882010042844a38c7bbe9e0d0aaf9d46babe46366ed6f169b72e
Name:		python-hsluv
Version:	5.0.4
Release:        1%{?dist}
Summary:        A Python implementation of HSLuv (revision 4)
License:	MIT
URL:		https://www.hsluv.org/
Source0:        https://files.pythonhosted.org/packages/source/h/hsluv/hsluv-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hsluv = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-hsluv
Summary:        A Python implementation of HSLuv (revision 4)
%description -n python3-hsluv

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hsluv-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hsluv usr/lib/python3*/site-packages/hsluv* usr/lib64/python3*/site-packages/hsluv* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hsluv* usr/lib64/python3*/site-packages/hsluv* usr/bin/*

%check

%pytest
%pyproject_check_import
%files
%files -n python3-hsluv -f %{oreon_filedir}/python3-hsluv.list

%changelog

%autochangelog
