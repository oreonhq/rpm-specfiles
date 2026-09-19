%global source0_hash f119058d685bb9f93ed8928be80804d4357d699d6b40f4d2209a0d61981647be

Name:           perl-WWW-Babelfish
Version:        0.16
Release:        50%{?dist}
Summary:        Perl extension for translation via Babelfish or Google
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/WWW-Babelfish
Source0:        https://cpan.metacpan.org/authors/id/D/DU/DURIST/WWW-Babelfish-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(LWP::UserAgent)

%{?perl_default_filter}

%description
Perl interface to the WWW babelfish translation server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Babelfish-%{version}

%build
# nix internet-based tests
echo n | %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/WWW*

%changelog
%autochangelog
