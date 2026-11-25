# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: CC-BY-SA-4.0

%global source0_hash 3bc7580caabef7e42c161180bc1a27095962c377acbde7ec0ee4d8da130e7857

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}

%bcond bootstrap 0

%oreon_bootstrap

Name: cosmic-wallpapers

Version: 1.12.0

Release: 1%{?dist}

Summary: Wallpapers for the COSMIC Desktop Environment

License: CC-BY-SA-4.0

URL: https://github.com/pop-os/cosmic-wallpapers

Source0: https://github.com/pop-os/cosmic-wallpapers/archive/refs/tags/epoch-1.12.0.tar.gz

BuildArch: noarch

BuildRequires: oreon-rpm-macros

BuildRequires: make

%description

Wallpapers for the COSMIC Desktop Environment

%prep

%oreon_sha256

%autosetup -n cosmic-wallpapers-epoch-1.12.0

%install

make DESTDIR=%{buildroot} prefix=%{_prefix} install

%oreon_filelist

%check

test -d %{buildroot}%{_datadir}/backgrounds

%files -f %{_builddir}/%{name}.files

%license LICENSE

%doc README.md

%changelog

%autochangelog
