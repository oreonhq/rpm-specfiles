%global source0_hash c7c8a652d2977c8319ea86cd5e1c5be51bd4a6bfc37a5ec5cc0df4345ff450a2

Name:           perl-Business-CreditCard
Version:        0.39
Release:        9%{?dist}
Summary:        Validate/generate credit card check-sums/names
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Business-CreditCard
Source0:        https://cpan.metacpan.org/modules/by-module/Business/Business-CreditCard-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)

%description
These subroutines tell you whether a credit card number is self-consistent
-- whether the last digit of the number is a valid check-sum for the
preceding digits.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Business-CreditCard-%{version}
for F in BINS; do
    iconv -f iso-8859-1 -t utf-8 <"$F" >"${F}.utf8"
    touch -r "$F"{,.utf8}
    mv "$F"{.utf8,}
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
%doc BINS Changes CONTRIBUTING.md README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
