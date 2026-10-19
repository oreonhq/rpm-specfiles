%global source0_hash 97f84daf033eb9b49cd8fe31db221fef035a5c2ee1d757f3122c88cf9762414c
Summary:        Checks if scalar is valid UTF-8
Name:		perl-Unicode-CheckUTF8
Version:	1.03
Release:        1%{?dist}
License:	Unicode-3.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:		https://metacpan.org/release/Unicode-CheckUTF8
Source0:        https://cpan.metacpan.org/modules/by-module/Unicode/Unicode-CheckUTF8-%{version}.tar.gz
%{?perl_default_filter}
Provides:       perl(Unicode::CheckUTF8)
Provides:       perl(Unicode::CheckUTF8)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is an XS wrapper around some Unicode Consortium code to check if a string
is valid UTF-8, revised to conform to what expat/Mozilla think is valid UTF-8,
especially with regard to low-ASCII characters.

Note that this module has NOTHING to do with Perl's internal UTF8 flag on
scalars.

This module is for use when you're getting input from users and want to make
sure it's valid UTF-8 before continuing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Unicode-CheckUTF8-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
