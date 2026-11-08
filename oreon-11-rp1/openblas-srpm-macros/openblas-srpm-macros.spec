# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2de2df7d8176ba3a51926b1e1e38204d658ad6ca3b53ef3c381147ec1c5e37c2


%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           openblas-srpm-macros
Version:        2
Release:        2%{?dist}
Summary:        OpenBLAS architecture macros
License:        MIT
Source0:        macros.openblas-srpm
BuildArch:      noarch
BuildRequires:  oreon-rpm-macros

%description
%{summary}.


%prep
%oreon_sha256



%build


%install
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
mkdir -p %{buildroot}%{macrosdir}
install -m0644 %SOURCE0 %{buildroot}%{macrosdir}/macros.openblas-srpm


%files
%{macrosdir}/macros.openblas-srpm


