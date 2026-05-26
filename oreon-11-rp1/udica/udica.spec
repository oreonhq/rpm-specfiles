Summary: A tool for generating SELinux security policies for containers
Name: udica
Version: 0.2.8
Release: 12%{?dist}
Source0: https://github.com/containers/udica/archive/v%{version}.tar.gz
#git format-patch -N v0.2.8 -- . ':!.cirrus.yml' ':!.github'
Patch0001: 0001-Add-option-to-generate-custom-policy-for-a-confined-.patch
Patch0002: 0002-Add-tests-covering-confined-user-policy-generation.patch
Patch0003: 0003-confined-make-l-non-optional.patch
Patch0004: 0004-confined-allow-asynchronous-I-O-operations.patch
Patch0005: 0005-use-relative-paths-it-s-undefined-behavior-with-abso.patch
# oreon url source checksums begin
%global source0_sha256 f5453a3cdc8c7f82ad4155be9356339a579ac6cea21c10b64ca8cfe636854931
%global source0_file v0.2.8.tar.gz
# oreon url source checksums end
License: GPL-3.0-or-later
BuildArch: noarch
Url: https://github.com/containers/udica
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: python3 python3-devel
Requires: python3 python3-libsemanage python3-libselinux
%else
BuildRequires: python2 python2-devel python2-setuptools
Requires: python2 libsemanage-python libselinux-python
%endif
# container-selinux provides policy templates
Requires: container-selinux >= 2.168.0-2

%description
Tool for generating SELinux security profiles for containers based on
inspection of container JSON file.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v0.2.8.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f5453a3cdc8c7f82ad4155be9356339a579ac6cea21c10b64ca8cfe636854931" || { echo "oreon: Source0 SHA256 mismatch for v0.2.8.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

install --directory %{buildroot}%{_datadir}/udica/macros
install --directory %{buildroot}%{_mandir}/man8
install -m 0644 udica/man/man8/udica.8 %{buildroot}%{_mandir}/man8/udica.8

%files
%{_mandir}/man8/udica.8*
%{_bindir}/udica
%dir %{_datadir}/udica
%dir %{_datadir}/udica/ansible
%dir %{_datadir}/udica/macros
%{_datadir}/udica/ansible/*
%{_datadir}/udica/macros/*
%license LICENSE
%{python3_sitelib}/udica/
%{python3_sitelib}/udica-*.dist-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.8-12
- Prepare for Oreon 11 (RP1)
