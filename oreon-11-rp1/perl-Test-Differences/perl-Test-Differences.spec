%global source0_hash 648844b9dcb7dae6f9b5a15c9359d0f09de247a624b65c4620ebff249558f913

# TODO: BR: optional test dependency Unknown::Values if it becomes available

Name:           perl-Test-Differences
%global cpan_version 0.72
Version:        %(LANG=C printf "%.4f" %{cpan_version})
Release:        3%{?dist}
Summary:        Test strings and data structures and show differences if not OK
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Differences
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Test-Differences-0.72.tar.gz

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper) >= 2.126
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Diff) >= 1.43
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Capture::Tiny) >= 0.24
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Explicit Dependencies
Requires:       perl(B::Deparse)
Requires:       perl(Text::Diff) >= 1.43

%description
When the code you're testing returns multiple lines, records or data
structures and they're just plain wrong, an equivalent to the Unix
diff utility may be just what's needed.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Test-Differences-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Differences.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %(LANG=Cprintf"%.4f"%{cpan_version})-3
- Prepare for Oreon 11 (RP1)
