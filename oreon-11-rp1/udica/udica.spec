%global source0_hash f5453a3cdc8c7f82ad4155be9356339a579ac6cea21c10b64ca8cfe636854931
Summary:        A tool for generating SELinux security policies for containers
Name: udica
Version: 0.2.8
Release:        1%{?dist}
Source0:        https://github.com/containers/udica/archive/refs/tags/v%{version}.tar.gz#/udica-0.2.8.tar.gz
Patch0001: 0001-Add-option-to-generate-custom-policy-for-a-confined-.patch
Patch0002: 0002-Add-tests-covering-confined-user-policy-generation.patch
Patch0003: 0003-confined-make-l-non-optional.patch
Patch0004: 0004-confined-allow-asynchronous-I-O-operations.patch
Patch0005: 0005-use-relative-paths-it-s-undefined-behavior-with-abso.patch
License: GPL-3.0-or-later
BuildArch: noarch
Url: https://github.com/containers/udica
Requires: python2 libsemanage-python libselinux-python
Requires: container-selinux >= 2.168.0-2
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-udica = %{version}-%{release}
# /oreon:deps
%description
Tool for generating SELinux security profiles for containers based on
inspection of container JSON file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install --directory %{buildroot}%{_datadir}/udica/macros
install --directory %{buildroot}%{_mandir}/man8
install -m 0644 udica/man/man8/udica.8 %{buildroot}%{_mandir}/man8/udica.8
%oreon_autofiles main

%files

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.8-12
- Prepare for Oreon 11 (RP1)
