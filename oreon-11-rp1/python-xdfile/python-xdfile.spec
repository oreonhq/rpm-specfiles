%global source0_hash aa62cbe338ddcb11ebf2460bcd6a005a766e516ed3d00751cc2e0379b937c587
Name:           python-xd
Version:        0.1.8
Release:        1%{?dist}
Summary:        a list of useful commands which makes life easier
License:        ...
URL:            https://github.com/damnever/xd
Source0:        https://files.pythonhosted.org/packages/source/x/xd/xd-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xd = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xd
Summary:        a list of useful commands which makes life easier
%description -n python3-xd

%prep
%global oreon_srcdir xd-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xd usr/lib/python3*/site-packages/xd* usr/lib64/python3*/site-packages/xd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xd* usr/lib64/python3*/site-packages/xd* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xd -f %{oreon_filedir}/python3-xd.list

%changelog

%autochangelog
