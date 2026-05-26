Name:		perl-File-Slurp-Tiny
Version:	0.004
Release:	30%{?dist}
Summary:	A simple, sane and efficient file slurper
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/File-Slurp-Tiny
Source0:	https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Slurp-Tiny-0.004.tar.gz
# oreon url source checksums begin
%global source0_sha256 452995beeabf0e923e65fdc627a725dbb12c9e10c00d8018c16d10ba62757f1e
%global source0_file File-Slurp-Tiny-0.004.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
# (none)

%description
This module provides functions for fast and correct slurping and spewing
of files.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-Slurp-Tiny-0.004.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "452995beeabf0e923e65fdc627a725dbb12c9e10c00d8018c16d10ba62757f1e" || { echo "oreon: Source0 SHA256 mismatch for File-Slurp-Tiny-0.004.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n File-Slurp-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Slurp::Tiny.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.004-30
- Prepare for Oreon 11 (RP1)
