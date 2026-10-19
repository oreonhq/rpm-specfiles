%global source0_hash 2169c05252c0efbe897f346f0683326ec25854beab1d0c6430df6e903a57b315
Name:           python-dbf
Version:        0.99.11
Release:        1%{?dist}
Summary:        Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf files _including memos_
License:        ...
URL:            https://github.com/ethanfurman/dbf
Source0:        https://files.pythonhosted.org/packages/source/d/dbf/dbf-%{version}.tar.gz
BuildArch:      noarch
Patch0:         prevent-synthax-error.patch
Patch1:         remove-distutil.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dbf = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dbf
Summary:        Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf files _including memos_
%description -n python3-dbf

%prep
%global oreon_srcdir dbf-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dbf usr/lib/python3*/site-packages/dbf* usr/lib64/python3*/site-packages/dbf* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dbf* usr/lib64/python3*/site-packages/dbf* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dbf -f %{oreon_filedir}/python3-dbf.list

%changelog

%autochangelog
