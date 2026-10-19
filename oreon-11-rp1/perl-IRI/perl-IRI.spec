%global source0_hash 5c024975f2a6c20b50fc2b31fe36cc276ffd53960dfbc9b0517552bc8866da00
Name:           perl-IRI
Version:        0.013
Release:        1%{?dist}
Summary:        Internationalized Resource Identifiers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IRI
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/IRI-%{version}.tar.gz
Patch0:         IRI-0.011-Disable-author-features.patch
BuildArch:      noarch
Requires:       perl(Types::Standard) >= 0.008
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test::More|Types::Standard)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::HandlesVia)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The IRI module provides an object representation for Internationalized
Resource Identifiers (IRIs) as defined by RFC 3987 and supports their
parsing, serializing, and base resolution.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n IRI-%{version}
# Remove bundled modules
rm -rf inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Correct permissions
chmod +x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-IRI-tests -f %{oreon_filedir}/perl-IRI-tests.list

%changelog

%autochangelog
