%global source0_hash ad42e9137f5148df7fdb22aa52186b306032977bcd70d49f44a288070e4f0f23
Name:           perl-JSON-Tiny
Version:        0.58
Release:        1%{?dist}
Summary:        Minimalistic JSON. No dependencies
License:        Apache-2.0
URL:            https://metacpan.org/release/JSON-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/JSON-Tiny-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
JSON::Tiny is a minimalistic standalone adaptation of Mojo::JSON, from the
Mojolicious framework. It is a single-source-file module with 350 lines of
code and core-only dependencies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-Tiny-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

RELEASE_TESTING=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
