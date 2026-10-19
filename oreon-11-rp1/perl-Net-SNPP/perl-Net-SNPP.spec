%global source0_hash 06b851d64596625e866359fb017dd0d08973e0ebc50c323f4a1d50ecdd868e76
Name:           perl-Net-SNPP
Version:        1.17
Release:        55%{?dist}
Summary:        Perl modules for the Simple Network Pager Protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-SNPP
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBEYA/Net-SNPP-%{version}.tar.gz
Patch0:         Net-SNPP-1.17-Define-dummy-Net-SNPP-Server-timeout.patch
Patch1:         Net-SNPP-1.17-Convert-README-to-UTF-8.patch
BuildArch:      noarch
Requires:       perl(Net::Cmd) >= 0.01
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Net::Cmd|Socket)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Net::Cmd)
BuildRequires:  perl(Net::Config)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Perl client and server modules for the Simple Network Pager Protocol,
as described in RFC 1861.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-SNPP-%{version}
%patch -P0 -p1
%patch -P1 -p1
chmod a-x README
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-SNPP-tests -f %{oreon_filedir}/perl-Net-SNPP-tests.list

%changelog

%autochangelog
