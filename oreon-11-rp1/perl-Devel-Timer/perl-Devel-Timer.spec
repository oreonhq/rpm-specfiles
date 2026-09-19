%global source0_hash 6a2b99d3ebfb78200fa649fdf5fe196b56c511fee96b8f2b0756838cc1c74755

Name:           perl-Devel-Timer
Version:        0.14
Release:        10%{?dist}
Summary:        Track and report execution time for parts of code
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Timer

Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Devel-Timer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Testing
BuildRequires:  perl(Capture::Tiny) >= 0.25
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Devel::Timer allows developers to accurately time how long a specific
piece of code takes to execute. This can be helpful in locating the
slowest parts of an existing application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Timer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
