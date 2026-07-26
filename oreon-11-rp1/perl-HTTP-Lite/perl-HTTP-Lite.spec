%global source0_hash 38e43d7911cfc14e3a38f0382b6cc7a6d559307d23b109ce73ac7d24a9b3e77c

Name:           perl-HTTP-Lite
Version:        2.44
Release:        40%{?dist}
Summary:        Lightweight HTTP implementation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/HTTP-Lite
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/HTTP-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::Pod)
%endif

%{?perl_default_filter}

%description
HTTP::Lite is a stand-alone lightweight HTTP/1.1 implementation for perl. It is
not intended as a replacement for the fully-features LWP module. Instead, it is
intended for use in situations where it is desirable to install the minimal
number of modules to achieve HTTP support, or where LWP is not a good candidate
due to CPU overhead, such as slower processors. HTTP::Lite is also
significantly faster than LWP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Lite-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# most real tests require network access - ignore "skipping test on this
# platform" messages
%if !%{defined perl_bootstrap}
RELEASE_TESTING=1 make test
%endif

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
