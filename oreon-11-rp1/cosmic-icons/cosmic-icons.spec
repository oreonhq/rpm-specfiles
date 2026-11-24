# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: CC-BY-SA-4.0

%global source0_hash 1cbe6ca6ad3743a26b84ab17d3f7b8e5a885fcbcbb2d071ff0b74bccb5b44a53

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}

%bcond bootstrap 0

%oreon_bootstrap

Name: cosmic-icons

Version: 1.11.0

Release: 1%{?dist}

Summary: Icon theme for the COSMIC Desktop Environment

License: CC-BY-SA-4.0

URL: https://github.com/pop-os/cosmic-icons

Source0: https://github.com/pop-os/cosmic-icons/archive/refs/tags/epoch-1.11.0.tar.gz

BuildArch: noarch

BuildRequires: oreon-rpm-macros

BuildRequires: just

%description

Icon theme for the COSMIC Desktop Environment

%prep

%oreon_sha256

%autosetup -n cosmic-icons-epoch-1.11.0

%install

just rootdir=%{buildroot} prefix=%{_prefix} install

%oreon_filelist

%check

test -d %{buildroot}%{_datadir}/icons

%files -f %{_builddir}/%{name}.files

%changelog

%autochangelog
