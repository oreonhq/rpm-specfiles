%global source0_hash ee9f39055dc695aa244a252f56ffd37f8be07209b337ad387824721206d2a89e

Name:           perl-Tie-Handle-Offset
Version:        0.004
Release:        24%{?dist}
Summary:        Tied handle that hides the beginning of a file
License:        Apache-2.0
URL:            https://metacpan.org/release/Tie-Handle-Offset
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Tie-Handle-Offset-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Tie::Handle)
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(warnings)

%description
This modules provides a file handle that hides the beginning of a file.
After opening, the file is positioned at the offset location. seek() and
tell() calls are modified to preserve the offset.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-Handle-Offset-%{version}

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
%doc Changes CONTRIBUTING.mkdn README
%dir %{perl_vendorlib}/Tie
%dir %{perl_vendorlib}/Tie/Handle
%{perl_vendorlib}/Tie/Handle/Offset.pm
%{perl_vendorlib}/Tie/Handle/SkipHeader.pm
%{_mandir}/man3/Tie::Handle::Offset.*
%{_mandir}/man3/Tie::Handle::SkipHeader.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
