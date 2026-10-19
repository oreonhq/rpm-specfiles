%global source0_hash 15c188253993a4b66e5599f0789b1326f0a66c092bdbfac9313706d41c285170
%bcond_with perl_Archive_Any_Lite_enables_extra_test
Name:		perl-Archive-Any-Lite
Version:	0.11
Release:        1%{?dist}
Summary:        Simple CPAN package extractor
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Archive-Any-Lite
Source0:        https://cpan.metacpan.org/modules/by-module/Archive/Archive-Any-Lite-%{version}.tar.gz
Patch0:		Archive-Any-Lite-0.08-EU:MM.patch
BuildArch:	noarch
%if %{with perl_Archive_Any_Lite_enables_extra_test}
%endif
Requires:	perl(IO::Uncompress::Bunzip2)
Requires:	perl(IO::Zlib)
Provides:       perl(Archive::Any::Lite)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a fork of Archive::Any by Michael Schwern and Clint Moore. The main
difference is that this works properly even when you fork(), and may require
less memory to extract a tarball. On the other hand, this isn't pluggable
(it only supports file formats used in the CPAN toolchains), and it doesn't
check MIME types.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Archive-Any-Lite-%{version}

# Build with ExtUtils::MakeMaker rather than ExtUtils::MakeMaker::CPANfile
%patch -P0

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test TEST_POD=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
