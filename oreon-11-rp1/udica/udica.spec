# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 f5453a3cdc8c7f82ad4155be9356339a579ac6cea21c10b64ca8cfe636854931
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
