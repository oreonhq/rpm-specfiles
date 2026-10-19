%global source0_hash f992dac2aecc75c9a0ca0abb848f524aa1361635c866f7c42365b95bb41b78b2
Name:           python-flufl-bounce
Version:        5.0.1
Release:        1%{?dist}
Summary:        Email bounce detectors
License:        Apache-2.0
URL:            https://fluflbounce.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/f/flufl_bounce/flufl_bounce-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flufl-bounce = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flufl-bounce
Summary:        Email bounce detectors
%description -n python3-flufl-bounce

%prep
%global oreon_srcdir flufl_bounce-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flufl-bounce usr/lib/python3*/site-packages/flufl_bounce* usr/lib64/python3*/site-packages/flufl_bounce* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flufl_bounce* usr/lib64/python3*/site-packages/flufl_bounce* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flufl-bounce -f %{oreon_filedir}/python3-flufl-bounce.list

%changelog

%autochangelog
