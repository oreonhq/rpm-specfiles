%global source0_hash af46e4dc089be55050896d133643e2bdc6070fbfe78a039691ff08948af88c38
Name:           python-fontconfig
Version:        0.6.3
Release:        1%{?dist}
Summary:        Python bindings for Fontconfig library
License:        GPL-3.0
URL:            https://github.com/Vayn/python-fontconfig
Source0:        https://files.pythonhosted.org/packages/source/p/python_fontconfig/python_fontconfig-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fontconfig = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-python-fontconfig
Summary:        Python bindings for Fontconfig library
%description -n python3-python-fontconfig

%prep
%global oreon_srcdir python_fontconfig-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-python-fontconfig usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-python-fontconfig -f %{oreon_filedir}/python3-python-fontconfig.list

%changelog

%autochangelog
