%global source0_hash 04310e9840b918383a5b9ae9ca4b3bde1b2771ec786c758bd2fffd79d409332b
%bcond_with perl_YAML_LibYAML_enables_optional_test
Name:           perl-YAML-LibYAML
Epoch:          1
Version:        0.910.0
Release:        1%{?dist}
Summary:        Perl YAML Serialization using XS and libyaml
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAML-LibYAML
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-LibYAML-v%{version}.tar.gz
Patch0:         YAML-LibYAML-0.79-Unbundled-libyaml.patch
%if %{with perl_YAML_LibYAML_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Requires:       perl(B::Deparse)
Requires:       libyaml >= 0.2.4
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestYAML.*\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libyaml
BuildRequires:  libyaml-devel
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/000-require-modules.t
rm %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
perl -i -pe 's{^use blib;}{#use blib;}' %{buildroot}%{_libexecdir}/%{name}/t/TestYAML.pm
perl -i -pe 's{^use_blib: 1}{use_blib: 0}' %{buildroot}%{_libexecdir}/%{name}/t/yaml_tests.yaml
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
%files -n perl-YAML-LibYAML-tests -f %{oreon_filedir}/perl-YAML-LibYAML-tests.list

%changelog

%autochangelog
