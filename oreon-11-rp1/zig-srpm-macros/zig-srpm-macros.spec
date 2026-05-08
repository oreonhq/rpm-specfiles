Name:           zig-srpm-macros
Version:        1
Release:        %autorelease
Summary:        SRPM macros required for Zig packages
License:        MIT
URL:            https://ziglang.org/

Source0:        macros.zig-srpm
Source1:        LICENSE

BuildArch:      noarch

Requires:       rpm

%description
Macros used when building Zig source RPMs on RPM-based distributions.

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.zig-srpm
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%license %{_datadir}/licenses/%{name}/LICENSE
%{_rpmmacrodir}/macros.zig-srpm

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-1
- Import from Fedora 44 dist-git, debrand docs and changelog
