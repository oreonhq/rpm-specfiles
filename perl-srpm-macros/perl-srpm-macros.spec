Name:       perl-srpm-macros    
Version:    1
Release:    61%{?dist}
Summary:    RPM macros for building Perl source package from source repository
License:    GPL-3.0-or-later
Source0:    macros.perl-srpm
BuildArch:  noarch

%description
These RPM macros are used for building Perl source packages from source
repositories. They influence build-requires set into the source package.

%install
install -m 644 -D "%{SOURCE0}" \
    '%{buildroot}%{_rpmconfigdir}/macros.d/macros.perl-srpm'

%files
%{_rpmconfigdir}/macros.d/macros.perl-srpm

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-61
- Prepare for Oreon 11 (RP1)
