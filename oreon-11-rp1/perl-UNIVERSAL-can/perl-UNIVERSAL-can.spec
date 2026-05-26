Name:           perl-UNIVERSAL-can
Version:        1.20140328
Release:        32%{?dist}
Summary:        Hack around people calling UNIVERSAL::can() as a function
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/UNIVERSAL-can
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/UNIVERSAL-can-1.20140328.tar.gz
# oreon url source checksums begin
%global source0_sha256 522da9f274786fe2cba99bc77cc1c81d2161947903d7fad10bd62dfb7f11990f
%global source0_file UNIVERSAL-can-1.20140328.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Module:
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
# Test Suite:
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
# Dependencies:

%description
The UNIVERSAL class provides a few default methods so that all objects
can use them. Object orientation allows programmers to override these
methods in subclasses to provide more specific and appropriate behavior.

Some authors call methods in the UNIVERSAL class on potential invocants
as functions, bypassing any possible overriding. This is wrong and you
should not do it. Unfortunately, not everyone heeds this warning and
their bad code can break your good code.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/UNIVERSAL-can-1.20140328.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "522da9f274786fe2cba99bc77cc1c81d2161947903d7fad10bd62dfb7f11990f" || { echo "oreon: Source0 SHA256 mismatch for UNIVERSAL-can-1.20140328.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n UNIVERSAL-can-%{version}

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
%license LICENSE
%doc Changes README
%{perl_vendorlib}/UNIVERSAL/
%{_mandir}/man3/UNIVERSAL::can.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20140328-32
- Prepare for Oreon 11 (RP1)
