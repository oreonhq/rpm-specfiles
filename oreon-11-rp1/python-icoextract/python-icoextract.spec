%global source0_hash 8fb4584671662e61814a48e3f2fed30d083a1aede68947a0cb07ddb7f59238ec
Name:           python-icoextract
Version:        0.3.0
Release:        1%{?dist}
Summary:        Windows EXE icon extractor
License:        MIT
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/i/icoextract/icoextract-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0.0
Requires:       python3-icoextract = %{version}-%{release}
# /oreon:deps
%package -n       python3-icoextract+thumbnailer
Summary:        Metapackage for python3-icoextract thumbnailer extras
Requires:       python3-icoextract = %{version}-%{release}
Provides:       python3dist(icoextract[thumbnailer]) = %{version}-%{release}

%description -n python3-icoextract+thumbnailer
Metapackage for python3-icoextract thumbnailer extras.

%package -n       python3-icoextract+win16
Summary:        Metapackage for python3-icoextract win16 extras
Requires:       python3-icoextract = %{version}-%{release}
Provides:       python3dist(icoextract[win16]) = %{version}-%{release}

%description -n python3-icoextract+win16
Metapackage for python3-icoextract win16 extras.

%package -n       python3-icoextract+dev
Summary:        Metapackage for python3-icoextract dev extras
Requires:       python3-icoextract = %{version}-%{release}
Provides:       python3dist(icoextract[dev]) = %{version}-%{release}

%description -n python3-icoextract+dev
Metapackage for python3-icoextract dev extras.

%description

%package -n     python3-icoextract
Summary:        Windows EXE icon extractor
%description -n python3-icoextract

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir icoextract-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-icoextract usr/lib/python3*/site-packages/icoextract* usr/lib64/python3*/site-packages/icoextract* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/icoextract* usr/lib64/python3*/site-packages/icoextract* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-icoextract -f %{oreon_filedir}/python3-icoextract.list

%changelog

%autochangelog
