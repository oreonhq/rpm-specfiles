%global source0_hash 57900b684bb00b54b8cf72cc1738258563b6216d4eff972e0d93393e4a520781

Name:           perl-grpc-xs
Version:        0.38
Release:        10%{?dist}
Summary:        Perl binding to a client part of the gRPC library
# examples/route_guide/route_guide.proto:   BSD-3-Clause
# LICENSE:      Apache-2.0 text
# ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
License:        Apache-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
URL:            https://metacpan.org/dist/grpc-xs
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JOYREX/grpc-xs-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  grpc-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

%description
This is a low-level binding to a client part of the gRPC library.

%package tests
Summary:        Tests for %{name}
License:        Apache-2.0
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Grpc-XS-%{version} -p1
# Fix shebangs in examples
perl -MConfig -i -p -e 's/^#!perl\b/$Config{startperl}/' examples/*/t/*.t
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
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
%doc examples README.md
%dir %{perl_vendorarch}/auto/Grpc
%{perl_vendorarch}/auto/Grpc/XS
%dir %{perl_vendorarch}/Grpc
%{perl_vendorarch}/Grpc/Client
%{perl_vendorarch}/Grpc/Constants.pm
%{perl_vendorarch}/Grpc/XS
%{perl_vendorarch}/Grpc/XS.pm
%{_mandir}/man3/Grpc::XS.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
