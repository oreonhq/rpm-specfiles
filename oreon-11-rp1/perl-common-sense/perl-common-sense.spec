%global source0_hash a86a1c4ca4f3006d7479064425a09fa5b6689e57261fcb994fe67d061cba0e7e

# Suspect that upstream prefers single-decimal versions
%global cpan_version 3.75
%global rpm_version 3.7.5

# This arch-specific package has no binaries and generates no debuginfo
%global debug_package %{nil}

Name:		perl-common-sense
Summary:	"Common sense" Perl defaults 
Version:	%{rpm_version}
Release:	21%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/common-sense
Source0:	https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/common-sense-%{cpan_version}.tar.gz
Patch1:		common-sense-3.71-podenc.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(feature)
BuildRequires:	perl(strict)
BuildRequires:	perl(utf8)
BuildRequires:	perl(warnings)
BuildRequires:	/usr/bin/pod2man
BuildRequires:	/usr/bin/pod2text
# Module Runtime
# (no additional dependencies)
# Test Suite
# (no additional dependencies)
# Dependencies

%description
This module implements some sane defaults for Perl programs, as defined
by two typical (or not so typical - use your common sense) specimens of
Perl coders:

It's supposed to be mostly the same, with much lower memory usage, as:

	use utf8;
	use strict qw(vars subs);
	use feature qw(say state switch);
	use feature qw(unicode_strings unicode_eval current_sub fc evalbytes);
	no feature qw(array_base);
	no warnings;
	use warnings qw(FATAL closed threads internal debugging pack
			prototype inplace io pipe unpack malloc
			deprecated glob digit printf layer
			reserved taint closure semicolon);
	no warnings qw(exec newline unopened);

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n common-sense-%{cpan_version}

# Specify POD encoding
%patch -P 1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

# Have a non-empty manpage
pod2man sense.pod > %{buildroot}%{_mandir}/man3/common::sense.3pm

%check
make test

%files
%license LICENSE
%doc Changes README t/
%dir %{perl_vendorarch}/common/
%{perl_vendorarch}/common/sense.pm
%doc %{perl_vendorarch}/common/sense.pod
%{_mandir}/man3/common::sense.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{rpm_version}-21
- Prepare for Oreon 11 (RP1)
