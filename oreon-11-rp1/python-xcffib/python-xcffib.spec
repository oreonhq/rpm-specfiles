%global source0_hash 43452de509c1264d5bcea4bc025ca1bf68272d240ef26d3340b46e11f63d3d4a
Name:           python-xcffib
Version:        1.12.0
Release:        1%{?dist}
Summary:        xcffib is the XCB binding for python
License:        ...
URL:            http://github.com/tych0/xcffib
Source0:        https://files.pythonhosted.org/packages/source/x/xcffib/xcffib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-xcffib = %{version}-%{release}
# /oreon:deps
%package -n       python3-xcffib+dev
Summary:        Metapackage for python3-xcffib dev extras
Requires:       python3-xcffib = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.4
Provides:       python3dist(xcffib[dev]) = %{version}-%{release}

%description -n python3-xcffib+dev
Metapackage for python3-xcffib dev extras.

%description

%package -n     python3-xcffib
Summary:        xcffib is the XCB binding for python
# oreon:reqs
Requires:       python3dist(cffi) >= 1.1.0
# /oreon:reqs
%description -n python3-xcffib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir xcffib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xcffib usr/lib/python3*/site-packages/xcffib* usr/lib64/python3*/site-packages/xcffib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xcffib* usr/lib64/python3*/site-packages/xcffib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xcffib -f %{oreon_filedir}/python3-xcffib.list

%changelog

%autochangelog
