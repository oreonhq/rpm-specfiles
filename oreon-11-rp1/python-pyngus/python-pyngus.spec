%global source0_hash d925868637fcaf2b6a2174137d39af909d1e95f5c8a27c816b55b5a204e9240d
Name:           python-pyngus
Version:        2.3.1
Release:        1%{?dist}
Summary:        Callback API implemented over Proton
License:        ...
URL:            https://github.com/kgiusti/pyngus
Source0:        https://files.pythonhosted.org/packages/source/p/pyngus/pyngus-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyngus = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyngus
Summary:        Callback API implemented over Proton
%description -n python3-pyngus

%prep
%global oreon_srcdir pyngus-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyngus usr/lib/python3*/site-packages/pyngus* usr/lib64/python3*/site-packages/pyngus* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyngus* usr/lib64/python3*/site-packages/pyngus* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyngus -f %{oreon_filedir}/python3-pyngus.list

%changelog

%autochangelog
