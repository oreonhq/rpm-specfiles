%global source0_hash ece981f4161635a2fba6215d0257195e538c4f234384530501dfdb6a1bd8d636
%bcond_without perl_HTTP_Body_enables_optional_test
%bcond_with perl_HTTP_Body_enables_plack_test
Name:           perl-HTTP-Body
Summary:        HTTP Body Parser
Version:        1.23
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GETTY/HTTP-Body-%{version}.tar.gz
URL:            https://metacpan.org/dist/HTTP-Body
BuildArch:      noarch
%if %{with perl_HTTP_Body_enables_optional_test}
%if %{with perl_HTTP_Body_enables_plack_test}
%endif
%endif
Requires:       perl(IO::File) >= 1.14
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IO::File\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A perl module for parsing the MultiPart, OctetStream, and UrlEncoded 
parts of an HTTP Body.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Body-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%if %{with perl_HTTP_Body_enables_optional_test}
export TEST_POD=1
%endif
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
