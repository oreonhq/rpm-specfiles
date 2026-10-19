%global source0_hash 6cadd8b0c7757bd367d1eb8b7c107c6d933d7528b0917440d4e57e646e82a3d1
Name:           python-tvb-data
Version:        3.0.0
Release:        1%{?dist}
Summary:        Demo data for The Virtual Brain software
License:        GPL-3.0-or-later
URL:            https://gitlab.ebrains.eu/ri/tech-hub/apps/tvb/tvb-data
Source0:        https://files.pythonhosted.org/packages/source/t/tvb_data/tvb_data-%{version}.tar.gz
BuildArch:      noarch
%global desc %{expand:
The Virtual Brain Project (TVB Project) has the purpose of offering some modern
tools to the Neurosciences community, for computing, simulating and analyzing
functional and structural data of human brains.
Various demonstration datasets for use with The Virtual Brain are provided
here.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tvb-data = %{version}-%{release}
# /oreon:deps
%description %{desc}

%package -n python3-tvb-data
Summary:        Demo data for The Virtual Brain software
%description -n python3-tvb-data %{desc}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tvb-data usr/lib/python3*/site-packages/tvb_data* usr/lib64/python3*/site-packages/tvb_data* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tvb_data* usr/lib64/python3*/site-packages/tvb_data* usr/bin/*

%files
%files -n python3-tvb-data -f %{oreon_filedir}/python3-tvb-data.list

%changelog

%autochangelog
