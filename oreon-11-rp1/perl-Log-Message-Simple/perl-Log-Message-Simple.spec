%global source0_hash aa12d1a4c0ac260b94d448fa01feba242a8a85cb6cbfdc66432e3b5b468add96
Name:           perl-Log-Message-Simple
Version:        0.10
Release:        325%{?dist}
Summary:        Simplified interface to Log::Message
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Message-Simple
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Log-Message-Simple-%{version}.tar.gz
BuildArch:      noarch
%if 0%(perl -e 'print $] > 5.017')
%endif
%if 0%(perl -e 'print $] > 5.017')
Requires:       perl(deprecate)
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Log::Message)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a simplified front-end to Log::Message, offering
most common use for logging, and easy access to the stack (in both
raw and pretty-printable form).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Message-Simple-%{version}
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Log-Message-Simple-tests -f %{oreon_filedir}/perl-Log-Message-Simple-tests.list

%changelog

%autochangelog
