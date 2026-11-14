# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bb0d4c54bac2990e1bdf8132f2c9477ae752859d523e141e72b3b11a12c26e7b

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           chrpath
Version:        0.16
Release:        1%{?dist}
Summary:        Modify rpath of compiled programs
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/chrpath
Source0:        https://deb.debian.org/debian/pool/main/c/chrpath/chrpath_%{version}.orig.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%oreon_sha256
%autosetup -n chrpath-%{version}

%build
%configure
%make_build

%install
%make_install
rm -fr %{buildroot}%{_prefix}/doc

%check
make check

%files
%doc AUTHORS README NEWS ChangeLog*
%license COPYING
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1*

%changelog
%autochangelog
