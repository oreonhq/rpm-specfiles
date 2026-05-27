%global source0_hash none

Name:           gap-srpm-macros
Version:        2
Release:        %autorelease
Summary:        Macros for building GAP source RPMs

License:        MIT
URL:            https://www.gap-system.org/

BuildArch:      noarch

Source0:        macros.gap-srpm
Source1:        LICENSE

%description
Macros needed to build GAP package source RPMs on RPM-based distributions.

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.gap-srpm
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%license %{_datadir}/licenses/%{name}/LICENSE
%{_rpmmacrodir}/macros.gap-srpm

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2-1
- Import from Fedora 44 dist-git, debrand URL, replace changelog
