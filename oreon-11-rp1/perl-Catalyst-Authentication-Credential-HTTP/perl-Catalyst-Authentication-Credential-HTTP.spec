%global source0_hash ec81e96c2a3f6586ea41d088ea8e801b1f34001ab19cc9a65def8a38c39a5bda

Name:           perl-Catalyst-Authentication-Credential-HTTP
Version:        1.019
Release:        2%{?dist}
Summary:        HTTP Basic and Digest authentication for Catalyst
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Authentication-Credential-HTTP
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Catalyst-Authentication-Credential-HTTP-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny)
# runtime requirements
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Crypt::SysRandom) >= 0.007
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(String::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# testing requirements
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Plugin::Authentication) >= 0.10005
BuildRequires:  perl(Catalyst::Plugin::Cache)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::MockObject::Extends)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(lib)
BuildRequires:  sed
Requires:       perl(Catalyst::Plugin::Authentication) >= 0.10005
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Crypt::SysRandom) >= 0.007

%{?perl_default_filter}

%description
This module lets you use HTTP authentication with
Catalyst::Plugin::Authentication. Both basic and digest authentication are
currently supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Authentication-Credential-HTTP-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes CONTRIBUTING README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
