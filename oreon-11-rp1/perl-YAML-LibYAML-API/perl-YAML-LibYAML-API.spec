%global source0_hash 31a0fedd77d824dab38983be9a3b426863f8aab13013beb95c4ecf80959733e1

Name:           perl-YAML-LibYAML-API
Version:        0.14.0
Release:        9%{?dist}
Summary:        Wrapper around the C libyaml library
License:        MIT
URL:            https://metacpan.org/release/YAML-LibYAML-API
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-LibYAML-API-v%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libyaml-devel >= 0.2.5
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(YAML::PP::Common) >= 0.024
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(YAML::PP::Common) >= 0.024

# Filter unversioned require
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(YAML::PP::Common\\)

%description
This module provides a thin wrapper around the C libyaml API.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n YAML-LibYAML-API-v%{version}

# Unbundled libyaml
for F in api.c config.h dumper.c emitter.c loader.c parser.c reader.c \
    scanner.c writer.c yaml.h yaml_private.h; do
    rm "LibYAML/$F"
    perl -i -ne 'print $_ unless m{^LibYAML/\Q'"$F"'\E}' MANIFEST
done

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
WITH_SYSTEM_LIBYAML=1 perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/YAML*
%{perl_vendorarch}/YAML*
%{_mandir}/man3/YAML::LibYAML::API*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
