Name:           perl-Object-HashBase
Version:        0.015
Release:        4%{?dist}
Summary:        Build hash-based classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-HashBase
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Object-HashBase-%{version}.tar.gz
# Correct shebangs
Patch0:         Object-HashBase-0.008-Normalize-shebang.patch
# oreon url source checksums begin
%global source0_sha256 18f70c6eddf44b19f36c190b6747b35b43198c394b0a36c6dd63946ff1a11d0a
%global source0_file Object-HashBase-0.015.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Temp)
Suggests:       perl(Class::XSAccessor)

# Remove under-specified dependenices
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(Object::HashBase::Test::HBase.*
%global __requires_exclude %{__requires_exclude}|^perl\\(My::Prefix::HashBase\\)$

%description
This package is used to generate classes based on hash references. Using this
class will give you a new() method, as well as generating accessors you
request.  Generated accessors will be getters, set_ACCESSOR setters will also
be generated for you. You also get constants for each accessor (all caps)
which return the key into the hash for that accessor. Single inheritance is
also supported.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%package tools
Summary:        Generate inlined Object::HashBase Perl module
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Test::More) >= 0.98

%description tools
hashbase_inc.pl script generates a Perl module that contains
a Object::HashBase module mangled into a name space of your choice. It can
also generate the tests for it.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Object-HashBase-0.015.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "18f70c6eddf44b19f36c190b6747b35b43198c394b0a36c6dd63946ff1a11d0a" || { echo "oreon: Source0 SHA256 mismatch for Object-HashBase-0.015.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Object-HashBase-%{version}
%patch -P0 -p1
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Object/HashBase
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%files tools
%{_bindir}/hashbase_inc.pl
%{perl_vendorlib}/Object/HashBase

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.015-4
- Prepare for Oreon 11 (RP1)
