%global source0_hash 4134533716d87af8fff56e250c488ad06df0a7bff48e7cf7de63ff6bc8d9c17f

Name:           perl-bareword-filehandles
Version:        0.007
Release:        24%{?dist}
Summary:        Disables bareword filehandles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/bareword-filehandles
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/bareword-filehandles-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
# B::Hooks::OP::Check is examined by ExtUtils::Depends from Makefile.PL
BuildRequires:  perl(B::Hooks::OP::Check)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(if)
# Lexical::SealRequireHints not used on Perl >= 5.12
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

Provides:       perl(bareword::filehandles)
%description
This module lexically disables the use of bareword filehandles with built-in
functions, except for the special built-in filehandles STDIN, STDOUT,
STDERR, ARGV, ARGVOUT and DATA.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n bareword-filehandles-%{version}
# Fix shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
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
%dir %{perl_vendorarch}/auto/bareword
%{perl_vendorarch}/auto/bareword/filehandles
%dir %{perl_vendorarch}/bareword
%{perl_vendorarch}/bareword/filehandles.pm
%{_mandir}/man3/bareword::filehandles.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
