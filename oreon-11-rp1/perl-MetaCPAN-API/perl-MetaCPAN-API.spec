%global source0_hash 4f55b9a6bd6e9c044f105f82420cc9596e29ca42060c42756e89b427329ce29a

Name:           perl-MetaCPAN-API
Version:        0.51
Release:        25%{?dist}
Summary:        A comprehensive, DWIM-featured API to MetaCPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MetaCPAN-API
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/MetaCPAN-API-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Tiny) >= 0.014
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(JSON::MaybeXS) >= 1.001000
BuildRequires:  perl(Moo) >= 1.000001
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(warnings)
# Test suite
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Test::TinyMocker)
# Dependencies
Requires:       perl(IO::Socket::SSL)

%description
This is a hopefully-complete API-compliant interface to MetaCPAN
(https://metacpan.org/) with DWIM capabilities, to make your life easier.

However, it has been completely rewritten to address a multitude of problems,
and is now available under the new official name: MetaCPAN::Client.

Please do not use this module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MetaCPAN-API-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/MetaCPAN/
%{_mandir}/man3/MetaCPAN::API.3*
%{_mandir}/man3/MetaCPAN::API::Author.3*
%{_mandir}/man3/MetaCPAN::API::Autocomplete.3*
%{_mandir}/man3/MetaCPAN::API::Distribution.3*
%{_mandir}/man3/MetaCPAN::API::Favorite.3*
%{_mandir}/man3/MetaCPAN::API::File.3*
%{_mandir}/man3/MetaCPAN::API::Module.3*
%{_mandir}/man3/MetaCPAN::API::Rating.3*
%{_mandir}/man3/MetaCPAN::API::POD.3*
%{_mandir}/man3/MetaCPAN::API::Release.3*
%{_mandir}/man3/MetaCPAN::API::Source.3*

%changelog
%autochangelog
