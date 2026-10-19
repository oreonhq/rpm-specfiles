%global source0_hash 13f5237f3ade2c4ce80c5b8dd447e5792aca17e31746c79c166f7cdc93f2336b
Name:           perl-Plack-Middleware-ForceEnv
Version:        0.02
Release:        40%{?dist}
Summary:        Force set environment variables for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack-Middleware-ForceEnv
Source0:        https://cpan.metacpan.org/authors/id/T/TS/TSIBLEY/Plack-Middleware-ForceEnv-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Plack) >= 0.9925
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl-generators
# /oreon:deps
%description
ForceEnv modifies the environment passed to the application by adding your
specified key value pairs. This is primarily useful when testing apps under
plackup (or similar) in a development environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-Middleware-ForceEnv-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
