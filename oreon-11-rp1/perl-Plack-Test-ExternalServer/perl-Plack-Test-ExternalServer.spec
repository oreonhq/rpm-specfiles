%global source0_hash 5baf5c57fe0c06412deec9c5abe7952ab8a04f8c47b4bbd8e9e9982268903ed0
Name:           perl-Plack-Test-ExternalServer
Version:        0.02
Release:        1%{?dist}
Summary:        Run HTTP tests on external live servers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack-Test-ExternalServer
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Plack-Test-ExternalServer-%{version}.tar.gz
BuildArch:      noarch
%if !0%{?perl_bootstrap}
%endif
Requires:       perl(Plack::Test)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(URI)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module allows you to run your Plack::Test tests against an external
server instead of just against a local application through either mocked
HTTP or a locally spawned server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-Test-ExternalServer-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

RELEASE_TESTING=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
