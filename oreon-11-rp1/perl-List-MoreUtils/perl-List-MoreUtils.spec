# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 63b1f7842cd42d9b538d1e34e0330de5ff1559e4c2737342506418276f646527
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:		perl-List-MoreUtils
Version:	0.430
Release:	15%{?dist}
Summary:	Provide the stuff missing in List::Util
# All code present in version 0.416: GPL-1.0-or-later OR Artistic-1.0-Perl
# All new code from version 0.417 onwards: Apache-2.0
License:	(GPL-1.0-or-later OR Artistic-1.0-Perl) AND Apache-2.0
URL:		https://metacpan.org/release/List-MoreUtils
Source0:	https://cpan.metacpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-0.430.tar.gz

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.75
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(lib)
BuildRequires:	perl(PerlIO)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Text::ParseWords)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter::Tiny) >= 0.038
BuildRequires:	perl(List::MoreUtils::XS) >= 0.430
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Exporter)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Math::Trig)
BuildRequires:	perl(overload)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Tie::Array)
# Optional Tests
%if ! ( 0%{?rhel} )
BuildRequires:	perl(Test::LeakTrace)
%endif
# Dependencies
Requires:	perl(Carp)
Requires:	perl(List::MoreUtils::XS) >= 0.430

%description
List::MoreUtils provides some trivial but commonly needed functionality
on lists that is not going to go into List::Util.

%prep
%oreon_verify_sources
%setup -q -n List-MoreUtils-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes README.md
%{perl_vendorlib}/List/
%{_mandir}/man3/List::MoreUtils.3*
%{_mandir}/man3/List::MoreUtils::Contributing.3*
%{_mandir}/man3/List::MoreUtils::PP.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.430-15
- Prepare for Oreon 11 (RP1)
