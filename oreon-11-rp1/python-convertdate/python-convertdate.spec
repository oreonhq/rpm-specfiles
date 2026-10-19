%global source0_hash 8ade438cced7eae579e622f3f54354e52609840f597f7b09a16d7789a15d4e0a
Name:           python-convertdate
Version:        2.5.1
Release:        1%{?dist}
Summary:        Converts between Gregorian dates and other calendar systems
License:        MIT
URL:            https://github.com/fitnr/convertdate
Source0:        https://files.pythonhosted.org/packages/source/c/convertdate/convertdate-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.1.1
Requires:       python3-convertdate = %{version}-%{release}
# /oreon:deps
%package -n       python3-convertdate+tests
Summary:        Metapackage for python3-convertdate tests extras
Requires:       python3-convertdate = %{version}-%{release}
Provides:       python3dist(convertdate[tests]) = %{version}-%{release}

%description -n python3-convertdate+tests
Metapackage for python3-convertdate tests extras.

%package -n       python3-convertdate+docs
Summary:        Metapackage for python3-convertdate docs extras
Requires:       python3-convertdate = %{version}-%{release}
Provides:       python3dist(convertdate[docs]) = %{version}-%{release}

%description -n python3-convertdate+docs
Metapackage for python3-convertdate docs extras.

%package -n       python3-convertdate+dev
Summary:        Metapackage for python3-convertdate dev extras
Requires:       python3-convertdate = %{version}-%{release}
Provides:       python3dist(convertdate[dev]) = %{version}-%{release}

%description -n python3-convertdate+dev
Metapackage for python3-convertdate dev extras.

%description

%package -n     python3-convertdate
Summary:        Converts between Gregorian dates and other calendar systems
# oreon:reqs
Requires:       python3dist(pymeeus) <= 1
Requires:       python3dist(pymeeus) >= 0.3.13
# /oreon:reqs
%description -n python3-convertdate

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir convertdate-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-convertdate usr/lib/python3*/site-packages/convertdate* usr/lib64/python3*/site-packages/convertdate* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/convertdate* usr/lib64/python3*/site-packages/convertdate* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-convertdate -f %{oreon_filedir}/python3-convertdate.list

%changelog

%autochangelog
