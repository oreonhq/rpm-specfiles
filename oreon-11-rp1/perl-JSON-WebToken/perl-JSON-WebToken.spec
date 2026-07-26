%global source0_hash 77c182a98528f1714d82afc548d5b3b4dc93e67069128bb9b9413f24cf07248b

Name:           perl-JSON-WebToken
Version:        0.10
Release:        29%{?dist}
Summary:        JSON Web Token (JWT) implementation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-WebToken
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAICRON/JSON-WebToken-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Mock::Guard) >= 0.07
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Requires) >= 0.06
BuildRequires:  perl-generators
Requires:       perl(Carp)
Requires:       perl(Digest::SHA)
Requires:       perl(Exporter)
Requires:       perl(JSON)
Requires:       perl(MIME::Base64)
Requires:       perl(Module::Runtime)
Requires:       perl(parent)

%description
JSON::WebToken is JSON Web Token (JWT) implementation for Perl

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-WebToken-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes cpanfile META.json minil.toml README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
