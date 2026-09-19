%global source0_hash c33db44790aa8d254147882e2378dffe970ad60331350bde062d17953482b1b7

%global pkgname Data-MessagePack

Name:           perl-Data-MessagePack
Version:        1.02
Release:        14%{?dist}
Summary:        MessagePack serialising/deserialising
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-MessagePack
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYOHEX/%{pkgname}-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
#BuildRequires:  perl(Devel::PPPort) >= 3.42
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(vars)
BuildRequires:  perl(Module::Build::XSUtil)
BuildRequires:  perl(overload)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Math::BigInt) >= 1.89
BuildRequires:  perl(overload)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(if)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
# Optional tests
BuildRequires:  perl(threads)

Requires:       perl(XSLoader)

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(t::Util\\)

%description
This module converts Perl data structures to MessagePack and vice versa.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
