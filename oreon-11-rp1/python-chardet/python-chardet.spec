%global source0_hash 93d9df6089ded42ed1fe9f57e272c0b74bd0464d45c0c7d50f09f26f31105c3c
BuildArch:      noarch
Name:           python-chardet
Version:        7.6.0
Release:        1%{?dist}
Summary:        Universal character encoding detector
License:        0BSD
URL:            https://github.com/chardet/chardet
Source0:        https://files.pythonhosted.org/packages/source/c/chardet/chardet-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-chardet = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-chardet
Summary:        Universal character encoding detector
%description -n python3-chardet

%prep
%global oreon_srcdir chardet-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-chardet usr/lib/python3*/site-packages/chardet* usr/lib64/python3*/site-packages/chardet* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/chardet* usr/lib64/python3*/site-packages/chardet* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-chardet -f %{oreon_filedir}/python3-chardet.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.0.post1-1
- Import
