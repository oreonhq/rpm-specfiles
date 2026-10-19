%global source0_hash 9f252394775e23aa42c3176611e5930638ab528d5190110b4731aa5b0bf35a15
Name:           perl-LWP-Protocol-connect
Version:        6.09
Release:        33%{?dist}
Summary:        Provides HTTP CONNECT proxy support for LWP::UserAgent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Protocol-connect
Source0:        https://cpan.metacpan.org/authors/id/B/BE/BENNING/LWP-Protocol-connect-%{version}.tar.gz
Patch0:         LWP-Protocol-connect-6.09-Do-not-use-bin-env-in-shebangs.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The LWP::Protocol::connect module provides support for using HTTP and HTTPS
over a proxy via the HTTP CONNECT method.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n LWP-Protocol-connect-%{version}
# Remove author and release tests which are always skipped
rm t/author-*.t t/release-*.t t/empty-ca-bundle.crt
perl -i -ne 'print $_ unless m{^t/(?:(?:author|release)-.*\.t|empty-ca-bundle\.crt)}' MANIFEST
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
%files -n perl-LWP-Protocol-connect-tests -f %{oreon_filedir}/perl-LWP-Protocol-connect-tests.list

%changelog

%autochangelog
