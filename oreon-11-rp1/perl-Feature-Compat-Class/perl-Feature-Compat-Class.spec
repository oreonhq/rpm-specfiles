%global source0_hash 0ddf9a82841f10e35f107cdf627b160755f9de93d8b7ea2a090183fdc268c70b

Name:           perl-Feature-Compat-Class
Version:        0.08
Release:        2%{?dist}
Summary:        Make class syntax available
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Feature-Compat-Class
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Feature-Compat-Class-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Object::Pad)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

Requires:       perl(Object::Pad)

%description
This module provides the new class keyword and related others (method, field
and ADJUST) in a forward-compatible way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Feature-Compat-Class-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%dir %{perl_vendorlib}/Feature/
%dir %{perl_vendorlib}/Feature/Compat
%{perl_vendorlib}/Feature/Compat/Class.pm
%{_mandir}/man3/Feature::Compat::Class.*

%changelog
%autochangelog
