# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Devel_CheckLib_enables_optional_test
%else
%bcond_with perl_Devel_CheckLib_enables_optional_test
%endif

Name:           perl-Devel-CheckLib
Version:        1.16
Release:        16%{?dist}
Summary:        Check that a library is available

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-CheckLib
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTN/Devel-CheckLib-1.16.tar.gz
# oreon url source checksums begin
%global source0_sha256 869d38c258e646dcef676609f0dd7ca90f085f56cf6fd7001b019a5d5b831fca
%global source0_file Devel-CheckLib-1.16.tar.gz
# oreon url source checksums end


BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.16
BuildRequires:  perl(Text::ParseWords)
# Tests:
BuildRequires:  gcc
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests
%if %{with perl_Devel_CheckLib_enables_optional_test}
BuildRequires:  perl(Mock::Config)
%endif
# perl inherits the compiler flags it was built with, hence we need this on hardened systems
Requires:       redhat-rpm-config

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
Devel::CheckLib is a perl module that checks whether a particular C library
and its headers are available.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       gcc
# Optional tests
%if %{with perl_Devel_CheckLib_enables_optional_test}
Requires:       perl(Mock::Config)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Devel-CheckLib-1.16.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "869d38c258e646dcef676609f0dd7ca90f085f56cf6fd7001b019a5d5b831fca" || { echo "oreon: Source0 SHA256 mismatch for Devel-CheckLib-1.16.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Devel-CheckLib-%{version}

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
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -ne 'print $_ unless m{\Q'-Mblib'\E}' %{buildroot}%{_libexecdir}/%{name}/t/cmdline-LIBS-INC.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests need to write into temporary files/directories.
# Copy the tests into a writable directory and execute them from there.
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
%doc CHANGES README TODO
%{_bindir}/use-devel-checklib
%{perl_vendorlib}/Devel*
%{_mandir}/man1/use-devel-checklib.1*
%{_mandir}/man3/Devel::CheckLib.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-16
- Prepare for Oreon 11 (RP1)
