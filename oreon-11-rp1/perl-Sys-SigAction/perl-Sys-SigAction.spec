%global source0_hash e04c9a7fdf745d3e9cd9e8b2d5a46d826ba958c5e1e0c48b3cd132bb15396255

Name:           perl-Sys-SigAction
Version:        0.24
Release:        3%{?dist}
Summary:        Perl extension for Consistent Signal Handling
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-SigAction
Source0:        https://cpan.metacpan.org/modules/by-module/Sys/Sys-SigAction-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >=  5.5
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# threads not helpful
BuildRequires:  perl(Time::HiRes)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
Requires:       perl(Time::HiRes)

%description
Sys::SigAction provides EASY access to POSIX::sigaction() for signal
handling on systems that support sigaction().
It is hoped that with the use of this module, your signal handling 
behavior can be coded in a way that does not change from one perl 
version to the next, and that sigaction() will be easier for you to use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sys-SigAction-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
pod2man --name=dbd-oracle-timeout < dbd-oracle-timeout.POD \
    > dbd-oracle-timeout.man

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README dbd-oracle-timeout.man
%dir %{perl_vendorlib}/Sys
%{perl_vendorlib}/Sys/SigAction
%{perl_vendorlib}/Sys/SigAction.pm
%{_mandir}/man3/Sys::SigAction.*

%changelog
%autochangelog
