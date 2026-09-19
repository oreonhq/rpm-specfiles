%global source0_hash c0480b5f1f15b71163ec327b8e7842298f0cb3ace97e63d7034af1e94a2d90f4

Name:           perl-WWW-Form-UrlEncoded
Version:        0.26
Release:        20%{?dist}
Summary:        Parser and builder for application/x-www-form-urlencoded
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Form-UrlEncoded
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/WWW-Form-UrlEncoded-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 0:5.008001

BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP) >= 2
BuildRequires:  perl(Module::Build) > 0.4005
BuildRequires:  perl(Test::More) >= 0.98

BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

# N/A in Fedora
# Suggests: perl(WWW::Form::UrlEncoded::XS)

%description
WWW::Form::UrlEncoded provides application/x-www-form-urlencoded parser and
builder. This module aims to have compatibility with other CPAN modules
like HTTP::Body's urlencoded parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Form-UrlEncoded-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
BREAK_BACKWARD_COMPAT=1 ./Build

%install
BREAK_BACKWARD_COMPAT=1 ./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
BREAK_BACKWARD_COMPAT=1 ./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
