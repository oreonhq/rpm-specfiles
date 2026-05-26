%global cpan_version 1.35
Name:           perl-Time-Local
Epoch:          2
Version:        %{cpan_version}0
Release:        521%{?dist}
Summary:        Efficiently compute time from local and GMT time
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Time-Local
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Time-Local-%{cpan_version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 1d136b71bd041cbe6f66c43180ee79e675b72ad5a3596abd6a44d211072ada29
%global source0_file Time-Local-1.35.tar.gz
# oreon url source checksums end
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
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
# Tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Config)

%description
This module provides functions that are the inverse of built-in perl functions
localtime() and gmtime(). They accept a date as a six-element array, and
return the corresponding time(2) value in seconds since the system epoch
(Midnight, January 1, 1970 GMT on Unix, for example). This value can be
positive or negative, though POSIX only requires support for positive values,
so dates before the system's epoch may not work on all operating systems.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Time-Local-1.35.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1d136b71bd041cbe6f66c43180ee79e675b72ad5a3596abd6a44d211072ada29" || { echo "oreon: Source0 SHA256 mismatch for Time-Local-1.35.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Time-Local-%{cpan_version}
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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{perl_vendorlib}/Time*
%{_mandir}/man3/Time::Local*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{cpan_version}0-521
- Prepare for Oreon 11 (RP1)
