%global source0_hash 874931d37d07667ba0d0f37903b94511071f4191feb73fa45765da2b8c15a128

Name:           perl-Plack-Middleware-ReverseProxy
Version:        0.16
Release:        21%{?dist}
Summary:        Supports app to run as a reverse proxy back-end
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack-Middleware-ReverseProxy
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-Middleware-ReverseProxy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
# Plack::Middleware is not version, depend on Plack
BuildRequires:  perl(Plack) >= 0.9988
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(lib)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
#Requires:       perl(Plack::Middleware)
# Plack::Middleware is not version, depend on Plack
Requires:       perl(Plack) >= 0.9988

%{?perl_default_filter}

%description
Plack::Middleware::ReverseProxy resets some HTTP headers, which changed by
reverse-proxy. You can specify the reverse proxy address and stop fake
requests using 'enable_if' directive in your app.psgi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-Middleware-ReverseProxy-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Plack*
%{_mandir}/man3/Plack*

%changelog
%autochangelog
