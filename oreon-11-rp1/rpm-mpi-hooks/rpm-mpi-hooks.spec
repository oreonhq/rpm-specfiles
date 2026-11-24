# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8b8458d93356b88b85d2321f729da18537363462787df531a57502f895bd42b1
%global source1_hash 8584e0f1a07eeacced37833918ac261fc18d16c8d9b0f8f1832cb34ba9c7d21b
%global source2_hash 39e17c993c1049078f826af15bd0752eaee89e61a053273f930b47e2a340cb47
%global source3_hash 9a4acb5a11fa990f988cec61fa3f414c2ebd4acc13a1cc1eb2a59b5275cead62
%global source4_hash ed63cac2509574c03d471698565e1dc056a48b41bcbbd29ddcae9d5e2cc7325c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           rpm-mpi-hooks
Version:        8
Release:        1%{?dist}
Summary:        RPM dependency generator hooks for MPI packages

License:        MIT
BuildArch:      noarch

Source0:        mpi.attr
Source1:        mpilibsymlink.attr
Source2:        mpi.prov
Source3:        mpi.req
Source4:        LICENSE

Requires:       filesystem
Requires:       environment-modules

%description
RPM dependency generator hooks for MPI packages. This package should be added
as a BuildRequires to all mpi implementations (i.e. openmpi, mpich) as well as
a Requires to the their -devel packages.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
cp -a %SOURCE4 .

%build

%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/fileattrs/mpi.attr
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/fileattrs/mpilibsymlink.attr
install -Dpm 0755 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/mpi.prov
install -Dpm 0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/mpi.req

%files
%license LICENSE
%{_rpmconfigdir}/fileattrs/mpi.attr
%{_rpmconfigdir}/fileattrs/mpilibsymlink.attr
%{_rpmconfigdir}/mpi.req
%{_rpmconfigdir}/mpi.prov

%changelog
%autochangelog
