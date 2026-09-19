%global source0_hash 962ffdc1c5470bf9e43413297724308e938cb9c9c02a9041d7cbd485b1ddfb13

Name:           perl-Net-Pcap
Version:        0.21
Release:        11%{?dist}
Summary:        Interface to pcap(3) LBL packet capture library

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Pcap
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/Net-Pcap-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
# ExtUtils::Constant || File::Copy
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
# Run-time:
BuildRequires:  perl(Carp)
# DynaLoader not used if XSLoader is available
BuildRequires:  perl(Exporter)
# Sys::Hostname not used at tests
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More) >= 0.45
# Optional tests:
# POE not usefull without POE::Component::Pcap
# POE::Component::Pcap not yet packaged
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::Exception)
# Test::Spelling not used
# Test::Portability::Files not used
# DynaLoader not used if XSLoader is available
Requires:  perl(XSLoader)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Utils\\)

%description
perl-Net-Pcap provides Perl bindings to the LBL pcap(3) library.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::Exception)
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Net-Pcap-%{version}

for f in README Changes ; do
  iconv -f iso-8859-1 -t utf-8 $f >$f.conv && mv -f $f.conv $f
done

chmod 0644 eg/*

# Help generators to recognize Perl scripts
for F in `find t -name *.t -o -name *.pl`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/pod*
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/distchk.t
cp -a macros.all funcs.txt %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%doc eg/ t/
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net
%{_mandir}/man?/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
