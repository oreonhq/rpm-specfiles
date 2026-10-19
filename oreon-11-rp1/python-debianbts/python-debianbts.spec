%global source0_hash f443b18ce2411b373103784715e6707df034f48dad7be387a6917b16e154d793
Name:           python-debianbts
Version:        4.1.1
Release:        1%{?dist}
Summary:        Python interface to Debian_s Bug Tracking System
License:        MIT
URL:            https://github.com/venthur/python-debianbts
Source0:        https://files.pythonhosted.org/packages/source/p/python_debianbts/python_debianbts-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64.0
Requires:       python3-debianbts = %{version}-%{release}
# /oreon:deps
%package -n       python3-debianbts+dev
Summary:        Metapackage for python3-debianbts dev extras
Requires:       python3-debianbts = %{version}-%{release}
Provides:       python3dist(debianbts[dev]) = %{version}-%{release}

%description -n python3-debianbts+dev
Metapackage for python3-debianbts dev extras.

%description

%package -n     python3-python-debianbts
Summary:        Python interface to Debian_s Bug Tracking System
%description -n python3-python-debianbts

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir python_debianbts-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-python-debianbts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-python-debianbts -f %{oreon_filedir}/python3-python-debianbts.list

%changelog

%autochangelog
