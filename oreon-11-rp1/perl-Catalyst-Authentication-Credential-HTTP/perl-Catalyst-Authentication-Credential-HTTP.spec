%global source0_hash ec81e96c2a3f6586ea41d088ea8e801b1f34001ab19cc9a65def8a38c39a5bda
Name:           perl-Catalyst-Authentication-Credential-HTTP
Version:        1.019
Release:        1%{?dist}
Summary:        HTTP Basic and Digest authentication for Catalyst
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Authentication-Credential-HTTP
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Catalyst-Authentication-Credential-HTTP-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Catalyst::Plugin::Authentication) >= 0.10005
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Crypt::SysRandom) >= 0.007
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Cache)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Crypt::SysRandom)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(String::Escape)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::MockObject::Extends)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
