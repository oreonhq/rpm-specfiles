%global source0_hash 29a1926314ce1681a312d6155c29590c771ddacf91b7485873ce449ef209dd04

Summary:	Simple date object for perl
Name:		perl-Date-Simple
Version:	3.03
Release:	54%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Date-Simple
Source0:	https://cpan.metacpan.org/authors/id/I/IZ/IZUT/Date-Simple-%{version}.tar.gz
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(overload)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings::register)
# Test Suite
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)
# Dependencies
Requires:	perl(DynaLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

Provides:       perl(Date::Simple)
Provides:       perl(Date::Simple)
%description
Simple date object for perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Date-Simple-%{version}

# Spurious exec permissions in files from tarball
find lib -type f -exec chmod -c -x {} ';'
chmod -c -x ChangeLog COPYING README Simple.xs

# The NoXS.pm file provides a pure-perl alternative to the C implementation
# of the module. This results in duplicate "Provides:" entries, which rpmlint
# whinges about. This kludge removes the redundant file, which has the added
# benefit of shutting up rpmlint.
rm -f lib/Date/Simple/NoXS.pm
sed -i -e '/^lib\/Date\/Simple\/NoXS\.pm$/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -a -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc ChangeLog README
%{perl_vendorarch}/Date/
%{perl_vendorarch}/auto/Date/
%{_mandir}/man3/Date::Simple.3*
%{_mandir}/man3/Date::Simple::D8.3*
%{_mandir}/man3/Date::Simple::Fmt.3*
%{_mandir}/man3/Date::Simple::ISO.3*

%changelog
%autochangelog
