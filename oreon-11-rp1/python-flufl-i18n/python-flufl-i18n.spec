%global source0_hash 84f2076c1ff85cea1c8b8f5c66e8c41e5d61834d923cb3e6df4392a3b237a12d
Name:           python-flufl-i18n
Version:        6.0.0
Release:        1%{?dist}
Summary:        A high level API for internationalizing Python libraries and applications
License:        Apache-2.0
URL:            https://flufli18n.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/f/flufl_i18n/flufl_i18n-%{version}.tar.gz
BuildArch:      noarch
Patch:          flufl_i18n-no-covtest.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flufl-i18n = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flufl-i18n
Summary:        A high level API for internationalizing Python libraries and applications
%description -n python3-flufl-i18n

%prep
%global oreon_srcdir flufl_i18n-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flufl-i18n usr/lib/python3*/site-packages/flufl_i18n* usr/lib64/python3*/site-packages/flufl_i18n* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flufl_i18n* usr/lib64/python3*/site-packages/flufl_i18n* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flufl-i18n -f %{oreon_filedir}/python3-flufl-i18n.list

%changelog

%autochangelog
