%global source0_hash f1adcb543d5a1ce59be08a25578125992c6dcf1d4888fd9ff658823b46922c24

Name:           perl-CPAN-Uploader
Version:        0.103019
Release:        1%{?dist}
Summary:        Upload things to the CPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Uploader
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/CPAN-Uploader-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
# Unused BuildRequires:  perl(Config::Identity)
# Unused BuildRequires:  perl(Data::Dumper)
# Unused BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
# Unused BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.084
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
# Unused BuildRequires:  perl(LWP::Protocol::https) >= 1
BuildRequires:  perl(LWP::UserAgent)
# Unused BuildRequires:  perl(Term::ReadKey)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::MD5)
Requires:       perl(LWP::Protocol::https) >= 1
Requires:       perl(Term::ReadKey)

# cpan-upload replaced by perl-CPAN-Uploader, bugs #1043581, #1095426
Provides:       cpan-upload = 2.2-17
Obsoletes:      cpan-upload < 2.2-18

%{?perl_default_filter}

%description
CPAN::Uploader is a module which automates the process of uploading a file to
CPAN using PAUSE, the Perl Authors Upload Server.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPAN-Uploader-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/CPAN*
%{perl_vendorlib}/CPAN/Uploader.pm
%{_bindir}/cpan-upload
%{_mandir}/man1/cpan-upload*
%{_mandir}/man3/CPAN::Uploader*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
