%global source0_hash 3ddfb2bdd2e7ef2d949dbd8ffb51439164c84d22bff615e47dbd8ea48ba75cae

Name:           perl-YAML-PP
Version:        0.41.0
Release:        1%{?dist}
Summary:        YAML 1.2 processor
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAML-PP/
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-PP-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(experimental)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.07
BuildRequires:  perl(Term::ANSIColor) >= 4.02
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdArray)
BuildRequires:  perl(Tie::StdHash)
# Tests
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Warnings) >= 0.005
BuildRequires:  perl(Tie::IxHash)
Requires:       perl(boolean)
Requires:       perl(B::Deparse)
Requires:       perl(Cpanel::JSON::XS)
Requires:       perl(experimental)
Requires:       perl(HTML::Entities)
Requires:       perl(JSON::PP)
Requires:       perl(JSON::XS)
Requires:       perl(Scalar::Util) >= 1.07
Requires:       perl(Term::ANSIColor)
Requires:       perl(Tie::IxHash)
Requires:       perl(YAML::PP::Schema::Include)
# bin/yamlpp-load can use various YAML implementations on user's request:
Suggests:       perl(YAML)
Suggests:       perl(YAML::PP::LibYAML)
Suggests:       perl(YAML::PP::LibYAML::Parser)
Suggests:       perl(YAML::PP::Ref)
Suggests:       perl(YAML::Syck)
Suggests:       perl(YAML::Tiny)
Suggests:       perl(YAML::XS)

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Scalar::Util\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(YAML::PP::Test)\s*$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

Provides:       perl(YAML::PP)
Provides:       perl(YAML::PP::Schema::Include)
%description
YAML::PP is a modern, modular YAML processor.
It aims to support YAML 1.2 and YAML 1.1. See http://yaml.org/.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n YAML-PP-v%{version}

for i in $(find e* -type f); do
    chmod -x "$i"
    perl -i -MConfig -pe 's{\A#!.*perl}{$Config{startperl}}' "$i"
done

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
cp -a t examples ext test-suite %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{\$Bin/data/simple-out.yaml}{/tmp/simple-out.yaml}' %{buildroot}%{_libexecdir}/%{name}/t/19.file.t
perl -i -pe 's{\$Bin/data/simple.yaml.copy}{/tmp/simple.yaml.copy}' %{buildroot}%{_libexecdir}/%{name}/t/30.legacy.t

# t/00.compile.t examines ./bin
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
for F in yamlpp-events yamlpp-highlight yamlpp-load yamlpp-load-dump yamlpp-parse-emit; do
    ln -s %{_bindir}/"$F" %{buildroot}%{_libexecdir}/%{name}/bin
done

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
%doc Changes CONTRIBUTING.md etc examples README.md
%{_bindir}/yamlpp-*
%dir %{perl_vendorlib}/YAML
%{perl_vendorlib}/YAML/PP*
%{_mandir}/man3/YAML::PP*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
