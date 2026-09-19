%global source0_hash 92a5831658810d23732e6e3bae7a44a1fa5a7d8a6a6e6dcd75b91c6a9c24b466

Name:           perl-Plack-Middleware-Session
Version:        0.36
Release:        2%{?dist}
Summary:        Middleware for session management
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            http://metacpan.org/release/Plack-Middleware-Session
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-Middleware-Session-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# build deps
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# runtime deps
BuildRequires:  perl(Cookie::Baker)
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(parent)
# test deps
BuildRequires:  perl(Crypt::SysRandom)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(YAML)

%{?perl_default_filter}

%description
This is a Plack Middleware component for session management. By default it
will use cookies to keep session state and store data in memory. This
distribution also comes with other state and store solutions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-Middleware-Session-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 PERL5LIB="." ./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Plack*
%{_mandir}/man3/Plack*

%changelog
%autochangelog
