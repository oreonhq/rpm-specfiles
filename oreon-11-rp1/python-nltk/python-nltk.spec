%global source0_hash bb9327a461c3811c2fa4900e03840401f2126adfb30c0072827c433bd2444ea4
Name:           python-nltk
Version:        3.10.3
Release:        1%{?dist}
Summary:        Natural Language Toolkit
License:        ...
URL:            https://github.com/nltk/nltk
Source0:        https://files.pythonhosted.org/packages/source/n/nltk/nltk-%{version}.tar.gz
BuildArch:      noarch
Patch1: fix-import-WordNetLemmatizer.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-nltk = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-nltk
Summary:        Natural Language Toolkit
%description -n python3-nltk

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir nltk-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nltk usr/lib/python3*/site-packages/nltk* usr/lib64/python3*/site-packages/nltk* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nltk* usr/lib64/python3*/site-packages/nltk* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nltk -f %{oreon_filedir}/python3-nltk.list

%changelog

%autochangelog
