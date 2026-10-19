%global source0_hash e2ef1da66427145842c23cc7cf6631dfa2a0ebcaf54debdfa81b72a38ece4a84
Name:           perl-Text-Ngram
Summary:        Ngram analysis of text
Version:        0.15
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Ngram
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/Text/Text-Ngram-%{version}.tar.gz
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Unicode::CaseFold)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
n-Gram analysis is a field in textual analysis which uses sliding window
character sequences in order to aid topic analysis, language determination
and so on. The n-gram spectrum of a document can be used to compare and
filter documents in multiple languages, prepare word prediction networks,
and perform spelling correction.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Ngram-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
