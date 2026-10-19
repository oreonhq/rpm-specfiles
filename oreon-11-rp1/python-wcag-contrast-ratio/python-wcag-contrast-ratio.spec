%global source0_hash 5263b7b2d0f5a8de2eb409421284947df6229b67bca0055fa10da38153835815
Name:           python-wcag-contrast-ratio
Version:        0.9
Release:        1%{?dist}
Summary:        A library for computing contrast ratios, as required by WCAG 2.0
License:        MIT
URL:            https://github.com/gsnedders/wcag-contrast-ratio
Source0:        https://github.com/gsnedders/wcag-contrast-ratio/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wcag-contrast-ratio = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wcag-contrast-ratio
Summary:        A library for computing contrast ratios, as required by WCAG 2.0
%description -n python3-wcag-contrast-ratio

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n wcag-contrast-ratio-%{version}

# - functionality of hypothesis-pytest is now included into hypothesis
# - let our tox set the correct path to py.test
# both issues reported: https://github.com/gsnedders/wcag-contrast-ratio/pull/5
sed -i 's/hypothesis-pytest/hypothesis/g' tox.ini
sed -i 's/{envbindir}\/py.test/py.test/g' tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wcag-contrast-ratio usr/lib/python3*/site-packages/wcag_contrast_ratio* usr/lib64/python3*/site-packages/wcag_contrast_ratio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wcag_contrast_ratio* usr/lib64/python3*/site-packages/wcag_contrast_ratio* usr/bin/*

%check

%tox
%files
%files -n python3-wcag-contrast-ratio -f %{oreon_filedir}/python3-wcag-contrast-ratio.list

%changelog

%autochangelog
