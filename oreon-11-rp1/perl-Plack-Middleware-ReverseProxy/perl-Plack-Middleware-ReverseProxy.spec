%global source0_hash 874931d37d07667ba0d0f37903b94511071f4191feb73fa45765da2b8c15a128
Name:           perl-Plack-Middleware-ReverseProxy
Version:        0.16
Release:        21%{?dist}
Summary:        Supports app to run as a reverse proxy back-end
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack-Middleware-ReverseProxy
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-Middleware-ReverseProxy-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Plack) >= 0.9988
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
