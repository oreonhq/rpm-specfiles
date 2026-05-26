Name:           perl-perlfaq
Version:        5.20250619
Release:        521%{?dist}
Summary:        Frequently asked questions about Perl
# Code examples are Public Domain
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Public-Domain
URL:            https://metacpan.org/release/perlfaq
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/perlfaq-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 eed03a887f21e2bede71c07645357a26cabde487365ac17fa3366baaeb0ea8d6
%global source0_file perlfaq-5.20250619.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Conflicts:      perl < 4:5.22.0-347

%description
The perlfaq comprises several documents that answer the most commonly asked
questions about Perl and Perl programming.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/perlfaq-5.20250619.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "eed03a887f21e2bede71c07645357a26cabde487365ac17fa3366baaeb0ea8d6" || { echo "oreon: Source0 SHA256 mismatch for perlfaq-5.20250619.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n perlfaq-%{version}

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
%doc Changes README
%{perl_vendorlib}/perlfaq*
%{perl_vendorlib}/perlglossary*
%{_mandir}/man3/perlfaq*
%{_mandir}/man3/perlglossary*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.20250619-521
- Import
