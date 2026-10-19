%global source0_hash 669c04cbc83e64dc580c5c350d773efab7363c300c7934aec57cc35943f5b913
Name:           python-dragonmapper
Version:        0.3.0
Release:        1%{?dist}
Summary:        Identification and conversion functions for Chinese text processing
License:        MIT
URL:            https://github.com/tsroten/dragonmapper
Source0:        https://github.com/tsroten/dragonmapper/archive/v%{version}/dragonmapper-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dragonmapper = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dragonmapper
Summary:        Identification and conversion functions for Chinese text processing
# oreon:reqs
Requires:       python3dist(hanzidentifier) >= 1.2
Requires:       python3dist(zhon) >= 2.0
# /oreon:reqs
%description -n python3-dragonmapper

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dragonmapper-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dragonmapper usr/lib/python3*/site-packages/dragonmapper* usr/lib64/python3*/site-packages/dragonmapper* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dragonmapper* usr/lib64/python3*/site-packages/dragonmapper* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-dragonmapper -f %{oreon_filedir}/python3-dragonmapper.list

%changelog

%autochangelog
