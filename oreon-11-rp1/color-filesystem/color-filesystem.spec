# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           color-filesystem
Version:        1
Release:        1%{?dist}
Summary:        Color filesystem layout
License:        LicenseRef-Not-Copyrightable
BuildArch:      noarch

BuildRequires: oreon-rpm-macros

Requires:  filesystem
Requires:  rpm

%description
This package provides some directories that are required/used to store color.

%prep
:

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/color/icc
mkdir -p %{buildroot}%{_datadir}/color/cmms
mkdir -p %{buildroot}%{_datadir}/color/settings
mkdir -p %{buildroot}%{_localstatedir}/lib/color/icc
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
cat >%{buildroot}%{_rpmconfigdir}/macros.d/macros.color <<'ENDMACROS'
%_colordir %_datadir/color
%_syscolordir %_colordir
%_icccolordir %_colordir/icc
%_cmmscolordir %_colordir/cmms
%_settingscolordir %_colordir/settings
ENDMACROS

%files
%dir %{_datadir}/color
%dir %{_datadir}/color/icc
%dir %{_datadir}/color/cmms
%dir %{_datadir}/color/settings
%dir %{_localstatedir}/lib/color
%dir %{_localstatedir}/lib/color/icc
%{_rpmconfigdir}/macros.d/macros.color

%changelog
%autochangelog
