%global source0_hash 7ec4f52cadca7dc9ca7722e20afeabf0210886fa2db5cc0179ec1c7d65a750a0

Name:           perl-MooseX-Param
Version:        0.02
Release:        48%{?dist}
Summary:        Simple role to provide a standard param method
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-Param
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEVAN/MooseX-Param-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose) >= 0.32
BuildRequires:  perl(Test::Exception) >= 0.21
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Moose) >= 0.32

%description
This is a very simple Moose role which provides a CGI like param method.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Param-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc ChangeLog README
%{perl_vendorlib}/Moose*
%{_mandir}/man3/Moose*

%changelog
%autochangelog
