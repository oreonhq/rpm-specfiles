%global source0_hash eaa959bc116b420dd7ec415fcae49b98100dda3dd18cd2fdfa86d09f112f6d57
Name:           python-pdf2image
Version:        1.17.0
Release:        1%{?dist}
Summary:        A wrapper around the pdftoppm and pdftocairo command line tools to convert PDF to a PIL Image list.
License:        MIT
URL:            https://github.com/Belval/pdf2image
Source0:        https://files.pythonhosted.org/packages/source/p/pdf2image/pdf2image-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/269.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pdf2image = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pdf2image
Summary:        A wrapper around the pdftoppm and pdftocairo command line tools to convert PDF to a PIL Image list.
%description -n python3-pdf2image

%prep
%global oreon_srcdir pdf2image-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pdf2image usr/lib/python3*/site-packages/pdf2image* usr/lib64/python3*/site-packages/pdf2image* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pdf2image* usr/lib64/python3*/site-packages/pdf2image* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pdf2image -f %{oreon_filedir}/python3-pdf2image.list

%changelog

%autochangelog
