%global source0_hash 27a79f48754a968b801ba80890cfb2ac1835ba27387a257c514b90db73edc20b
Name:           python-tcxreader
Version:        0.4.11
Release:        1%{?dist}
Summary:        tcxreader is a reader for Garmin’s TCX file format. It also works well with missing data!
License:        MIT
URL:            https://github.com/alenrajsp/tcxreader
Source0:        https://files.pythonhosted.org/packages/source/t/tcxreader/tcxreader-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-tcxreader = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tcxreader
Summary:        tcxreader is a reader for Garmin’s TCX file format. It also works well with missing data!
%description -n python3-tcxreader

%prep
%global oreon_srcdir tcxreader-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tcxreader usr/lib/python3*/site-packages/tcxreader* usr/lib64/python3*/site-packages/tcxreader* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tcxreader* usr/lib64/python3*/site-packages/tcxreader* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tcxreader -f %{oreon_filedir}/python3-tcxreader.list

%changelog

%autochangelog
