%global source0_hash 6f1b1787df5492793a545746fe2963ad6e1b6203179f65e646cdca41e9fb3cc0

Name:           perl-Convert-Binary-C
Version:        0.86
Release:        2%{?dist}
Summary:        Binary data conversion using C types
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Binary-C
Source0:        https://cpan.metacpan.org/modules/by-module/Convert/Convert-Binary-C-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
# Optional tests
BuildRequires:  perl(Pod::Coverage) >= 0.10
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Pod) >= 0.95
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Thread)
BuildRequires:  perl(threads)

%description
Convert::Binary::C is a preprocessor and parser for C type definitions. It
is highly configurable and supports arbitrarily complex data structures.
Its object-oriented interface has pack and unpack methods that act as
replacements for Perl's pack and unpack and allow to use C types instead of
a string representation of the data structure for conversion of binary data
from and to Perl's complex data structures.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Data::Dumper)
Requires:       perl(Scalar::Util)
Requires:       perl(threads)
Requires:       perl(Time::HiRes)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-Binary-C-%{version}

# Help generators to recognize Perl scripts
for F in tests/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/%{name}
cp -a examples tests $RPM_BUILD_ROOT/%{_libexecdir}/%{name}
rm $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/tests/80*pod*
cat > $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README.md TODO
%{_bindir}/ccconfig*
%{perl_vendorarch}/auto/Convert*
%dir %{perl_vendorarch}/Convert
%{perl_vendorarch}/Convert/Binary*
%{_mandir}/man1/ccconfig*
%{_mandir}/man3/Convert::Binary::C*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
