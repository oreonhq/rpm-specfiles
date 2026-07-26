%global source0_hash c2770f028269fcdb65150f2bb313f8a6f6b5def4ee21b5619f5cbfa4031b7c54

Name:           perl-Net-OAuth
Version:        0.31
Release:        3%{?dist}
Summary:        OAuth protocol support library for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-OAuth
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Net-OAuth-%{version}.tar.gz
BuildArch:      noarch

# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor) >= 0.31
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable) >= 0.06
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::URandom) >= 0.37
BuildRequires:  perl(Digest::SHA) >= 5.47
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::UserAgent) >= 1
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Compat)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(strict)
BuildRequires:  perl(URI) >= 5.15
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
Perl implementation of OAuth, an open protocol to allow secure API
authentication in a simple and standard method from desktop and web
applications. In practical terms, a mechanism for a Consumer to request
protected resources from a Service Provider on behalf of a user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-OAuth-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::OAuth*3pm*

%changelog
%autochangelog
