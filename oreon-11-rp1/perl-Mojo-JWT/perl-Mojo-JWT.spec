%global source0_hash fa9cbc47ce494f01a042e0f39e873f8fa5ca5e91472b5ecc4fbb263cc3bd260c

Name:           perl-Mojo-JWT
Version:        1.01
Release:        4%{?dist}
Summary:        JSON Web Token the Mojo way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Mojo-JWT
Source0:        https://cpan.metacpan.org/authors/id/J/JB/JBERGER/Mojo-JWT-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny)
# runtime requirements
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::Mac::HMAC)
BuildRequires:  perl(Crypt::Misc)
BuildRequires:  perl(Crypt::PK::RSA)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::Base) >= 5.00
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Scalar::Util)
# test requirements
BuildRequires:  perl(Crypt::OpenSSL::RSA)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Crypt::OpenSSL::RSA)
Requires:       perl(Digest::SHA)

%description
JSON Web Token is described in https://tools.ietf.org/html/rfc7519.
Mojo::JWT implements that standard with an API that should feel familiar to
Mojolicious users (though of course it is useful elsewhere). Indeed, JWT is
much like Mojolicious::Sessions except that the result is a URL-safe text
string rather than a cookie.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojo-JWT-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
%autochangelog
