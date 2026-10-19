%global source0_hash 1c72b39f09457db3c05ce1d19158c2cbef4c32b8bedd02c155e49282b7ea7459
Name:           python-send2trash
Version:        2.1.0
Release:        1%{?dist}
Summary:        Send file to trash natively under Mac OS X, Windows and Linux
License:        BSD-3-Clause
URL:            https://github.com/arsenetar/send2trash
Source0:        https://files.pythonhosted.org/packages/source/s/send2trash/send2trash-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75.3.1
Requires:       python3-send2trash = %{version}-%{release}
# /oreon:deps
%package -n       python3-send2trash+test
Summary:        Metapackage for python3-send2trash test extras
Requires:       python3-send2trash = %{version}-%{release}
Requires:       python3dist(pytest) >= 8
Provides:       python3dist(send2trash[test]) = %{version}-%{release}

%description -n python3-send2trash+test
Metapackage for python3-send2trash test extras.

%package -n       python3-send2trash+nativelib
Summary:        Metapackage for python3-send2trash nativelib extras
Requires:       python3-send2trash = %{version}-%{release}
Requires:       python3dist(pywin32) >= 305
Requires:       python3dist(pyobjc) >= 9.0
Provides:       python3dist(send2trash[nativelib]) = %{version}-%{release}

%description -n python3-send2trash+nativelib
Metapackage for python3-send2trash nativelib extras.

%description

%package -n     python3-send2trash
Summary:        Send file to trash natively under Mac OS X, Windows and Linux
%description -n python3-send2trash

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir send2trash-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-send2trash usr/lib/python3*/site-packages/send2trash* usr/lib64/python3*/site-packages/send2trash* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/send2trash* usr/lib64/python3*/site-packages/send2trash* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-send2trash -f %{oreon_filedir}/python3-send2trash.list

%changelog

%autochangelog
