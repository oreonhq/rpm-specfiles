%global source0_hash 95066ed8810dd61e2ffac4adb47e947c1840b36c8fcedd23edd960b7135ac302
Name:           python-pyongc
Version:        1.2.2
Release:        1%{?dist}
Summary:        Python interface to OpenNGC database data
License:        MIT AND CC-BY-SA-4.0
URL:            https://github.com/mattiaverga/PyOngc
Source0:        https://files.pythonhosted.org/packages/source/p/pyongc/pyongc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27
Requires:       python3-pyongc = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyongc+data
Summary:        Metapackage for python3-pyongc data extras
Requires:       python3-pyongc = %{version}-%{release}
Requires:       python3dist(pandas) >= 2
Requires:       python3dist(pandas) < 4
Provides:       python3dist(pyongc[data]) = %{version}-%{release}

%description -n python3-pyongc+data
Metapackage for python3-pyongc data extras.

%package -n       python3-pyongc+development
Summary:        Metapackage for python3-pyongc development extras
Requires:       python3-pyongc = %{version}-%{release}
Provides:       python3dist(pyongc[development]) = %{version}-%{release}

%description -n python3-pyongc+development
Metapackage for python3-pyongc development extras.

%package -n       python3-pyongc+docs
Summary:        Metapackage for python3-pyongc docs extras
Requires:       python3-pyongc = %{version}-%{release}
Requires:       python3dist(pandas) >= 2
Requires:       python3dist(pandas) < 4
Requires:       python3dist(sphinx) >= 9.1
Requires:       python3dist(sphinx-rtd-theme) >= 3.0
Provides:       python3dist(pyongc[docs]) = %{version}-%{release}

%description -n python3-pyongc+docs
Metapackage for python3-pyongc docs extras.

%description

%package -n     python3-pyongc
Summary:        Python interface to OpenNGC database data
# oreon:reqs
Requires:       python3dist(click) >= 8.0
Requires:       python3dist(numpy) >= 2.0
# /oreon:reqs
%description -n python3-pyongc

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyongc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyongc usr/lib/python3*/site-packages/pyongc* usr/lib64/python3*/site-packages/pyongc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyongc* usr/lib64/python3*/site-packages/pyongc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyongc -f %{oreon_filedir}/python3-pyongc.list

%changelog

%autochangelog
