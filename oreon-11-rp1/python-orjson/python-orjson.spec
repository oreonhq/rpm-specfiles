%global source0_hash d14203fb1aae2ad9b3d52f8a0e82aeb10197ef1c9bc61da7f358bd70b00123d5
Name:           python-orjson
Version:        3.12.0
Release:        1%{?dist}
Summary:        Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
License:        MPL-2.0 AND (Apache-2.0 OR MIT)
URL:            https://github.com/ijl/orjson
Source0:        https://files.pythonhosted.org/packages/source/o/orjson/orjson-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(maturin) >= 1
Requires:       python3-orjson = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-orjson
Summary:        Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy
%description -n python3-orjson

%prep
%global oreon_srcdir orjson-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-orjson usr/lib/python3*/site-packages/orjson* usr/lib64/python3*/site-packages/orjson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/orjson* usr/lib64/python3*/site-packages/orjson* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-orjson -f %{oreon_filedir}/python3-orjson.list

%changelog

%autochangelog
