%global source0_hash a06be7f9ae1b73c9bfd5b6662b141c0d70469e9c19bb4413a6ee56f82adae442

Name:           perl-Regexp-Assemble
Version:        0.38
Release:        25%{?dist}
Summary:        Assemble multiple Regular Expressions into a single RE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Regexp-Assemble
Source0:        https://cpan.metacpan.org/modules/by-module/Regexp/Regexp-Assemble-%{version}.tgz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::Warn)
# Dependencies
Requires:       perl(Carp)
Requires:       perl(Storable)
Requires:       perl(Time::HiRes)

%description
Regexp::Assemble takes an arbitrary number of regular expressions and
assembles them into a single regular expression (or RE) that matches all
that the individual REs match.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Regexp-Assemble-%{version}

# Tidy up the examples (note that eg/file.3 is required to have DOS line endings)
find examples/ -type f | xargs chmod -c -x
find examples/ -type f | xargs perl -pi -e 's|^#!\s*/usr/local/bin/perl\S*|%{__perl}|'

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
%doc Changes examples/ README TODO
%{perl_vendorlib}/Regexp/
%{_mandir}/man3/Regexp::Assemble.3*

%changelog
%autochangelog
