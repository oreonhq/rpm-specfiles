%global source0_hash ad42e9137f5148df7fdb22aa52186b306032977bcd70d49f44a288070e4f0f23

Name:           perl-JSON-Tiny
Version:        0.58
Release:        26%{?dist}
Summary:        Minimalistic JSON. No dependencies
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0

URL:            https://metacpan.org/release/JSON-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/JSON-Tiny-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

 
%{?perl_default_filter}

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

%check
RELEASE_TESTING=1 make test

%files
%license LICENSE
%doc Changes README examples
%{perl_vendorlib}/JSON*
%{_mandir}/man3/JSON*

%changelog
%autochangelog
