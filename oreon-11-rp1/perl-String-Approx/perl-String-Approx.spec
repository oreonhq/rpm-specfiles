%global source0_hash 43201e762d8699cb0ac2c0764a5454bdc2306c0771014d6c8fba821480631342

Name:           perl-String-Approx
Version:        3.28
Release:        32%{?dist}
Summary:        Perl extension for approximate (fuzzy) matching
# Fedora legal
# <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/172>
# recommends ignoring COPYRIGHT.agrep because there is no agrep source code
# and Artistic-1.0-Perl option because Fedora does not allow it.
# Approx.pm:    Artistic-2.0 OR LGPL-2.0-only
# apse.c:       LGPL-2.0-or-later OR Artistic-1.0-Perl
# apse.h:       LGPL-2.0-or-later OR Artistic-1.0-Perl
# Artistic:     Artistic-2.0 text
# COPYRIGHT:    LGPL-1.0-or-later (!) OR Artistic-1.0-Perl
# COPYRIGHT.agrep:  agrep license text
#               <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/172>
# LGPL:         LGPL-2.0 text
# README:       Artistic-2.0 OR LGPL-2.0-only
# README.apse:  "read the COPYRIGHT. This implementation shares no code with agrep"
License:        (Artistic-2.0 OR LGPL-2.0-only) AND (LGPL-2.0-or-later)
URL:            https://metacpan.org/release/String-Approx
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHI/String-Approx-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)

%description
String::Approx lets you match and substitute strings approximately. With
this you can emulate errors: typing errors, speling errors, closely
related vocabularies (colour vs. color), genetic mutations (GAG vs. ACT),
abbreviations (McScot, MacScot).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Approx-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license Artistic COPYRIGHT LGPL
%doc ChangeLog PROBLEMS README README.apse
%dir %{perl_vendorarch}/auto/String
%{perl_vendorarch}/auto/String/Approx
%dir %{perl_vendorarch}/String
%{perl_vendorarch}/String/Approx.pm
%{_mandir}/man3/String::Approx.*

%changelog
%autochangelog
