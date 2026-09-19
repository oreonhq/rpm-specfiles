%global source0_hash 6e6b0e4172acb6a53c222639c000608c2dd61d50848647482ac8600d50e541ef

Name:           perl-URI-ws
Version:        0.03
Release:        32%{?dist}
Summary:        WebSocket support for URI package
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/URI-ws
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/URI-ws-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::_server)
BuildRequires:  perl(warnings)

%description
After this module is installed, the URI package provides the same set of
methods for WebSocket URIs as it does for HTTP ones. For secure WebSockets,
see URI::wss.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-ws-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/URI*
%{_mandir}/man3/URI*

%changelog
%autochangelog
