%global source0_hash 1cc89ac40a9d8eb30914917f62e1cf793c744510104a7b7870668bfc9d39f94c
%global debug_package %{nil}

Name: kernel-srpm-macros
Version: 1.0
Release: 32%{?dist}
Summary: SRPM macros for kernel module packages
License: MIT
URL: https://kernel.org/
BuildArch: noarch
Source0: macros.kernel-srpm
Source1: kmod.attr

BuildRequires: oreon-rpm-macros

%description
Macros that list the arches a full kernel is built on, and the kmod file attribute.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
mkdir -p %{buildroot}%{_fileattrsdir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.kernel-srpm
install -m 644 %{SOURCE1} %{buildroot}%{_fileattrsdir}/kmod.attr

%files
%{_rpmconfigdir}/macros.d/macros.kernel-srpm
%{_fileattrsdir}/kmod.attr
