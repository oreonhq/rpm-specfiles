%global source0_hash ab4f6ba451f717c96122f44030cd0228d25293aaa7fb232985fe4aedb450e024
Name:           perl-Object-HashBase
Version:        0.018
Release:        1%{?dist}
Summary:        Build hash-based classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-HashBase
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Object-HashBase-%{version}.tar.gz
Patch0:         Object-HashBase-0.008-Normalize-shebang.patch
BuildArch:      noarch
Suggests:       perl(Class::XSAccessor)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Object::HashBase::Test::HBase.*
%global __requires_exclude %{__requires_exclude}|^perl\\(My::Prefix::HashBase\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Object-HashBase-tests -f %{oreon_filedir}/perl-Object-HashBase-tests.list
%files -n perl-Object-HashBase-tools -f %{oreon_filedir}/perl-Object-HashBase-tools.list

%changelog

%autochangelog
