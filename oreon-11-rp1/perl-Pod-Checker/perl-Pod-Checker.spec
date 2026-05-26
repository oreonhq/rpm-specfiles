Name:           perl-Pod-Checker
# Compete with perl.spec
Epoch:          4
Version:        1.77
Release:        521%{?dist}
Summary:        Check POD documents for syntax errors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Checker
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Checker-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 131a7c049bed758cab29901792c999ca315d4e881c630d3f93bf6aae69e9e242
%global source0_file Pod-Checker-1.77.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(Pod::Simple) >= 3.4
BuildRequires:  perl(Pod::Simple::Methody)
# Pod::Usage not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# VMS::Filespec not used
Requires:       perl(Pod::Simple) >= 3.28

%description
Module and tools to verify POD documentation contents for compliance with the
Plain Old Documentation format specifications.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Pod-Checker-1.77.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "131a7c049bed758cab29901792c999ca315d4e881c630d3f93bf6aae69e9e242" || { echo "oreon: Source0 SHA256 mismatch for Pod-Checker-1.77.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Pod-Checker-%{version}
for F in CHANGES README; do
    perl -pi -e 's/\r//' "$F"
done

# Help generators to recognize Perl scripts
for F in `find t/pod -name *.t -o -name *.pl`; do
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
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
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc CHANGES README
%{_bindir}/podchecker
%{perl_vendorlib}/Pod*
%{_mandir}/man1/podchecker*
%{_mandir}/man3/Pod::Checker*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.77-521
- Prepare for Oreon 11 (RP1)
