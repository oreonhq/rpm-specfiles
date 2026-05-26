# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 b656b0b11a4219c125679e8cbf7436a3f636e833fd63cf322d171dcb7c3eaf3e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Run optional test
%if ! 0%{?rhel}
%bcond_without perl_YAML_LibYAML_enables_optional_test
%else
%bcond_with perl_YAML_LibYAML_enables_optional_test
%endif

Name:           perl-YAML-LibYAML
Epoch:          1
Version:        0.904.0
Release:        5%{?dist}
Summary:        Perl YAML Serialization using XS and libyaml
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAML-LibYAML
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-LibYAML-v0.904.0.tar.gz

Patch0:         YAML-LibYAML-0.79-Unbundled-libyaml.patch

# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libyaml >= 0.2.4
BuildRequires:  libyaml-devel >= 0.2.4
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed

# Module
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

# Tests
BuildRequires:  perl(B)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(experimental)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(utf8)

# A build cycle: perl-YAML-LibYAML → perl-boolean → perl-JSON-MaybeXS
# → perl-Cpanel-JSON-XS → perl-YAML-LibYAML
%if %{with perl_YAML_LibYAML_enables_optional_test} && !%{defined perl_bootstrap}
# Optional Tests
BuildRequires:  perl(boolean)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Path::Class)
%endif

# Dependencies
Requires:       perl(B::Deparse)
Requires:       libyaml >= 0.2.4

# Avoid provides for perl shared objects
%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestYAML.*\\)

%description
Kirill Siminov's "libyaml" is arguably the best YAML implementation. The C
library is written precisely to the YAML 1.1 specification. It was originally
bound to Python and was later bound to Ruby.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_verify_sources
%setup -q -n YAML-LibYAML-v%{version}
# Unbundled libyaml, the source files are the same as in libyaml-0.2.4
# It was determined by comparing commits in upstream repo:
# https://github.com/yaml/libyaml/
%patch -P 0 -p1 -b .orig
for file in api.c dumper.c emitter.c loader.c parser.c reader.c scanner.c \
    writer.c yaml.h yaml_private.h; do
    rm LibYAML/$file
    sed -i -e "/^LibYAML\/$file/d" MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# It needs libraries in lib/ not in system directories
rm %{buildroot}%{_libexecdir}/%{name}/t/000-require-modules.t
# Remove author test
rm %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
# Don't use blib
perl -i -pe 's{^use blib;}{#use blib;}' %{buildroot}%{_libexecdir}/%{name}/t/TestYAML.pm
perl -i -pe 's{^use_blib: 1}{use_blib: 0}' %{buildroot}%{_libexecdir}/%{name}/t/yaml_tests.yaml
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The solution is to
# copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README
%{perl_vendorarch}/auto/YAML/
%{perl_vendorarch}/YAML/
%{_mandir}/man3/YAML::LibYAML.3*
%{_mandir}/man3/YAML::XS.3*
%{_mandir}/man3/YAML::XS::LibYAML.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.904.0-5
- Prepare for Oreon 11 (RP1)
