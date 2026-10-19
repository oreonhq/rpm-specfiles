%global source0_hash 8cbfba26938befd8a35e3cc06ca0632f61320b7b2be7df32550b895e1725b1ce
Name:           python-mbstrdecoder
Version:        1.1.5
Release:        1%{?dist}
Summary:        mbstrdecoder is a Python library for multi-byte character string decoder
License:        MIT
URL:            https://github.com/thombashi/mbstrdecoder
Source0:        https://files.pythonhosted.org/packages/source/m/mbstrdecoder/mbstrdecoder-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-mbstrdecoder = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mbstrdecoder
Summary:        mbstrdecoder is a Python library for multi-byte character string decoder
%description -n python3-mbstrdecoder

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mbstrdecoder-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mbstrdecoder usr/lib/python3*/site-packages/mbstrdecoder* usr/lib64/python3*/site-packages/mbstrdecoder* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mbstrdecoder* usr/lib64/python3*/site-packages/mbstrdecoder* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mbstrdecoder -f %{oreon_filedir}/python3-mbstrdecoder.list

%changelog

%autochangelog
