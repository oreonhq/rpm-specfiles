%global source0_hash 10167b8e238a682004ab0d7accbe9d76eae2db57af07c5ae2dfa808074a4a8aa

Name:           perl-HTTP-Response-Encoding
Version:        0.06
Release:        47%{?dist}
Summary:        HTTP::Response::Encoding Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Response-Encoding
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/HTTP-Response-Encoding-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::More)

# For improved tests
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14

%description
Adds encoding() to HTTP::Response.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Response-Encoding-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
