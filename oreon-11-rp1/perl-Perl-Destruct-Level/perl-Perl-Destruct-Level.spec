%global source0_hash 40b4ac0b292b60ce3b87de7aa39bc2fb25a19d10e5c9f69866961c84b3f6d13b

Name:		perl-Perl-Destruct-Level
Summary:	Allows you to change perl's internal destruction level
Version:	0.02
Release:	45%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Perl-Destruct-Level
Source0:        https://cpan.metacpan.org/modules/by-module/Perl/Perl-Destruct-Level-%{version}.tar.gz



# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module allows you to change perl's internal destruction level. The
default value of the destruct level is 0; it means that perl won't bother
destroying all of its internal data structures and lets the OS do the cleanup
for it at exit.

For perls built with debugging support (-DDEBUGGING), an environment variable
PERL_DESTRUCT_LEVEL allows you to control the destruction level. This module
enables you to modify it on non-debugging perls too.

Note that some embedded environments might extend the meaning of the
destruction level for their own purposes: mod_perl does that, for example.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Perl-Destruct-Level-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%{perl_vendorarch}/auto/Perl/
%{perl_vendorarch}/Perl/
%{_mandir}/man3/Perl::Destruct::Level.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.02-45
- Prepare for Oreon 11 (RP1)
