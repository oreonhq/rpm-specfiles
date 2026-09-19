%global source0_hash 967e99ba0cf6af654bcf6028610f8c209dcfed601a78a84f9de436d4f4e7d268

%global cpan_name Directory-Queue

Name:           perl-%{cpan_name}
Version:        2.2
Release:        12%{?dist}
Summary:        Object oriented interface to a directory based queue
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
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(No::Worries::Die) >= 1.4
BuildRequires:  perl(No::Worries::Export)
BuildRequires:  perl(No::Worries::File)
BuildRequires:  perl(No::Worries::Stat)
BuildRequires:  perl(No::Worries::Warn)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(No::Worries::Dir)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(No::Worries::Die) >= 1.4

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(No::Worries::Die\\)$

%description
The goal of this module is to offer a simple queue system using the underlying
file system for storage, security and to prevent race conditions via atomic
operations. It focuses on simplicity, robustness and scalability.

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
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%dir %{perl_vendorlib}/Directory
%{perl_vendorlib}/Directory/Queue
%{perl_vendorlib}/Directory/Queue.pm
%{_mandir}/man3/Directory::Queue.*
%{_mandir}/man3/Directory::Queue::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
