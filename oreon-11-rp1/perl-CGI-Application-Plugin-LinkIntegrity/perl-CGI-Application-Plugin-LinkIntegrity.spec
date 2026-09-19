%global source0_hash 6ba14381085c4217fbd856863749728d8e382c81a64750bb896af89eecaa633b

Name:           perl-CGI-Application-Plugin-LinkIntegrity
Version:        0.06
Release:        44%{?dist}
Summary:        Make tamper-resistant links in CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-LinkIntegrity
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGRAHAM/CGI-Application-Plugin-LinkIntegrity-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Digest::HMAC)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)

%{?perl_default_filter}

%description
CGI::Application::Plugin::LinkIntegrity lets you create tamper-resistant
links within your CGI::Application project. When you create an URL with
link, a check-sum is added to the URL. The check-sum is a (cryptographic) hash
of the URL, plus a secret string known only to the server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-LinkIntegrity-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
