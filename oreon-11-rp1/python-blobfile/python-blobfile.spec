%global source0_hash 98bd9fafed8d0175d315a5b605680f522949057e16cb4932b07ce5a5f67e8985
Name:           python-blobfile
Version:        3.3.0
Release:        1%{?dist}
Summary:        Read GCS, ABS and local paths with the same interface, clone of tensorflow.io.gfile
License:        ...
URL:            https://github.com/blobfile/blobfile
Source0:        https://files.pythonhosted.org/packages/source/b/blobfile/blobfile-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 69
Requires:       python3-blobfile = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-blobfile
Summary:        Read GCS, ABS and local paths with the same interface, clone of tensorflow.io.gfile
# oreon:reqs
Requires:       python3dist(filelock) >= 3.0
Requires:       python3dist(lxml) >= 4.9
Requires:       python3dist(pycryptodomex) >= 3.8
Requires:       python3dist(urllib3) >= 2
# /oreon:reqs
%description -n python3-blobfile

%prep
%global oreon_srcdir blobfile-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-blobfile usr/lib/python3*/site-packages/blobfile* usr/lib64/python3*/site-packages/blobfile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/blobfile* usr/lib64/python3*/site-packages/blobfile* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-blobfile -f %{oreon_filedir}/python3-blobfile.list

%changelog

%autochangelog
