# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1dfe42d83a51282260afb6f2438b345198dc483d287a791d9f716306a0372c89
%global debug_package %{nil}

Name: package-notes-srpm-macros
Version: 0.17
Release: 2%{?dist}
Summary: RPM macros that stamp package notes into ELF binaries
License: MIT
URL: https://github.com/systemd/package-notes
BuildArch: noarch
Source0: https://github.com/systemd/package-notes/archive/refs/tags/v%{version}.tar.gz
Obsoletes: package-notes < 0.5
Conflicts: binutils < 2.37-34
Conflicts: binutils-gold < 2.37-34
Conflicts: mold < 1.3.0
Conflicts: lld < 14.0.5-4

BuildRequires: oreon-rpm-macros

%description
Macros that pass --package-metadata to the linker so ELF notes record the RPM name and version.

%prep
%autosetup -n package-notes-%{version} -p1
%oreon_sha256

%build
sed 's|@OSCPE@|cpe:/o:oreon:oreon:11|' rpm/redhat-package-notes.in > oreon-package-notes
sed -i 's|/usr/lib/rpm/redhat/redhat-package-notes|%{_rpmconfigdir}/oreon/oreon-package-notes|' rpm/macros.package-notes-srpm

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}/oreon
install -m 644 rpm/macros.package-notes-srpm %{buildroot}%{_rpmmacrodir}/macros.package-notes-srpm
install -m 644 oreon-package-notes %{buildroot}%{_rpmconfigdir}/oreon/oreon-package-notes

%files
%{_rpmmacrodir}/macros.package-notes-srpm
%{_rpmconfigdir}/oreon/oreon-package-notes
