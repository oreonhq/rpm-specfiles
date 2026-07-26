%global source0_hash 750c3a79d8e1824758a6ef7d2dd077dcddca503542b8c34eccd5acbb779dc423

Name:           perl-Pod-Elemental
Version:        0.103006
Release:        9%{?dist}
Summary:        Work with nestable Pod elements
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Elemental
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Pod-Elemental-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Encode)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Mixin::Linewise::Readers)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role) >= 0.90
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Pod::Eventual::Simple) >= 0.004
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(String::Truncate)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::ForMethods)
BuildRequires:  perl(utf8)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.88

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moose::Role\\)$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
Pod::Elemental is a system for treating a Pod (plain old documentation)
documents as trees of elements. This model may be familiar from many other
document systems, especially the HTML DOM. Pod::Elemental's document object
model is much less sophisticated than the HTML DOM, but still makes a lot
of document transformations easy.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Elemental-%{version}
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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
