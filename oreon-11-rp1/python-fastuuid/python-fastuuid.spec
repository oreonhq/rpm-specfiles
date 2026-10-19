%global source0_hash 178947fc2f995b38497a74172adee64fdeb8b7ec18f2a5934d037641ba265d26
Name:           python-fastuuid
Version:        0.14.0
Release:        1%{?dist}
Summary:        Python bindings to Rust's UUID library
License:        %{shrink:
        BSD-3-Clause AND
        (Apache-2.0 OR MIT) AND
        (BSD-2-Clause OR Apache-2.0 OR MIT) AND
        BSD-3-Clause AND
        (MIT OR Apache-2.0) AND
        MIT AND
        (Zlib OR Apache-2.0 OR MIT)
}
URL:            https://github.com/thedrow/fastuuid/
Source0:        https://files.pythonhosted.org/packages/source/f/fastuuid/fastuuid-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-fastuuid = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fastuuid
Summary:        Python bindings to Rust's UUID library
%description -n python3-fastuuid

%prep
%oreon_prep
%build

%pyproject_wheel
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%pyproject_install
%oreon_autofiles python3-fastuuid usr/lib/python3*/site-packages/fastuuid* usr/lib64/python3*/site-packages/fastuuid* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastuuid* usr/lib64/python3*/site-packages/fastuuid* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-fastuuid -f %{oreon_filedir}/python3-fastuuid.list

%changelog

%autochangelog
