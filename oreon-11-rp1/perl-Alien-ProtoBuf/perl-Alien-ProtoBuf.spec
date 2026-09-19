%global source0_hash e9fcef5b8dba8c05110d89b457ab83eb0e85fa23cb8316de5a0526e2adcac712

Name:           perl-Alien-ProtoBuf
Version:        0.09
Release:        28%{?dist}
Summary:        Find Protocol Buffers library
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-ProtoBuf
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/Alien-ProtoBuf-%{version}.tar.gz
# Although Alien::* modules are usually architecture specific because they
# store architecture specific data, this is not a case of
# perl-Alien-ProtoBuf. We can remain noarch.
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Alien::Base::ModuleBuild) >= 0.023
BuildRequires:  perl(lib)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.11
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(protobuf)
# Run-time:
BuildRequires:  perl(Alien::Base)
# Tests:
BuildRequires:  perl(Test::More)
# Test::Pod not used
Requires:       perl(Data::Dumper)
Requires:       perl(Module::Build) >= 0.28
# A purpose of this package is to ensure a user can develop against protobuf.
# We require exact version because the version is stored into generated
# Alien/ProtoBuf/Install/Files.pm file.
Requires:       pkgconfig(protobuf) = %(type -p pkgconf >/dev/null && pkgconf --exists protobuf && pkg-config --modversion protobuf || echo 0)

%description
Depending on Alien::ProtoBuf Perl module ensures the Protocol Buffers library
is installed on your system.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-ProtoBuf-%{version}
# Remove author tests
rm t/author-pod-syntax.t
perl -i -ne 'print $_ unless m{^t/author-pod-syntax\.t}' MANIFEST
# Normalize permissions
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
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
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
