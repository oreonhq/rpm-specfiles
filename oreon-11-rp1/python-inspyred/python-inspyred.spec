%global source0_hash acc1215003a8937ef174f2719e8256bf21b4bb67a9aa7de495db6044f4055961
Name:           python-inspyred
Version:        1.0.3
Release:        1%{?dist}
Summary:        A framework for creating bio-inspired computational intelligence algorithms in Python
License:        MIT
URL:            https://github.com/aarongarrett/inspyred
Source0:        https://files.pythonhosted.org/packages/source/i/inspyred/inspyred-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-inspyred = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-inspyred
Summary:        A framework for creating bio-inspired computational intelligence algorithms in Python
%description -n python3-inspyred

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir inspyred-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-inspyred usr/lib/python3*/site-packages/inspyred* usr/lib64/python3*/site-packages/inspyred* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/inspyred* usr/lib64/python3*/site-packages/inspyred* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-inspyred -f %{oreon_filedir}/python3-inspyred.list

%changelog

%autochangelog
