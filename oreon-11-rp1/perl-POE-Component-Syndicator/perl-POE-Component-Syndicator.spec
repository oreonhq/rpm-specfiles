%global source0_hash 3775a409c080204d25b13a56968eda00933db3a1b43d08fcc9290780f7614952
Name:           perl-POE-Component-Syndicator
Version:        0.06
Release:        1%{?dist}
Summary:        POE component base class which implements the Observer pattern
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Syndicator
Source0:        https://cpan.metacpan.org/authors/id/H/HI/HINRIK/POE-Component-Syndicator-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Object::Pluggable) >= 1.29
Requires:       perl(POE) >= 1.311
%filter_from_requires /^perl(POE)$/d
%filter_from_requires /^perl(Object::Pluggable)$/d
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(POE\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Object::Pluggable\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Object::Pluggable)
BuildRequires:  perl(Object::Pluggable::Constants)
BuildRequires:  perl(POE)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
