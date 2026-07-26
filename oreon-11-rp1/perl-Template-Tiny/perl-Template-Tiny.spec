%global source0_hash cea4735220af81c72943dea70465a83f61beb499a2a2ba67ea55762e1cd8060e

Name:           perl-Template-Tiny
Version:        1.16
Release:        3%{?dist}
Summary:        Template Toolkit re-implemented in as little code as possible
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Tiny
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Template-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(vars)

%description
WARNING: THIS MODULE IS EXPERIMENTAL AND SUBJECT TO CHANGE WITHOUT NOTICE
Template::Tiny is a re-implementation of a partial subset of the Template 
Toolkit,  in as few lines of code as possible. It is intended for use in 
light-usage, low-memory, or low-CPU templating situations, where you may 
need to upgrade to the full feature set in the future, or if you want the 
familiarity of TT-style templates. It is intended to have fully-compatible 
template and stash usage, with a limited by similar Perl API. Unlike 
Template Toolkit, Template::Tiny will process templates without a compile 
phase (but despite this is still quicker, owing to heavy use of the Perl 
regular expression engine.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Tiny-%{version}

# Help file to recognise the Perl scripts
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
