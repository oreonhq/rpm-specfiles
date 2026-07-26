%global source0_hash 6a1ccd4008d4cc66ded4e2a1694b5b2a21d7655e276e1354160012ba2be2a284

Name:		perl-true
Version:	1.0.2
Release:	18%{?dist}
Summary:	Automatically return a true value when a file is required
License:	Artistic-2.0
URL:		https://metacpan.org/release/true
Source0:	http://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/true-v%{version}.tar.gz
# ============= Module Build ====================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::Depends) >= 0.304
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Copy)
# ============= Module Runtime ==================
BuildRequires:	perl(B::Hooks::OP::Annotation) >= 0.44
BuildRequires:	perl(B::Hooks::OP::Check) >= 0.22
BuildRequires:	perl(Devel::StackTrace) >= 2.03
BuildRequires:	perl(strict)
BuildRequires:	perl(version) >= 0.77
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# ============= Test Suite ======================
BuildRequires:	perl(base)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Function::Parameters) >= 2.001003
BuildRequires:	perl(lib)
BuildRequires:	perl(Moo) >= 2.003004
BuildRequires:	perl(Test::More)
# ============= Module Dependencies =============
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
Perl's require built-in (and its use wrapper) requires the files it loads to
return a true value. This is usually accomplished by placing a single

	1;

statement at the end of included scripts or modules. It's not onerous to add
but it's a speed bump on the Perl novice's road to enlightenment. In addition,
it appears to be a non-sequitur to the uninitiated, leading some to attempt to
mitigate its appearance with a comment:

	1; # keep require happy
or:
	1; # Do not remove this line
or even:
	1; # Must end with this, because Perl is bogus.

This module packages this "return true" behavior so that it need not be
written explicitly. It can be used directly, but it is intended to be invoked
from the import method of a Modern::Perl-style module that enables modern Perl
features and conveniences and cleans up legacy Perl warts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n true-v%{version}

%build
perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE.md
%doc Changes README
%{perl_vendorarch}/auto/true/
%{perl_vendorarch}/true.pm
%{perl_vendorarch}/true/
%{_mandir}/man3/true.3*
%{_mandir}/man3/true::VERSION.3*

%changelog
%autochangelog
