%global source0_hash 107522b6133255f7bb8b5f61d902dc26800196c2390111b1aff2cde12dffefb8

Name:           perl-MooseX-Types-Set-Object
Version:        0.05
Release:        30%{?dist}
Summary:        Set::Object type with coercions and stuff
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-Types-Set-Object
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-Set-Object-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose) >= 0.50
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(Set::Object)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::use::ok)

%{?perl_default_filter}

%description
This module provides Moose type constraints (see
Moose::Util::TypeConstraints, MooseX::Types).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-Set-Object-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc README
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
%autochangelog
