%global source0_hash a0d6fd43cd9d519e65d83cb8f78e9310756d2104efa5ee521952df75bb8b5efb
%global debug_package %{nil}

Name: pyproject-srpm-macros
Version: 1.18.7
Release: 1%{?dist}
Summary: SRPM macros for pyproject packages
License: MIT
URL: https://github.com/rpm-software-management/pyproject-rpm-macros
BuildArch: noarch
Source0: macros.aaa-pyproject-srpm
Source1: LICENSE
Requires: (pyproject-rpm-macros = %{version}-%{release} if pyproject-rpm-macros)
Requires: (rpm-build >= 4.14.90 if rpm-build)

BuildRequires: oreon-rpm-macros

%description
SRPM macros that load before the rest of the pyproject macros.

%prep
%oreon_sha256
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.aaa-pyproject-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.aaa-pyproject-srpm
