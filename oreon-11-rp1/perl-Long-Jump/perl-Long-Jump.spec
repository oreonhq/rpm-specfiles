%global source0_hash 5b4aef1221dda3dd9708e7b8da73ffd8b8dbbcf571726ac6cfa1155a0c382064

Name:           perl-Long-Jump
Version:        0.000003
Release:        5%{?dist}
Summary:        Mechanism for returning to a specific point from a deeply nested stack
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Long-Jump
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Long-Jump-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Importer)
# Tests:
# Test2::V0 version from Test2::Suite in META
BuildRequires:  perl(Test2::V0) >= 0.000126

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}^}perl\\(Test2::V0\\)$

%description
This Perl module essentially provides a multi-level return. You can mark
a spot with setjump() and then unwind the stack back to that point from any
nested stack frame by name using longjump(). You can also provide a list of
return values. It is safer than C language jump in that it only lets you
escape frames by going up the stack, you cannot jump in other ways.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test2::V0) >= 0.000126
Requires:       perl(warnings)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Long-Jump-%{version}

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
%dir %{perl_vendorlib}/Long
%{perl_vendorlib}/Long/Jump.pm
%{_mandir}/man3/Long::Jump.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
