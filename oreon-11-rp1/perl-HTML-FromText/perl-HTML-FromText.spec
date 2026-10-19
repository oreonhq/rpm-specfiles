%global source0_hash c5e010324105be707fb5746bb5f2d30ccbc8e4f78d2a6e159b4147a462fe23ad
Name:           perl-HTML-FromText
Version:        2.07
Release:        1%{?dist}
Summary:        Convert plain text to HTML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FromText
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/HTML-FromText-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Email::Find::addrspec)
BuildRequires:  perl(Exporter::Lite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl-generators
# /oreon:deps
%description
"HTML::FromText" converts plain text to HTML. There are a handful of
options that shape the conversion. There is a utility function,
"text2html", that's exported by default. This function is simply a
short- cut to the Object Oriented interface described in detail below.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FromText-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
