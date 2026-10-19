%global source0_hash a19d9f542beb3ce5ecb4ca780b47092c785725263e339bed8e7d340b322c4f9d
Name:           python-playsound3
Version:        3.3.2
Release:        1%{?dist}
Summary:        Cross-platform library to play audio files
License:        MIT
URL:            https://github.com/szmikler/playsound3
Source0:        https://files.pythonhosted.org/packages/source/p/playsound3/playsound3-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-playsound3 = %{version}-%{release}
# /oreon:deps
%package -n       python3-playsound3+dev
Summary:        Metapackage for python3-playsound3 dev extras
Requires:       python3-playsound3 = %{version}-%{release}
Provides:       python3dist(playsound3[dev]) = %{version}-%{release}

%description -n python3-playsound3+dev
Metapackage for python3-playsound3 dev extras.

%description

%package -n     python3-playsound3
Summary:        Cross-platform library to play audio files
%description -n python3-playsound3

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir playsound3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-playsound3 usr/lib/python3*/site-packages/playsound3* usr/lib64/python3*/site-packages/playsound3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/playsound3* usr/lib64/python3*/site-packages/playsound3* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-playsound3 -f %{oreon_filedir}/python3-playsound3.list

%changelog

%autochangelog
