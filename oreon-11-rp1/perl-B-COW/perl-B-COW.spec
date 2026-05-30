%global source0_hash 1290daf227e8b09889a31cf182e29106f1cf9f1a4e9bf7752f9de92ed1158b44

Name:		perl-B-COW
Version:	0.007
Release:	12%{?dist}
Summary:	Additional B helpers to check Copy On Write status
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/B-COW
Source0:        https://cpan.metacpan.org/modules/by-module/B/B-COW-%{version}.tar.gz

# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(Devel::Peek)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Dependencies
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
B::COW provides some naïve additional B helpers to check the Copy On Write
(COW) status of one SvPV (a Perl string variable).

A COWed SvPV is sharing its string (the PV) with other SvPVs. It's a (kind of)
Read Only C string, which would be Copied On Write (COW). More than one SV can
share the same PV, but when one PV needs to alter it, it would perform a copy
of it, decreasing the COWREFCNT counter. One SV can then drop the COW flag when
it's the only one holding a pointer to the PV. The COWREFCNT is stored at the
end of the PV, after the null byte terminating the string. That value is
limited to 255: when we reach 255, a new PV would be created.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n B-COW-%{version}

%build
perl Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{optflags}" \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes examples/ README
%{perl_vendorarch}/auto/B/
%{perl_vendorarch}/B/
%{_mandir}/man3/B::COW.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.007-12
- Import
