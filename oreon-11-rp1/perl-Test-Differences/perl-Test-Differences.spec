%global source0_hash 648844b9dcb7dae6f9b5a15c9359d0f09de247a624b65c4620ebff249558f913
Name:           perl-Test-Differences
%global cpan_version 0.72
Version:        %(LANG=C printf "%.4f" %{cpan_version})
Release:        1%{?dist}
Summary:        Test strings and data structures and show differences if not OK
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Differences
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Test-Differences-0.72.tar.gz
BuildArch:      noarch
Requires:       perl(B::Deparse)
Requires:       perl(Text::Diff) >= 1.43
Provides:       perl(Test::Differences)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
When the code you're testing returns multiple lines, records or data
structures and they're just plain wrong, an equivalent to the Unix
diff utility may be just what's needed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Differences-%{cpan_version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %(LANG=Cprintf"%.4f"%{cpan_version})-3
- Prepare for Oreon 11 (RP1)
