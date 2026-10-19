%global source0_hash none
Name:           fpc-srpm-macros
Version:        1.3
Release:        1%{?dist}
Summary:        RPM macros needed by packages built with Free Pascal Compiler
License:        MIT
URL:            https://www.freepascal.org/
Source0:        macros.fpc-srpm
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
This package contains RPM macros needed by packages built with the
Free Pascal Compiler. For example it exposes a macro listing architectures
where FPC is expected to be available.

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.fpc-srpm
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-1
- Import from Fedora 44 dist-git, debrand spec and macro comments, replace changelog
