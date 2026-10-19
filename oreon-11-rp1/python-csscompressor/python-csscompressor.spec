%global source0_hash afa22badbcf3120a4f392e4d22f9fff485c044a1feda4a950ecc5eba9dd31a05
Name:           python-csscompressor
Version:        0.9.5
Release:        1%{?dist}
Summary:        Python port of YUI CSS Compressor
License:        BSD-3-Clause
URL:            https://github.com/sprymix/csscompressor
Source0:        https://files.pythonhosted.org/packages/source/c/csscompressor/csscompressor-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-csscompressor = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-csscompressor
Summary:        Python port of YUI CSS Compressor
%description -n python3-csscompressor

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir csscompressor-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-csscompressor usr/lib/python3*/site-packages/csscompressor* usr/lib64/python3*/site-packages/csscompressor* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/csscompressor* usr/lib64/python3*/site-packages/csscompressor* usr/bin/*

%check

%pytest -v
%files
%files -n python3-csscompressor -f %{oreon_filedir}/python3-csscompressor.list

%changelog

%autochangelog
