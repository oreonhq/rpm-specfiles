%global source0_hash 68e0cb27115b08b681c843e30a153b5d9850c048e1158623ada36ccd4cf7e89b
Name:           python-types-pygments
Version:        2.21.0.20260819
Release:        1%{?dist}
Summary:        Typing stubs for Pygments
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        https://files.pythonhosted.org/packages/source/t/types_pygments/types_pygments-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82.0.1
Requires:       python3-types-pygments = %{version}-%{release}
# /oreon:deps
%package -n       python3-types-pygments+all
Summary:        Metapackage for python3-types-pygments all extras
Requires:       python3-types-pygments = %{version}-%{release}
Provides:       python3dist(types-pygments[all]) = %{version}-%{release}

%description -n python3-types-pygments+all
Metapackage for python3-types-pygments all extras.

%package -n       python3-types-pygments+docutils
Summary:        Metapackage for python3-types-pygments docutils extras
Requires:       python3-types-pygments = %{version}-%{release}
Provides:       python3dist(types-pygments[docutils]) = %{version}-%{release}

%description -n python3-types-pygments+docutils
Metapackage for python3-types-pygments docutils extras.

%description

%package -n     python3-types-pygments
Summary:        Typing stubs for Pygments
%description -n python3-types-pygments

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir types_pygments-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-types-pygments usr/lib/python3*/site-packages/types_pygments* usr/lib64/python3*/site-packages/types_pygments* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/types_pygments* usr/lib64/python3*/site-packages/types_pygments* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-types-pygments -f %{oreon_filedir}/python3-types-pygments.list

%changelog

%autochangelog
