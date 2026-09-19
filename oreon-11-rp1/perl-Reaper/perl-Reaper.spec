%global source0_hash 583d0f310d87aace1ddecd3f779ec72bfc6b75ee79806da0e02ea15663f006a6

Name:           perl-Reaper
Version:        1.00
Release:        43%{?dist}
Summary:        Support for reaping child processes via $SIG{CHLD}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Reaper
Source0:        https://cpan.metacpan.org/authors/id/J/JG/JGS/Reaper-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%{?perl_default_filter}

%description
perl has an annoying little problem with child processes -- well, it is not
actually a problem specific to perl, but it is somewhat more difficult with
perl: reaping child processes after they exit so they don't hang around as
zombies forever, and doing it in a way that accurately captures the exit
code of the child.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Reaper-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
