%global source0_hash 014b7d1bac86616e0ad7c8476e0a6b6c21d98615ec10cb5bc400ba06ebc288ac
%global cpan_version 3.64
Name:           perl-ExtUtils-ParseXS
Epoch:          1
Version:        3.64
Release:        1%{?dist}
Summary:        Module and a script for converting Perl XS code into C code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-ParseXS
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/ExtUtils-ParseXS-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter) >= 5.57
Requires:       perl(fields)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(ExtUtils::Typemaps::Test\\)
%global __requires_exclude %{__requires_exclude}|^perl\\((TypemapTest::Foo\|IncludeTester\|PrimitiveCapture)\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(attributes)
BuildRequires:  perl(fields)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and creates
the glue necessary to let Perl access those functions.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ExtUtils-ParseXS-%{cpan_version}

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
%{_fixperms} $RPM_BUILD_ROOT/*
rm $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/xsubpp
ln -s ../../../../bin/xsubpp $RPM_BUILD_ROOT%{perl_vendorlib}/ExtUtils/
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-ExtUtils-ParseXS-tests -f %{oreon_filedir}/perl-ExtUtils-ParseXS-tests.list

%changelog

%autochangelog
