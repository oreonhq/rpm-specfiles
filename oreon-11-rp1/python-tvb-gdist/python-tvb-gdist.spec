%global source0_hash 9f8843d4fd4a945979e3f26a87da895022d45145775228fa706a43caa8965df8
Name:           python-tvb-gdist
Version:        2.9.2
Release:        1%{?dist}
Summary:        Compute geodesic distances
License:        ...
URL:            https://github.com/the-virtual-brain/tvb-gdist
Source0:        https://files.pythonhosted.org/packages/source/t/tvb_gdist/tvb_gdist-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tvb-gdist = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tvb-gdist
Summary:        Compute geodesic distances
%description -n python3-tvb-gdist

%prep
%global oreon_srcdir tvb_gdist-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tvb-gdist usr/lib/python3*/site-packages/tvb_gdist* usr/lib64/python3*/site-packages/tvb_gdist* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tvb_gdist* usr/lib64/python3*/site-packages/tvb_gdist* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tvb-gdist -f %{oreon_filedir}/python3-tvb-gdist.list

%changelog

%autochangelog
