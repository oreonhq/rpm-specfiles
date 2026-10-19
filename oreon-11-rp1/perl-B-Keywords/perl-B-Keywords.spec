%global source0_hash e0aa19d3390409f0ece7342ab041c5b432c31d7cf1abf182c134b6aab78784b0
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_B_Keywords_enables_extra_test
Name:           perl-B-Keywords
Version:        1.29
Release:        1%{?dist}
Summary:        Lists of reserved barewords and symbol names
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Keywords
Source0:        https://cpan.metacpan.org/modules/by-module/B/B-Keywords-%{version}.tar.gz
BuildArch:      noarch
%if 0%{!?perl_bootstrap:1} && %{with perl_B_Keywords_enables_extra_test}
%endif
Provides:       perl(B::Keywords)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
B::Keywords supplies several arrays of exportable keywords: @Scalars, @Arrays,
@Hashes, @Filehandles, @Symbols, @Functions, @Barewords, @TieIOMethods,
@UNIVERSALMethods and @ExporterSymbols.

The @Symbols array includes the contents of each of @Scalars, @Arrays, @Hashes,
@Functions and @Filehandles.

Similarly, @Barewords adds a few non-function keywords and operators to the
@Functions array.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl-devel
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n B-Keywords-%{version}

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
%{_fixperms} -c %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/z_*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%if 0%{!?perl_bootstrap:1} && %{with perl_B_Keywords_enables_extra_test}
make test IS_MAINTAINER=1 AUTHOR_TESTING=1
%else
make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n perl-B-Keywords-tests -f %{oreon_filedir}/perl-B-Keywords-tests.list

%changelog

%autochangelog
