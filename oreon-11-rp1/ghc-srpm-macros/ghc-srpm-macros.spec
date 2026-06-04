%global source0_hash none

Name:           ghc-srpm-macros
Version:        1.10
Release:        %autorelease
Summary:        RPM macros for building Haskell source packages
License:        GPL-2.0-or-later
URL:            https://src.fedoraproject.org/rpms/ghc-srpm-macros

BuildArch:      noarch

Source0:        macros.ghc-srpm

%description
Macros used when generating Haskell source RPM packages.

%install
install -m 644 -D %{SOURCE0} \
    %{buildroot}%{_rpmconfigdir}/macros.d/macros.ghc-srpm

%files
%{_rpmconfigdir}/macros.d/macros.ghc-srpm

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10-1
- Import
