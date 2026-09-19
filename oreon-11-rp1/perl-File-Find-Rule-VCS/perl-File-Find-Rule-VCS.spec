%global source0_hash 43c798bff0a1f6ac196cfa0f28eddac768954df2d02a04d01974a8fafeafbb49

Name:           perl-File-Find-Rule-VCS
Version:        1.09
Release:        8%{?dist}
Summary:        Exclude files/directories for Version Control Systems
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Find-Rule-VCS
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Find-Rule-VCS-%{version}.tar.gz
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
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Find::Rule) >= 0.20
BuildRequires:  perl(Text::Glob) >= 0.08
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.47

%description
Many tools need to be equally useful both on ordinary files, and on code
that has been checked out from revision control systems.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Find-Rule-VCS-%{version}
# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
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
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/File*
%{_mandir}/man3/File::Find::Rule::VCS*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
