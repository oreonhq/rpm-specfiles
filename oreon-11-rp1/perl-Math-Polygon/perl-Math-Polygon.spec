%global source0_hash 6c403bad7c0a61b4d7c86736aaeb76789ae432fa7a864c147e160f3d552afa53

Name:           perl-Math-Polygon
Version:        2.00
Release:        2%{?dist}
Summary:        Maintaining polygon data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Polygon
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Math-Polygon-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util) >= 1.13
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(Scalar::Util) >= 1.13

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test::More)\\)$

%description
These Perl modules provide basic transformations on two-dimensional polygons
in pure Perl.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.47

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Polygon-%{version}
chmod a+x t/*.t

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
%doc ChangeLog README README.md
%dir %{perl_vendorlib}/Math
%{perl_vendorlib}/Math/Polygon{,.pm,.pod}
%{_mandir}/man3/Math::Polygon{.,::}*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
