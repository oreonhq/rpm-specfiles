%global source0_hash 5837d03711a7a3254f0afecb7e409e8b09376060c38a5b8295e8ee9af7575522

Name:           perl-Protocol-WebSocket
Version:        0.26
Release:        21%{?dist}
Summary:        WebSocket protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Protocol-WebSocket
Source0:        https://cpan.metacpan.org/authors/id/V/VT/VTI/Protocol-WebSocket-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny) >= 0.35
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed

%{?perl_default_filter}

%description
Client/server WebSocket message and frame parser/constructor. This module
does not provide a WebSocket server or client, but is made for using in
http servers or clients to provide WebSocket support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Protocol-WebSocket-%{version}
%{__sed} -i 's|\r||' ./examples/reflex.pl
# Upstream is okay with wsconsole being made available as a binary for Fedora/EPEL
# Module::Build::Tiny requires that all executables must be in script/
%{__mv} util script
%{__sed} -i -e '1s|#!/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|' script/* examples/*

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes examples
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*

%changelog
%autochangelog
