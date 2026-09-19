%global source0_hash 5263b7b2d0f5a8de2eb409421284947df6229b67bca0055fa10da38153835815

Name:           python-wcag-contrast-ratio
Version:        0.9
Release:        17%{?dist}
Summary:        A library for computing contrast ratios, as required by WCAG 2.0
# SPDX
License:        MIT
URL:            https://github.com/gsnedders/wcag-contrast-ratio
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A library for computing contrast ratios, as required by WCAG 2.0.}

%description %_description

%package -n     python3-wcag-contrast-ratio
Summary:        %{summary}

%description -n python3-wcag-contrast-ratio %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n wcag-contrast-ratio-%{version}

# - functionality of hypothesis-pytest is now included into hypothesis
# - let our tox set the correct path to py.test
# both issues reported: https://github.com/gsnedders/wcag-contrast-ratio/pull/5
sed -i 's/hypothesis-pytest/hypothesis/g' tox.ini
sed -i 's/{envbindir}\/py.test/py.test/g' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wcag_contrast_ratio

%check
%tox

%files -n python3-wcag-contrast-ratio -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
