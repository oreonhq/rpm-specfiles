%global source0_hash 87683d47965c1da65cdacaf31c8441d12b8044cdec9aca500cd78fc2c683afca
Name:           python-pickleshare
Version:        0.7.5
Release:        1%{?dist}
Summary:        Tiny 'shelve'-like database with concurrency support
License:        MIT
URL:            https://github.com/ipython/pickleshare
Source0:        https://files.pythonhosted.org/packages/source/p/pickleshare/pickleshare-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pickleshare = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pickleshare
Summary:        Tiny 'shelve'-like database with concurrency support
%description -n python3-pickleshare

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pickleshare-%{version}

# fix interpreter
sed -i 's/\/usr\/bin\/env python/\/usr\/bin\/python/' pickleshare.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pickleshare usr/lib/python3*/site-packages/pickleshare* usr/lib64/python3*/site-packages/pickleshare* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pickleshare* usr/lib64/python3*/site-packages/pickleshare* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-pickleshare -f %{oreon_filedir}/python3-pickleshare.list

%changelog

%autochangelog
