# Run optional tests
%if ! (0%{?rhel})
%{bcond_without perl_strictures_enables_optional_test}
%else
%{bcond_with perl_strictures_enables_optional_test}
%endif

Name:           perl-strictures
Version:        2.000006
Release:        23%{?dist}
Summary:        Turn on strict and make most warnings fatal
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/strictures
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/strictures-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 09d57974a6d1b2380c802870fed471108f51170da81458e2751859f2714f8d57
%global source0_file strictures-2.000006.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Text::ParseWords)
# Dependencies of bundled ExtUtils::HasCompiler
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_strictures_enables_optional_test}
# Optional Tests
BuildRequires:  perl(indirect)
BuildRequires:  perl(multidimensional)
BuildRequires:  perl(bareword::filehandles)
%endif
# Runtime
Requires:       perl(Carp)

%description
This package turns on strict and makes most warnings fatal.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/strictures-2.000006.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "09d57974a6d1b2380c802870fed471108f51170da81458e2751859f2714f8d57" || { echo "oreon: Source0 SHA256 mismatch for strictures-2.000006.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n strictures-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/strictures.pm
%{perl_vendorlib}/strictures/
%{_mandir}/man3/strictures.3*
%{_mandir}/man3/strictures::extra.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.000006-23
- Prepare for Oreon 11 (RP1)
