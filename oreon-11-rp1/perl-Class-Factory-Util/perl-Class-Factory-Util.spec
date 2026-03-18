Name:           perl-Class-Factory-Util
Version:        1.7
Release:        50%{?dist}
Summary:        Provide utility methods for factory classes 
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Factory-Util            
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Factory-Util-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat) >= 0.02
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
# Dependencies
# (none)

%description
This module exports utility functions that are useful for factory classes.

%prep
%setup -q -n Class-Factory-Util-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Factory::Util.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7-50
- Prepare for Oreon 11 (RP1)
