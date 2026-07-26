%global source0_hash 6ed25cf987fe8b0f06e9c43b824f8cd0326de4938bbf10b4309632c73d0faf60

Name:           perl-Config-INI-Reader-Multiline
Version:        1.002
Release:        1%{?dist}
Summary:        Parser for INI files with line continuations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-INI-Reader-Multiline
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/Config-INI-Reader-Multiline-%{version}.tar.gz
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
# Run-time:
BuildRequires:  perl(Config::INI::Reader) >= 0.024
# Tests:
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)

%description
The Config::INI::Reader::Multiline Perl module is a subclass of
Config::INI::Reader that offers support for line continuations, i.e. adding
a backslash-newline at the end of a line to indicate the newline should be
removed from the input stream and ignored.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(blib) >= 1.01

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-INI-Reader-Multiline-%{version}
# Remove always skipped tests
for F in t/author-distmeta.t t/author-pod-coverage.t t/author-pod-syntax.t; do
    rm -- "$F";
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' MANIFEST
done
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
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Config
%dir %{perl_vendorlib}/Config/INI
%dir %{perl_vendorlib}/Config/INI/Reader
%{perl_vendorlib}/Config/INI/Reader/Multiline.pm
%{_mandir}/man3/Config::INI::Reader::Multiline.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
