%global source0_hash f723ebb76a112e98816ff80fcea0a6c9b8ecde835f8ddda25df7a30a3c2db6ad
Name:           python-whitenoise
Version:        6.12.0
Release:        1%{?dist}
Summary:        Radically simplified static file serving for WSGI applications
License:        MIT
URL:            https://github.com/evansd/whitenoise
Source0:        https://files.pythonhosted.org/packages/source/w/whitenoise/whitenoise-%{version}.tar.gz
BuildArch:      noarch
Patch:          whitenoise-6.4.0-default-docs-theme.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-whitenoise = %{version}-%{release}
# /oreon:deps
%package -n       python3-whitenoise+brotli
Summary:        Metapackage for python3-whitenoise brotli extras
Requires:       python3-whitenoise = %{version}-%{release}
Provides:       python3dist(whitenoise[brotli]) = %{version}-%{release}

%description -n python3-whitenoise+brotli
Metapackage for python3-whitenoise brotli extras.

%description

%package -n     python3-whitenoise
Summary:        Radically simplified static file serving for WSGI applications
%description -n python3-whitenoise

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir whitenoise-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-whitenoise usr/lib/python3*/site-packages/whitenoise* usr/lib64/python3*/site-packages/whitenoise* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/whitenoise* usr/lib64/python3*/site-packages/whitenoise* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-whitenoise -f %{oreon_filedir}/python3-whitenoise.list

%changelog

%autochangelog
