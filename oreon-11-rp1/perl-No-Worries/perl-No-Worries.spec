%global source0_hash 2fddf3051ec57a42073d157ea2fddf509889508ce73cf7dacc7682efa9bcdb6a

%global cpan_name No-Worries

Name:           perl-%{cpan_name}
Version:        1.7
Release:        14%{?dist}
Summary:        Perl coding without worries
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LC/LCONS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI::Escape)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08

%description
This module and its sub-modules ease coding by providing consistent convenient
functions to perform frequently used programming tasks.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{3pod,4podcov}.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset NO_WORRIES
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%dir %{perl_vendorlib}/No
%{perl_vendorlib}/No/Worries
%{perl_vendorlib}/No/Worries.pm
%{_mandir}/man3/No::Worries.*
%{_mandir}/man3/No::Worries::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
