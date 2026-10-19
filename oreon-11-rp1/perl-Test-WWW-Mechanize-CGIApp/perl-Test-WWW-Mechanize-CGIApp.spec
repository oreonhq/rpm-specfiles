%global source0_hash 07149ca962d9eb922dfd0615b0402502b4b6092242ba345fe3ccbb35f882c5d4
Name:           perl-Test-WWW-Mechanize-CGIApp
Version:        0.05
Release:        1%{?dist}
Summary:        Test::WWW::Mechanize for CGI::Application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-WWW-Mechanize-CGIApp
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HARTZELL/Test-WWW-Mechanize-CGIApp-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Test::More)
Requires:       perl(Test::WWW::Mechanize)
Requires:       perl(CGI::Application)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::WWW::Mechanize)
BuildRequires:  perl-generators
# /oreon:deps
%description
This package makes testing CGIApp based modules fast and easy. It takes
advantage of Test::WWW::Mechanize to provide functions for common web
testing scenarios.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-WWW-Mechanize-CGIApp-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
