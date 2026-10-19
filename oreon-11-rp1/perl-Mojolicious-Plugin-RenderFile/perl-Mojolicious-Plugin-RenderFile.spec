%global source0_hash 013e42a2cc06bc7041bb13c9df388af24010e69793a8df0f0ab1d240aa61173f
Name:           perl-Mojolicious-Plugin-RenderFile
Version:        0.12
Release:        1%{?dist}
Summary:        Mojolicious plugin allowing customization to force file download
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mojolicious-Plugin-RenderFile
Source0:        https://cpan.metacpan.org/authors/id/K/KO/KOORCHIK/Mojolicious-Plugin-RenderFile-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Mojolicious::Plugin::RenderFile is a Mojolicious plugin that makes it
easy to provide files for download. It also allows customization of
the HTTP headers sent to the client.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojolicious-Plugin-RenderFile-%{version}
# This test only works properly with Mojo 5.78+:
# https://github.com/koorchik/Mojolicious-Plugin-RenderFile/commit/0dfa997

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
