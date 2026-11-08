# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1cb83e4f702e60b8211ab5ec4c2afbab1b1dec80209456a7d2faf7584ed225ea

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global has_which2_alias 1

Summary: Displays where a particular program in your path is located
Name: which
Version:        2.25
Release:        1%{?dist}
License: GPL-3.0-only
Url: https://savannah.gnu.org/projects/which/
Source0:        https://mirror.cs.odu.edu/gnu/which/which-%{version}.tar.gz
Source1: which2.sh
Source2: which2.csh
Patch0:        which-2.25-warning.patch
Requires: coreutils
BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: readline-devel
BuildRequires:  oreon-rpm-macros

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%oreon_sha256

%autosetup -p1
 
%build
%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
%if %{has_which2_alias}
    install -p -m 644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
%endif
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%license COPYING
%doc EXAMPLES README AUTHORS NEWS
%if %{has_which2_alias}
%attr(0644,root,root) %{_sysconfdir}/profile.d/which2.*
%endif
%{_bindir}/which
%{_infodir}/which.info*
%{_mandir}/man1/which.1*

