%global source0_hash b2b6b31745c57431fca0efb9b9d0b8f168d6081755e048fd9d6c4469bd108acd

Name:           perl-VM-EC2
Version:        1.28
Release:        33%{?dist}
Summary:        Perl interface to Amazon EC2
# lib/VM/EC2.pm:    GPL-1.0-or-later OR Artistic-2.0
# LICENSE:          GPL-1.0-or-later OR Artistic-2.0
# DISCLAIMER.txt:   GPL-1.0-or-later OR Artistic-1.0-Perl
# See <https://rt.cpan.org/Public/Bug/Display.html?id=104957>.
License:        (GPL-1.0-or-later OR Artistic-2.0) AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/VM-EC2
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/VM-EC2-%{version}.tar.gz
# Fix a typo leading to unresolved dependencies, CPAN RT#104961
Patch0:         VM-EC2-1.28-Fix-a-typo-in-used-module-name.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(AnyEvent) >= 7.04
BuildRequires:  perl(AnyEvent::CacheDNS) >= 0.08
BuildRequires:  perl(AnyEvent::CondVar)
BuildRequires:  perl(AnyEvent::HTTP) >= 2.15
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA) >= 5.47
BuildRequires:  perl(File::Basename)
# File::Find not used at tests
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
# Getopt::Long not used at tests
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
# LWP::UserAgent version from LWP's version in META.json
# LWP::UserAgent 5.835 not used at tests
BuildRequires:  perl(MIME::Base64) >= 3.08
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Storable not used at tests
BuildRequires:  perl(String::Approx) >= 3.26
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Simple) >= 2.18
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
Requires:       perl(AnyEvent) >= 7.04
Requires:       perl(AnyEvent::HTTP) >= 2.15
Requires:       perl(Digest::SHA) >= 5.47
Requires:       perl(File::Path) >= 2.08
# LWP::UserAgent version from LWP's version in META.json
Requires:       perl(LWP::UserAgent) >= 5.835
Requires:       perl(String::Approx) >= 3.26
Requires:       perl(XML::Simple) >= 2.18

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((AnyEvent|AnyEvent::HTTP|Digest::SHA|File::Path|LWP::UserAgent|String::Approx|XML::Simple)\\)$
# Filter under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(VM::EC2\\)$
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(EC2TestSupport\\)
%global __provides_exclude %{__provides_exclude}|^perl\\(EC2TestSupport\\)

%description
This is an interface to the 2014-05-01 version of the Amazon AWS API
(https://aws.amazon.com/ec2/). It was written provide access to the new tag
and metadata interface that is not currently supported by Net::Amazon::EC2, as
well as to provide developers with an extension mechanism for the API. This
library will also support the Open Stack open source cloud
(https://www.openstack.org/).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n VM-EC2-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" </dev/null
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test </dev/null

%files
%license DISCLAIMER.txt LICENSE
%doc Changes README
%{_bindir}/migrate-ebs-image.pl
%{_bindir}/sync_to_snapshot.pl
%dir %{perl_vendorlib}/VM
%{perl_vendorlib}/VM/EC2
%{perl_vendorlib}/VM/EC2.pm
%{_mandir}/man1/migrate-ebs-image.pl.*
%{_mandir}/man3/VM::EC2.*
%{_mandir}/man3/VM::EC2::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
