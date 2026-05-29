%global source0_hash 3a8db00f38148f3afadbe5330dc5490d9933f9cae137e842ec225a4d3adb2d9f

Name:           perl-accessors
Version:        1.01
Release:        47%{?dist}
Summary:        Create accessor methods in caller's package
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/accessors
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/accessors-1.01.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.20
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings::register)
# Test Suite
BuildRequires:  perl(Carp)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More) >= 0.01
# Dependencies
# (none)

%description
The accessors pragma lets you create simple accessors at compile-time.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n accessors-%{version}

# A few of the .pm modules have bogus execute permission
find . -name '*.pm' | xargs chmod -c a-x

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README TODO
%{perl_vendorlib}/accessors.pm
%{perl_vendorlib}/accessors/
%{_mandir}/man3/accessors.3*
%{_mandir}/man3/accessors::chained.3*
%{_mandir}/man3/accessors::classic.3*
%{_mandir}/man3/accessors::ro.3*
%{_mandir}/man3/accessors::rw.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.01-47
- Prepare for Oreon 11 (RP1)
