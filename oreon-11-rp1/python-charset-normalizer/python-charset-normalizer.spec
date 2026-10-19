%global source0_hash 39de2a259fc954455c57274dc94c79d5842774e1247a016aff30bc0efed0f4ef
Name:           python-charset-normalizer
Version:        3.5.2
Release:        1%{?dist}
Summary:        The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
License:        MIT
URL:            https://github.com/jawah/charset_normalizer/blob/master/CHANGELOG.md
Source0:        https://files.pythonhosted.org/packages/source/c/charset_normalizer/charset_normalizer-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 84.1
BuildRequires:  python3dist(setuptools) >= 68
Requires:       python3-charset-normalizer = %{version}-%{release}
# /oreon:deps
%package -n       python3-charset-normalizer+unicode_backport
Summary:        Metapackage for python3-charset-normalizer unicode_backport extras
Requires:       python3-charset-normalizer = %{version}-%{release}
Provides:       python3dist(charset-normalizer[unicode_backport]) = %{version}-%{release}

%description -n python3-charset-normalizer+unicode_backport
Metapackage for python3-charset-normalizer unicode_backport extras.

%description

%package -n     python3-charset-normalizer
Summary:        The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.
%description -n python3-charset-normalizer

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir charset_normalizer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-charset-normalizer usr/lib/python3*/site-packages/charset_normalizer* usr/lib64/python3*/site-packages/charset_normalizer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/charset_normalizer* usr/lib64/python3*/site-packages/charset_normalizer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-charset-normalizer -f %{oreon_filedir}/python3-charset-normalizer.list

%changelog

%autochangelog
