%global source0_hash 62dc242fd4ea2a50339f4f5aaaf6ecc55605ee74770d7eb2031e760d90a0d114
Name:           python-serpent
Version:        1.43
Release:        1%{?dist}
Summary:        Serialization based on ast.literal_eval
License:        MIT
URL:            https://github.com/irmen/Serpent
Source0:        https://files.pythonhosted.org/packages/source/s/serpent/serpent-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-serpent = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-serpent
Summary:        Serialization based on ast.literal_eval
%description -n python3-serpent

%prep
%global oreon_srcdir serpent-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-serpent usr/lib/python3*/site-packages/serpent* usr/lib64/python3*/site-packages/serpent* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/serpent* usr/lib64/python3*/site-packages/serpent* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-serpent -f %{oreon_filedir}/python3-serpent.list

%changelog

%autochangelog
