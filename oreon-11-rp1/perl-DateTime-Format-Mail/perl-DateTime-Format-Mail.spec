# Run extra tests
%bcond_without perl_DateTime_Format_Mail_enables_extra_test

Name:           perl-DateTime-Format-Mail
Epoch:          1
Version:        0.403
Release:        28%{?dist}
Summary:        Convert between DateTime and RFC2822/822 formats
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-Mail            
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/DateTime-Format-Mail-0.403.tar.gz
# oreon url source checksums begin
%global source0_sha256 8df8e35c4477388ff5c7ce8b3e8b6ae4ed30209c7a5051d41737bd14d755fcb0
%global source0_file DateTime-Format-Mail-0.403.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime) >= 1.04
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_DateTime_Format_Mail_enables_extra_test}
# Author tests
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Release tests
BuildRequires:  perl(Test::CPAN::Meta)
%endif
# Dependencies
# (none)

%description
RFCs 2822 and 822 specify date formats to be used by email. This module parses
and emits such dates.

RFC2822 (April 2001) introduces a slightly different format of date than that
used by RFC822 (August 1982). The main correction is that the preferred format
is more limited, and thus easier to parse programmatically.

Despite the ease of generating and parsing perfectly valid RFC822 and RFC2822
people still get it wrong. This module aims to correct that.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/DateTime-Format-Mail-0.403.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8df8e35c4477388ff5c7ce8b3e8b6ae4ed30209c7a5051d41737bd14d755fcb0" || { echo "oreon: Source0 SHA256 mismatch for DateTime-Format-Mail-0.403.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n DateTime-Format-Mail-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

%check
make test %{?with_perl_DateTime_Format_Mail_enables_extra_test:\
    AUTHOR_TESTING=1 RELEASE_TESTING=1}

%files
%license LICENSE
%doc CREDITS Changes README
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Format::Mail.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.403-28
- Prepare for Oreon 11 (RP1)
