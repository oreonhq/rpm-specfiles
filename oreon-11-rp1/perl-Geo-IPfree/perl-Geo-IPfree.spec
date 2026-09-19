%global source0_hash 1ff0a2ab25930af66d8ab5db68dcb820efdbae75941670e0ece68b53280ef5e9

# Perform optional tests
%bcond_without perl_Geo_IPfree_enables_optional_test

%global cpan_name Geo-IPfree
%global cpan_version 1.160001
%global cpan_author ATOOMIC
Name:           perl-%{cpan_name}
# Normalize version to dotted format
Version:        %(echo '%{cpan_version}' | sed 's/\(\....\)\(.\)/\1.\2/')
Release:        1%{?dist}
Summary:        Look up the country of an IPv4 Address
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/%(echo '%{cpan_author}' | sed 's=\(.\)\(.\)=\1/\1\2/\1\2=')/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Socket not used at tests
# Tests only:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
%if %{with perl_Geo_IPfree_enables_optional_test}
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
Requires:       perl(Socket)

%description
This package comes with it's own database to look up the IPv4's country, and
is totally free.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{cpan_name}-%{cpan_version}
%if !%{with perl_Geo_IPfree_enables_optional_test}
for F in t/pod.t t/pod_coverage.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
%endif
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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Geo_IPfree_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t \
    %{buildroot}%{_libexecdir}/%{name}/t/pod_coverage.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes misc README
%dir %{perl_vendorlib}/Geo
%{perl_vendorlib}/Geo/IPfree.pm
%{perl_vendorlib}/Geo/IPfree.pod
%{perl_vendorlib}/Geo/ipscountry.dat
%{_mandir}/man3/Geo::IPfree.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
