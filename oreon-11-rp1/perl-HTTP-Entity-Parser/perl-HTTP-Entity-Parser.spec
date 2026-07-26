%global source0_hash 3a8cd0d8cba3d17cd8c04ee82d7341dfaa247dbdd94a49eb94b53f69e483ec3a

Name:           perl-HTTP-Entity-Parser
Version:        0.25
Release:        16%{?dist}
Summary:        PSGI compliant HTTP Entity Parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Entity-Parser
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/HTTP-Entity-Parser-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__perl}

BuildRequires:  perl-interpreter >= 0:5.008001
BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Message) >= 6
BuildRequires:  perl(HTTP::MultiPartParser)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003007
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Stream::Buffered)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(WWW::Form::UrlEncoded) >= 0.23

BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
HTTP::Entity::Parser is a PSGI-compliant HTTP Entity parser. This module
also is compatible with HTTP::Body. Unlike HTTP::Body, HTTP::Entity::Parser
reads HTTP entities from PSGI's environment $env->{'psgi.input'} and parses
it. This module supports application/x-www-form-urlencoded, multipart/form-
data and application/json.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Entity-Parser-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md eg/
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
