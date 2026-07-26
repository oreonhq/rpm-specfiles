%global source0_hash 433e821ac44ab6164c7e92b60ff7afa60a279bc550134c82ceb70b3ef4ee2925

Name:           perl-Number-Range
Version:        0.12
Release:        28%{?dist}
Summary:        Extension to work with ranges of numbers
# "This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself."
# Query about separate license file: https://rt.cpan.org/Public/Bug/Display.html?id=117694
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Number-Range
Source0:        https://cpan.metacpan.org/authors/id/L/LA/LARRYSH/Number-Range-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  sed
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)

%description
Number::Range will take a description of a range, and then allow you to test on
if a number falls within the range. You can also add and delete from the range.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Number-Range-%{version}

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/Number::Range.3pm*

%changelog
%autochangelog
