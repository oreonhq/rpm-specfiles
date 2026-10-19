%global source0_hash d6625b2d3435ca814c9dd6590d39ae58ebeb8a4891eecb81446ad8b3e917f39b
Name:           python-unicode-segmentation-rs
Version:        0.3.3
Release:        1%{?dist}
Summary:        Unicode segmentation and width for Python using Rust
License:        Apache-2.0
URL:            https://weblate.org/
Source0:        https://files.pythonhosted.org/packages/source/u/unicode_segmentation_rs/unicode_segmentation_rs-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.14.0
Requires:       python3-unicode-segmentation-rs = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-unicode-segmentation-rs
Summary:        Unicode segmentation and width for Python using Rust
%description -n python3-unicode-segmentation-rs

%prep
%global oreon_srcdir unicode_segmentation_rs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-unicode-segmentation-rs usr/lib/python3*/site-packages/unicode_segmentation_rs* usr/lib64/python3*/site-packages/unicode_segmentation_rs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/unicode_segmentation_rs* usr/lib64/python3*/site-packages/unicode_segmentation_rs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-unicode-segmentation-rs -f %{oreon_filedir}/python3-unicode-segmentation-rs.list

%changelog

%autochangelog
