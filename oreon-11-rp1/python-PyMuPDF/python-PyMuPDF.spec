%global source0_hash 5e0be7908a715aa20333caddd73f1d6f01e4cd0c26e869fa2dd0b7f344da2249
Name:           python-pymupdf
Version:        1.28.2
Release:        1%{?dist}
Summary:        A high performance Python library for data extraction, analysis, conversion _ manipulation of PDF _and other_ documents.
License:        ...
URL:            https://github.com/pymupdf/pymupdf
Source0:        https://files.pythonhosted.org/packages/source/p/pymupdf/pymupdf-%{version}.tar.gz
Patch:		0001-fix-test_-font.patch
Patch:		0001-test_pixmap-adjust-to-turbojpeg.patch
Patch:		0001-setup.py-do-not-require-libclang-and-swig.patch
Patch:		0001-tests-adjust-to-verbose-font-warning.patch
Patch:		0001-adjust-tests-to-tesseract-5.5.1.patch
Patch:		0001-tests-conftest-do-not-call-pip.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pymupdf = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pymupdf
Summary:        A high performance Python library for data extraction, analysis, conversion _ manipulation of PDF _and other_ documents.
%description -n python3-pymupdf

%prep
%global oreon_srcdir pymupdf-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pymupdf usr/lib/python3*/site-packages/pymupdf* usr/lib64/python3*/site-packages/pymupdf* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pymupdf* usr/lib64/python3*/site-packages/pymupdf* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pymupdf -f %{oreon_filedir}/python3-pymupdf.list

%changelog

%autochangelog
