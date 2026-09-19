%global source0_hash 514993f5516c16499bb918f377a07a7988bc4c8771f916dafd3014a2f24a1a06

# Perform optional tests
%bcond_without perl_Time_Out_enables_optional_test

Name:           perl-Time-Out
Version:        1.0.0
Release:        4%{?dist}
Summary:        Easily time out long running operations
# lib/Time/Out.pod: GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:          GPL-1.0-or-later OR Artistic-1.0-Perl
# Makefile.PL:      GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Time-Out
Source0:        https://cpan.metacpan.org/authors/id/S/SV/SVW/Time-Out-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.9
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp) >= 1.32
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version) >= 0.9915
# Tests:
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 1.001005
%if %{with perl_Time_Out_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Time::HiRes) >= 1.9726
%endif
Requires:       perl(Carp) >= 1.32
Provides:       perl(Time::Out) = %{version}
Provides:       perl(Time::Out::Exception) = %{version}
Provides:       perl(Time::Out::ParamConstraints) = %{version}

# Remove under-specified modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test::More|Time::HiRes)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Time::Out(|::Exception|::ParamConstraints)\\)$

%description
The Time::Out module provides an easy interface to alarm(2) based timeouts.
Nested timeouts are supported.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(IO::Handle)
Requires:       perl(Test::More) >= 1.001005
%if %{with perl_Time_Out_enables_optional_test}
Requires:       perl(Time::HiRes) >= 1.9726
%endif
Requires:       perl(warnings)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-Out-%{version}
# Remove release tests that are always skipped
for F in \
%if %{without perl_Time_Out_enables_optional_test}
        t/06-RT-84141.t \
%endif
        t/09-pod.t t/10-critic.t; do
    rm -- "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done;
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
# MAKELEVEL not to use ./maint/AuthorExtensions.pl
MAKELEVEL=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
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
%dir %{perl_vendorlib}/Time
%{perl_vendorlib}/Time/Out
%{perl_vendorlib}/Time/Out.*
%{_mandir}/man3/Time::Out.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
