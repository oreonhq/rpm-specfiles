%global source0_hash fb6b8048af08d4ab061610d5b7d3696a7e4c95337dbda880edb9f95812cabc20
Name:           python-marshmallow
Version:        4.3.1
Release:        1%{?dist}
Summary:        A lightweight library for converting complex datatypes to and from native Python datatypes.
License:        MIT
URL:            https://github.com/marshmallow-code/marshmallow
Source0:        https://files.pythonhosted.org/packages/source/m/marshmallow/marshmallow-%{version}.tar.gz
BuildArch:      noarch
Patch0:         ordered_set.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.12
Requires:       python3-marshmallow = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-marshmallow
Summary:        A lightweight library for converting complex datatypes to and from native Python datatypes.
%description -n python3-marshmallow

%prep
%global oreon_srcdir marshmallow-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-marshmallow usr/lib/python3*/site-packages/marshmallow* usr/lib64/python3*/site-packages/marshmallow* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/marshmallow* usr/lib64/python3*/site-packages/marshmallow* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-marshmallow -f %{oreon_filedir}/python3-marshmallow.list

%changelog

%autochangelog
