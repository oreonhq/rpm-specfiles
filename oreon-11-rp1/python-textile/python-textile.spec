%global source0_hash 89428d848712b041cf4e354c0a6332339810d519a5c3109cb42a0c594f882a0d
Name:           python-textile
Version:        4.0.4
Release:        1%{?dist}
Summary:        Textile processing for python.
License:        ...
URL:            https://github.com/textile/python-textile
Source0:        https://files.pythonhosted.org/packages/source/t/textile/textile-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-textile = %{version}-%{release}
# /oreon:deps
%package -n       python3-textile+develop
Summary:        Metapackage for python3-textile develop extras
Requires:       python3-textile = %{version}-%{release}
Provides:       python3dist(textile[develop]) = %{version}-%{release}

%description -n python3-textile+develop
Metapackage for python3-textile develop extras.

%package -n       python3-textile+imagesize
Summary:        Metapackage for python3-textile imagesize extras
Requires:       python3-textile = %{version}-%{release}
Requires:       python3dist(pillow) >= 3.0.0
Provides:       python3dist(textile[imagesize]) = %{version}-%{release}

%description -n python3-textile+imagesize
Metapackage for python3-textile imagesize extras.

%description

%package -n     python3-textile
Summary:        Textile processing for python.
# oreon:reqs
Requires:       python3dist(regex) > 1.0
# /oreon:reqs
%description -n python3-textile

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir textile-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-textile usr/lib/python3*/site-packages/textile* usr/lib64/python3*/site-packages/textile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/textile* usr/lib64/python3*/site-packages/textile* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-textile -f %{oreon_filedir}/python3-textile.list

%changelog

%autochangelog
