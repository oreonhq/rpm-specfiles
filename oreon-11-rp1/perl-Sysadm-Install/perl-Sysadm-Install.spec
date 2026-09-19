%global source0_hash ffdf1c4291dae94650a728e251beba8e6fcd2e5c697bcde0d791b5fb9c6b8c99

Summary:	Typical installation tasks for system administrators
Name:		perl-Sysadm-Install
Version:	0.48
Release:	27%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Sysadm-Install
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/Sysadm-Install-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Expect)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp) >= 0.16
BuildRequires:	perl(File::Which) >= 1.09
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Status)
BuildRequires:	perl(Log::Log4perl) >= 1.00
BuildRequires:	perl(Log::Log4perl::Util)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(strict)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(utf8)
# Dependencies
Requires:	perl(Archive::Tar)
Requires:	perl(Encode)
Requires:	perl(Expect)
Requires:	perl(HTTP::Request)
Requires:	perl(HTTP::Status)
Requires:	perl(LWP::UserAgent)

%description
"Sysadm::Install" executes shell-like commands performing typical
installation tasks: Copying files, extracting tarballs, calling "make".
It has a "fail once and die" policy, meticulously checking the result of
every operation and calling "die()" immediately if anything fails,
with optional logging of everything.

"Sysadm::Install" also supports a *dry_run* mode, in which it logs
everything, but suppresses any write actions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sysadm-Install-%{version}

# Fix perl interpreter in eg/mkperl
perl -pi -e 's|/usr/local/bin/perl|/usr/bin/perl|;' eg/mkperl

# Note: not turning off exec bits in examples because they don't
# introduce any unwanted dependencies

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test TEST_VERBOSE=1

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%files
%doc Changes README eg/
# one-liner is an overly-generic name to include in %%{_bindir} and is included
# as %%doc if needed
%exclude %{_bindir}/one-liner
%{perl_vendorlib}/Sysadm/
%{_mandir}/man3/Sysadm::Install.3*

%changelog
%autochangelog
