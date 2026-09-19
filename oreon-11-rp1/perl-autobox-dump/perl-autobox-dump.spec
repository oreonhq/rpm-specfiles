%global source0_hash b394b14c1fcbfbbbf040621d95bfd20b27379568a73767bdb0f9c85a298e36eb

Name:           perl-autobox-dump
Version:        20090426.1746
Release:        40%{?dist}
Summary:        Human/perl readable strings from the results of an EXPR
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/autobox-dump
Source0:        https://cpan.metacpan.org/modules/by-module/autobox/autobox-dump-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(autobox)
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Data::Dumper)

%description
The autobox::dump pragma adds, via the autobox pragma, a method to normal
expression (such as scalars, arrays, hashes, math, literals, etc.) that
produces a human/perl readable representation of the value of that expression.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n autobox-dump-%{version}

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
%doc Changes README
%{perl_vendorlib}/autobox/
%{_mandir}/man3/autobox::dump.3*

%changelog
%autochangelog
