
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
Name:       perl-srpm-macros    
Version:        1
Release:        1%{?dist}
Summary:    RPM macros for building Perl source package from source repository
License:    GPL-3.0-or-later
Source0:    macros.perl-srpm
BuildArch:  noarch

%description
These RPM macros are used for building Perl source packages from source
repositories. They influence build-requires set into the source package.

%prep
%oreon_sha256

%install
install -m 644 -D "%{SOURCE0}" \
    '%{buildroot}%{_rpmconfigdir}/macros.d/macros.perl-srpm'

%files
%{_rpmconfigdir}/macros.d/macros.perl-srpm

