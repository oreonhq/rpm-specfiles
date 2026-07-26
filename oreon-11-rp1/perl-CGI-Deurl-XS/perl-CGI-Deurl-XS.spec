%global source0_hash 9a3c325582eab31e0ed431edd095f6f008fd734ee313bc65f582a1f3378b52a1

Name:           perl-CGI-Deurl-XS
Version:        0.08
Release:        35%{?dist}
Summary:        Fast decoder for URL parameter strings
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Apache-2.0
URL:            https://metacpan.org/release/CGI-Deurl-XS
Source0:        https://cpan.metacpan.org/modules/by-module/CGI/CGI-Deurl-XS-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

%description
This module decodes a URL-encoded parameter string in the manner of CGI.pm.
However, as it uses C code from libapreq to perform the task, it's
somewhere from slightly to much faster (depending on your strings) than
using CGI or a functionally similar module like CGI::Deurl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Deurl-XS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/CGI*
%{_mandir}/man3/*

%changelog
%autochangelog
