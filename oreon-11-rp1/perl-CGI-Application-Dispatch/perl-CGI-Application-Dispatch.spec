%global source0_hash 5dad58e4fa6d79f1d48120800872b22ffdbb9b165911a973642038db88078d0f

Name:           perl-CGI-Application-Dispatch
Version:        3.12
Release:        38%{?dist}
Summary:        Dispatch requests to CGI::Application based objects
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Dispatch
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/CGI-Application-Dispatch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application) >= 4.50
BuildRequires:  perl(CGI::PSGI)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exception::Class::TryCatch)
BuildRequires:  perl(HTTP::Exception)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More)
# Apache::Test must be configured before use.
# BuildRequires:  perl(Apache::Test)

%{?perl_default_filter}

%description
This module provides a way (as a mod_perl handler or running under vanilla
CGI) to look at the path (as returned by dispatch_path) of the incoming
request, parse off the desired module and it's run mode, create an instance
of that module and run it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Dispatch-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
