%global source0_hash 0387fd08848d00cadd1d885fcb19a17dd4250df2029e5338b6b668b7fed64b5b
Name:           python-wand
Version:        0.7.2
Release:        1%{?dist}
Summary:        Ctypes-based simple MagickWand API binding for Python
License:        MIT
URL:            https://docs.wand-py.org
Source0:        https://files.pythonhosted.org/packages/source/w/wand/wand-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-wand = %{version}-%{release}
# /oreon:deps
%package -n       python3-wand+test
Summary:        Metapackage for python3-wand test extras
Requires:       python3-wand = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.2.0
Provides:       python3dist(wand[test]) = %{version}-%{release}

%description -n python3-wand+test
Metapackage for python3-wand test extras.

%package -n       python3-wand+doc
Summary:        Metapackage for python3-wand doc extras
Requires:       python3-wand = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.2.6
Provides:       python3dist(wand[doc]) = %{version}-%{release}

%description -n python3-wand+doc
Metapackage for python3-wand doc extras.

%description

%package -n     python3-wand
Summary:        Ctypes-based simple MagickWand API binding for Python
%description -n python3-wand

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir wand-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wand usr/lib/python3*/site-packages/wand* usr/lib64/python3*/site-packages/wand* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wand* usr/lib64/python3*/site-packages/wand* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wand -f %{oreon_filedir}/python3-wand.list

%changelog

%autochangelog
