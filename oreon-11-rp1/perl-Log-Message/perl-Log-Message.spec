%global source0_hash bd697dd62aaf26d118e9f0a0813429deb1c544e4501559879b61fcbdfe99fe46

Name:           perl-Log-Message
# Epoch to compete with perl.spec
Epoch:          1
Version:        0.08
Release:        38%{?dist}
Summary:        Generic message storing mechanism
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Message
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(if)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(deprecate)

%description
This package enables you to do generic message logging throughout programs and
projects. Every message will be logged with stack traces, time stamps and so
on.  You can use built-in handlers immediately, or after the fact when you
inspect the error stack. It is highly configurable and let's you even provide
your own handlers for dealing with messages.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Message-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
