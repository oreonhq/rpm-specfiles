%global source0_hash c53fce1e43c393b643425d857cd327a02612e645412dfbb774304053ea5e1d4b
%global debug_package %{nil}

Name: perl-srpm-macros
Version: 1
Release: 1%{?dist}
Summary: SRPM macros for Perl packages
License: GPL-3.0-or-later
URL: https://www.perl.org/
BuildArch: noarch
Source0: macros.perl-srpm

BuildRequires: oreon-rpm-macros

%description
SRPM macros that set the build requires of Perl source packages.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.perl-srpm

%files
%{_rpmmacrodir}/macros.perl-srpm
