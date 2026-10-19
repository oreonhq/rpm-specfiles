%global source0_hash e7950246433f7ed6c3e4fd4df2227e0f2341137c3cab1989018fc370f58145c4
Name:           perl-Email-MIME-ContentType
Version:        1.028
Release:        1%{?dist}
Summary:        Parse a MIME Content-Type Header
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MIME-ContentType
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MIME-ContentType-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is responsible for parsing email content type headers according
to section 5.1 of RFC 2045. It returns a hash with entries for the type, the
subtype, and a hash of attributes.

For backward compatibility with a really unfortunate misunderstanding of RFC
2045 by the early implementors of this module, 'discrete' and 'composite' are
also present in the returned hashref, with the values of 'type' and 'subtype'
respectively.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-MIME-ContentType-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
