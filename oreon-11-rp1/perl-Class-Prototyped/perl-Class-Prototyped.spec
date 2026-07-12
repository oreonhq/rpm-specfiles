%global source0_hash 348d60938445f174cdbc56147393411a164e286abb680c8d30832019e9063a82

Name:           perl-Class-Prototyped
Version:        1.16
Release:        4%{?dist}
Summary:        Fast prototype-based OO programming in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Prototyped
Source0:        https://cpan.metacpan.org/authors/id/T/TE/TEVERETT/Class-Prototyped-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(Carp)
# GraphViz not used for tests
# IO::File not used for tests
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)

%{?perl_default_filter}

Provides:       perl(Class::Prototyped)
%description
This package provides for efficient and simple prototype-based programming
in Perl. You can provide different subroutines for each object, and also
have objects inherit their behavior and state from another object.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Class-Prototyped-%{version}
# Documentation and libraries should not be executable
chmod -x perf/* examples/* Changes lib/Class/*.pm lib/Class/Prototyped/*

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
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
./Build test

%files
%doc Changes README perf/ examples/
%dir %{perl_vendorlib}/Class
%{perl_vendorlib}/Class/Prototyped
%{perl_vendorlib}/Class/Prototyped.pm
%{_mandir}/man3/Class::Prototyped.*
%{_mandir}/man3/Class::Prototyped::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
