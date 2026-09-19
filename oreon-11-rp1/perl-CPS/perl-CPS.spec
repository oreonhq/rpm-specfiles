%global source0_hash b52fccf7a40607d0cfdfbc5de75973febb06ea65eef5380b391c87a5a472675b

Name:           perl-CPS
Version:        0.19
Release:        20%{?dist}
Summary:        CPS Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPS
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/CPS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Refcount)
BuildRequires:  perl(warnings)

%description
The functions in this module implement or assist the writing of
programs, or parts of them, in Continuation Passing Style (CPS).
Briefly, CPS is a style of writing code where the normal call/return
mechanism is replaced by explicit "continuations", values passed in to
functions which they should invoke, to implement return behavior. For
more detail on CPS, see the SEE ALSO section.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPS-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
