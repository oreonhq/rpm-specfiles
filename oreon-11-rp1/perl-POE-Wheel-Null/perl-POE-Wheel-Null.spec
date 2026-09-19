%global source0_hash 9a6844075d15b4154714d63b494fa54485205a38cd498df9badfaaeabcdcc6e4

Name:           perl-POE-Wheel-Null
Version:        0.01        
Release:        50%{?dist}
Summary:        POE Wheel that does puts data nowhere, and sends nothing
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Wheel-Null            
Source0: https://cpan.metacpan.org/authors/id/H/HA/HACHI/POE-Wheel-Null-%{version}.tar.gz        
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE::Wheel)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)

%description
POE::Wheel::Null creates a wheel which doesn't do anything upon put(), and
doesn't send any events to the current session.

Its function is the same as those pipes in the Enterprise's engine room 
marked "GNDN".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Wheel-Null-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
