%global source0_hash 151a352333a6d26626d9001bb7e3b3a11cd4251a191111da60a9657eb66acd6c

Name:           perl-CatalystX-Profile
Version:        0.02
Release:        40%{?dist}
Summary:        Profile your Catalyst application with Devel::NYTProf
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CatalystX-Profile
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/CatalystX-Profile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst::Runtime) >= 5.80020
BuildRequires:  perl(CatalystX::InjectComponent) >= 0.024
BuildRequires:  perl(Devel::NYTProf) >= 3.01
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose) >= 0.93
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(Sub::Identify) >= 0.04
BuildRequires:  perl(Test::More)
Requires:       perl(Catalyst::Runtime) >= 5.80020
Requires:       perl(CatalystX::InjectComponent) >= 0.024
Requires:       perl(Devel::NYTProf) >= 3.01
Requires:       perl(Moose) >= 0.93
Requires:       perl(namespace::autoclean) >= 0.09
Requires:       perl(Sub::Identify) >= 0.04

%{?perl_default_filter}

%description
This (really basic for now) plugin adds support for profiling your Catalyst
application, without profiling all the crap that happens during setup. This
noise can make finding the real profiling stuff trickier, so profiling is
disabled while this happens.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CatalystX-Profile-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
