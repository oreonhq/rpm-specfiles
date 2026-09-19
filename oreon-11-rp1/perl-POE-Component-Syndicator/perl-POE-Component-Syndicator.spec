%global source0_hash 3775a409c080204d25b13a56968eda00933db3a1b43d08fcc9290780f7614952

Name:           perl-POE-Component-Syndicator
Version:        0.06
Release:        40%{?dist}
Summary:        POE component base class which implements the Observer pattern
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Syndicator
Source0:        https://cpan.metacpan.org/authors/id/H/HI/HINRIK/POE-Component-Syndicator-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Object::Pluggable) >= 1.29
BuildRequires:  perl(Object::Pluggable::Constants)
BuildRequires:  perl(POE) >= 1.311
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Object::Pluggable) >= 1.29
Requires:       perl(POE) >= 1.311

# Underspecified dependencies filter
# RPM 4.8 style
%filter_from_requires /^perl(POE)$/d
%filter_from_requires /^perl(Object::Pluggable)$/d
%{?perl_default_filter}
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(POE\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Object::Pluggable\\)$

%description
POE::Component::Syndicator is a base class for POE components which need to
handle a persistent resource (e.g. a connection to an IRC server) for one
or more sessions in an extendable way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Syndicator-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes dist.ini LICENSE META.json README xt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
