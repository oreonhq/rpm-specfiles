%global source0_hash 67119c2aee93be821f077193bd8534e296c05b38bd174d9c5a80c4aa31d1a4d3
Name:           python-leather
Version:        0.4.1
Release:        1%{?dist}
Summary:        Python charting for 80% of humans.
License:        MIT
URL:            https://leather.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/l/leather/leather-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-leather = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-leather
Summary:        Python charting for 80% of humans.
%description -n python3-leather

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir leather-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-leather usr/lib/python3*/site-packages/leather* usr/lib64/python3*/site-packages/leather* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/leather* usr/lib64/python3*/site-packages/leather* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-leather -f %{oreon_filedir}/python3-leather.list

%changelog

%autochangelog
