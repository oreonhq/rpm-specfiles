Name:           perl-Role-Tiny
Version:        2.002004
Release:        15%{?dist}
Summary:        A nouvelle cuisine portion size slice of Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Role-Tiny
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 d7bdee9e138a4f83aa52d0a981625644bda87ff16642dfa845dcb44d9a242b45
%global source0_file Role-Tiny-2.002004.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Method::Modifiers) >= 1.05
BuildRequires:  perl(Exporter)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
Requires:       perl(Carp)
Requires:       perl(Class::Method::Modifiers) >= 1.05
Requires:       perl(mro)

%description
Role::Tiny is a minimalist role composition tool.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Role-Tiny-2.002004.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d7bdee9e138a4f83aa52d0a981625644bda87ff16642dfa845dcb44d9a242b45" || { echo "oreon: Source0 SHA256 mismatch for Role-Tiny-2.002004.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Role-Tiny-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Role/
%{_mandir}/man3/Role::Tiny.3*
%{_mandir}/man3/Role::Tiny::With.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.002004-15
- Prepare for Oreon 11 (RP1)
