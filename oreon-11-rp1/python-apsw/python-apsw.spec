%global source0_hash 4250fab667cc41c55170028ab095a9d4a4ae66363f4bc0720771c20519702625
Name:           python-apsw
Version:        3.53.4.0
Release:        1%{?dist}
Summary:        Another Python SQLite Wrapper
License:        any-OSI
URL:            https://rogerbinns.github.io/apsw/changes.html
Source0:        https://files.pythonhosted.org/packages/source/a/apsw/apsw-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-apsw = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-apsw
Summary:        Another Python SQLite Wrapper
%description -n python3-apsw

%prep
%global oreon_srcdir apsw-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-apsw usr/lib/python3*/site-packages/apsw* usr/lib64/python3*/site-packages/apsw* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/apsw* usr/lib64/python3*/site-packages/apsw* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-apsw -f %{oreon_filedir}/python3-apsw.list

%changelog

%autochangelog
