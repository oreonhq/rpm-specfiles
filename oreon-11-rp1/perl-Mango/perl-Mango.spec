%global source0_hash e85034967447fe10ac16ddf2d2ddd4fac8cf0a8579d45b656ef55d8728f0d579

Name:           perl-Mango
Version:        1.30
Release:        26%{?dist}
Summary:        Pure-Perl non-blocking I/O MongoDB driver
License:        Artistic-2.0
URL:            https://metacpan.org/release/Mango
Source0:        https://cpan.metacpan.org/authors/id/O/OD/ODC/Mango-%{version}.tar.gz
# Adjust to the changes in Mojolicious 8.50, bug #1843866,
# proposed to an upstream <https://github.com/oliwer/mango/issues/36>
Patch0:         Mango-1.30-Disable-unicode_strings-when-working-with-regular-ex.patch
# Do not use Mojo::IOLoop::Delay removed in Mojolicous 9, bug #1958432,
# <https://github.com/oliwer/mango/issues/38>. Fix borrowed from
# <https://github.com/fortl/mango> fork.
Patch1:         Mango-1.30-fix-atomicity-of-authetication-errors-while-high-con.patch
Patch2:         Mango-1.30-fix-Mojolicious-8-support-don-t-use-event-loop-singl.patch
BuildArch:      noarch
BuildRequires:  make
# This code is architecture-independent, but it requires at least 64-bit
# integers and these are not available on 32-bit architectures if perl is
# built without use64bitint option. We enabled use64bitint in 4:5.26.0-392.
BuildRequires:  perl-libs >= 4:5.26.0-392
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Authen::SCRAM::Client not used at tests
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Date)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
# Mojolicious version from META because this is the only versioned module in
# perl-Mojolicious RPM package
BuildRequires:  perl(Mojolicious) >= 5.40
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Mojo::IOLoop::Server)
BuildRequires:  perl(Test::More)
# Optional tests:
# Test::Pod 1.14 not used
# Test::Pod::Coverage 1.04 not used
Requires:       perl(Authen::SCRAM::Client)
Requires:       perl(Mojo::EventEmitter)
# Mojolicious version from META because this is the only versioned module in
# perl-Mojolicious RPM package
Requires:       perl(Mojolicious) >= 5.40
# This code is architecture-independent, but it requires at least 64-bit
# integers and these are not available on 32-bit architectures if perl is
# built without use64bitint option. We enabled use64bitint in 4:5.26.0-392.
Requires:       perl-libs >= 4:5.26.0-392

%description
Mango is a pure-Perl non-blocking I/O MongoDB driver, optimized for use
with the Mojolicious real-time web framework, and with multiple event loop
support. Since MongoDB is still changing rapidly, only the latest stable
version is supported.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(feature)
Requires:       perl(Mango::Auth)
Requires:       perl(warnings)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mango-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Help generators to recognize Perl scripts
for F in $(find t -type f -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset TEST_ONLINE TEST_POD
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset TEST_ONLINE TEST_POD
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
