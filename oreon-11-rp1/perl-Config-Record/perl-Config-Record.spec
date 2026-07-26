%global source0_hash 47ea02fafc936d35d36bb3abe2631e3e5ae9ba05323b2b0d1154ab73f8ac212f

Name:           perl-Config-Record
Version:        1.1.2
Release:        47%{?dist}
Summary:        Perl module for Configuration file access

License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Config-Record
Source:         https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Config-Record-%{version}.tar.gz
Patch0:         Config-Record-1.1.2-Fix-building-on-Perl-without-dot-in-INC.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

%description
Config::Record provides a module for loading configuration
records. It supports scalar, array and hash parameters nested
to an arbitrary depth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Record-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc AUTHORS CHANGES README
%{perl_vendorlib}/Config/
%{_mandir}/man3/Config::Record*.3pm*

%changelog
%autochangelog
