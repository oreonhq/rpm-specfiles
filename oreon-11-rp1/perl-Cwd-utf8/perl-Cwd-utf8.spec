%global source0_hash 2c2f8b582a84d68d18ec5bb4f6b5e2d898ff29a3807098a1a7a4273dea91890a

Name:           perl-Cwd-utf8
Version:        0.014
Release:        1%{?dist}
Summary:        Fully UTF-8 aware Cwd
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Cwd-utf8
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAYOBAAN/Cwd-utf8-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warn)
Requires:       perl(Exporter)

%description
While the original Cwd functions are capable of handling UTF-8 quite well,
they expects and return all data as bytes, not as characters. This Cwd::utf8
Perl module replaces all the Cwd functions with fully UTF-8 aware versions,
both expecting and returning characters.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Cwd-utf8-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
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
%dir %{perl_vendorlib}/Cwd
%{perl_vendorlib}/Cwd/utf8.pm
%{_mandir}/man3/Cwd::utf8.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
