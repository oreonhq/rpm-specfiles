%global source0_hash 9fa2953f7185795eb3ec4020d19adb75ab61fd58f435a9229bee727e91d459a3

Name:           perl-XML-Namespace
Version:        0.02
Release:        32%{?dist}
Summary:        Simple support for XML name spaces
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Namespace
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABW/XML-Namespace-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

%description
This Perl module implements a simple object for representing XML name spaces
in Perl. It provides little more than some syntactic sugar for your Perl
programs, saving you the bother of typing lots of long-winded URIs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Namespace-%{version}
chmod +x t/*.t

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
%doc README
%dir %{perl_vendorlib}/XML
%{perl_vendorlib}/XML/Namespace.pm
%{_mandir}/man3/XML::Namespace.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
