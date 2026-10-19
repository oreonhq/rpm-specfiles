%global source0_hash d0d39f1bc07db5799241053cfb9fc254f2615b411235ef8e540367b847e31dc0
Name:           python-tamilstring
Version:        2.2.1
Release:        1%{?dist}
Summary:        tamilstring helps to handle tamil unicode characters lot more easier
License:        MIT
URL:            https://gitlab.com/boopalan-dev/tamilstring
Source0:        https://files.pythonhosted.org/packages/source/t/tamilstring/tamilstring-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tamilstring = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tamilstring
Summary:        tamilstring helps to handle tamil unicode characters lot more easier
%description -n python3-tamilstring

%prep
%global oreon_srcdir tamilstring-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tamilstring usr/lib/python3*/site-packages/tamilstring* usr/lib64/python3*/site-packages/tamilstring* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tamilstring* usr/lib64/python3*/site-packages/tamilstring* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tamilstring -f %{oreon_filedir}/python3-tamilstring.list

%changelog

%autochangelog
