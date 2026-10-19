%global source0_hash 513591b4be46bd7eb91e83197721b4a045a9753a3dd2f11de82c9d3013226397
Name:		perl-Convert-BinHex
Version:	1.125
Release:        32%{?dist}
Summary:        Convert to/from RFC1741 HQX7 (Mac BinHex)
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Convert-BinHex
Source0:        https://cpan.metacpan.org/modules/by-module/Convert/Convert-BinHex-%{version}.tar.gz
BuildArch:	noarch
%global __requires_exclude ^perl\\(Mac::Files\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(autodie)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Convert::BinHex extracts data from Macintosh BinHex files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-BinHex-%{version}

# Don't want to ship a script with a security hole
perl -pi -e 's/^use lib .*$//' bin/*.pl

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test %{!?rhel:RELEASE_TESTING=1}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
