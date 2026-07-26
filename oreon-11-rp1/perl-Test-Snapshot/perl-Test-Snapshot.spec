%global source0_hash f4dd7a9a55baa2247540ae34210cd05a04f9d1061befec97a1c90eda95bfae45

Name:           perl-Test-Snapshot
Version:        0.06
Release:        16%{?dist}
Summary:        Test against data stored in automatically-named file
License:        Artistic-2.0

URL:            http://search.cpan.org/dist/Test-Snapshot/
Source0:        http://www.cpan.org/authors/id/E/ET/ETJ/Test-Snapshot-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-interpreter >= 5.008003
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirement:s
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.96

%{?perl_default_filter}

%description
Not connected with Test::Snapshots, which is based on a similar concept but
for running executables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Snapshot-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%changelog
%autochangelog
