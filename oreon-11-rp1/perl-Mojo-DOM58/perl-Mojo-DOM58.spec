%global source0_hash 1b066035a33553296c9e970d4196b759842a4af1d727b195a60b5db0ac14e338

%bcond_without perl_Mojo_DOM58_enables_role

Name:           perl-Mojo-DOM58
Version:        3.002
Release:        3%{?dist}
Summary:        Minimalistic HTML/XML DOM parser with CSS selectors
# CONTRIBUTING.md:      CC0
# lib/Mojo/DOM58.pm:    Artistic 2.0
License:        Artistic-2.0 AND CC0-1.0
URL:            https://metacpan.org/release/Mojo-DOM58
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Mojo-DOM58-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
%if %{with perl_Mojo_DOM58_enables_role}
BuildRequires:  perl(Role::Tiny) >= 2.000001
%endif
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
# Tests:
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(Exporter) >= 5.57
%if %{with perl_Mojo_DOM58_enables_role}
Suggests:       perl(Role::Tiny) >= 2.000001
%endif

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter|Test::More)\\)$

%description
Mojo::DOM58 is a minimalistic and relaxed pure-perl HTML/XML DOM parser. It
supports the HTML Living Standard and Extensible Markup Language (XML) 1.0,
and matching based on CSS3 selectors. It will even try to interpret broken
HTML and XML, so you should not use it for validation.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojo-DOM58-%{version}
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
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING MOJO_DOM58_CSS_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING MOJO_DOM58_CSS_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md examples README
%dir %{perl_vendorlib}/Mojo
%{perl_vendorlib}/Mojo/DOM58{,.pm}
%{_mandir}/man3/Mojo::DOM58{.,::}*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
