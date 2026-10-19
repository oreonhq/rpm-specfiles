%global source0_hash 1b066035a33553296c9e970d4196b759842a4af1d727b195a60b5db0ac14e338
%bcond_without perl_Mojo_DOM58_enables_role
Name:           perl-Mojo-DOM58
Version:        3.002
Release:        1%{?dist}
Summary:        Minimalistic HTML/XML DOM parser with CSS selectors
License:        Artistic-2.0 AND CC0-1.0
URL:            https://metacpan.org/release/Mojo-DOM58
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Mojo-DOM58-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Mojo_DOM58_enables_role}
%endif
Requires:       perl(Exporter) >= 5.57
%if %{with perl_Mojo_DOM58_enables_role}
Suggests:       perl(Role::Tiny) >= 2.000001
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING MOJO_DOM58_CSS_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING MOJO_DOM58_CSS_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Mojo-DOM58-tests -f %{oreon_filedir}/perl-Mojo-DOM58-tests.list

%changelog

%autochangelog
