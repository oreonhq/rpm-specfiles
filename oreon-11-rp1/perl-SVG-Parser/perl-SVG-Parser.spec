%global source0_hash 6c8c9117795f240cfe33a8e8345a0f7f220f89e259a604f148d204c7758cfbe1

Name:           perl-SVG-Parser
Version:        1.03
Release:        50%{?dist}
Summary:        XML Parser for SVG documents
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVG-Parser
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETERW/SVG-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(SVG) >= 2.0
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base)
# Tests:
BuildRequires:  perl(Test)

%{?perl_default_filter}

%description
SVG::Parser is an XML parser for SVG Documents. It takes XML as input and
produces an SVG object as its output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SVG-Parser-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
