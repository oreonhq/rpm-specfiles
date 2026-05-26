# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_DB_File_enables_optional_test
%else
%bcond_with perl_DB_File_enables_optional_test
%endif

Name:           perl-DB_File
Version:        1.860
Release:        1%{?dist}
Summary:        Perl5 access to Berkeley DB version 1.x
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DB_File
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/DB_File-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 cbe5e90b0e40e0d566f505789b73196e93c56709f660ca316af50662260749a0
%global source0_file DB_File-1.860.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libdb-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Copy not needed if ExtUtils::Constant is available
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
# DynaLoader not needed if XSLoader is available
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
%if %{with perl_DB_File_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests:
# Data::Dumper not useful
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
%endif
Requires:       perl(Fcntl)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
DB_File is a module which allows Perl programs to make use of the facilities
provided by Berkeley DB version 1.x (if you have a newer version of DB, you
will be limited to functionality provided by interface of version 1.x). The
interface defined here mirrors the Berkeley DB interface closely.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(threads)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/DB_File-1.860.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cbe5e90b0e40e0d566f505789b73196e93c56709f660ca316af50662260749a0" || { echo "oreon: Source0 SHA256 mismatch for DB_File-1.860.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n DB_File-%{version}
find -type f -exec chmod -x {} +
perl -MConfig -pi -e 's|^#!.*perl|$Config{startperl}|' dbinfo

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/meta-*.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes dbinfo README
%{perl_vendorarch}/auto/DB_File*
%{perl_vendorarch}/DB_File*
%{_mandir}/man3/DB_File*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.860-1
- Prepare for Oreon 11 (RP1)
