%global source0_hash none
Name:           zig-srpm-macros
Version:        1
Release:        1%{?dist}
Summary:        SRPM macros required for Zig packages
License:        MIT
URL:            https://ziglang.org/
Source0:        macros.zig-srpm
Source1:        LICENSE
BuildArch:      noarch
Requires:       rpm
# oreon:deps

# /oreon:deps
%description
Macros used when building Zig source RPMs on RPM-based distributions.

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.zig-srpm
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-1
- Import from Fedora 44 dist-git, debrand docs and changelog
