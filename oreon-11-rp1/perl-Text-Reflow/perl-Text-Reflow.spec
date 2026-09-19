%global source0_hash 4bf2139ff617d6e59cc0e59cdecd7cb723ecfd28d5ac387afb553ffdc071b860

Name:           perl-Text-Reflow
Version:        1.17
Release:        32%{?dist}
Summary:        Perl module for reflowing text files using Knuth's paragraphing algorithm
License:        GPL-3.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Text-Reflow
Source0:        https://cpan.metacpan.org/authors/id/M/MW/MWARD/Text-Reflow-%{version}.tar.gz
# Build
BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::Simple)

%description
These routines will reflow the paragraphs in the given file, filehandle,
string or array using Knuth's paragraphing algorithm (as used in TeX) to
pick "good" places to break the lines.

%package -n reflow
Summary:        A utility for reflowing text files using Knuth's paragraphing algorithm
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
BuildArch:      noarch

%description -n reflow
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Reflow-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text
%{_mandir}/man3/*

%files -n reflow
%{_bindir}/reflow
%{_mandir}/man1/reflow*

%changelog
%autochangelog
