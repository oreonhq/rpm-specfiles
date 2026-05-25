Name:           perl-DateTime-Format-IBeat
Version:        0.161
Release:        53%{?dist}
Summary:        Format times in .beat notation 
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-IBeat            
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-IBeat-%{version}.tar.gz
BuildArch:      noarch 
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime) >= 0.18
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.47
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
# Dependencies
# (none)

%description
No Time Zones, No Geographical Borders 

How long is a Swatch .beat? In short, we have divided up the virtual and real 
day into 1000 beats. One Swatch beat is the equivalent of 1 minute 26.4 
seconds. That means that 12 noon in the old time system is the equivalent of 
500 Swatch .beats.

%prep
%setup -q -n DateTime-Format-IBeat-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license Artistic COPYING LICENCE
%doc Changes README
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Format::IBeat.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.161-53
- Import
