%global source0_hash e9fcef5b8dba8c05110d89b457ab83eb0e85fa23cb8316de5a0526e2adcac712
Name:           perl-Alien-ProtoBuf
Version:        0.09
Release:        1%{?dist}
Summary:        Find Protocol Buffers library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-ProtoBuf
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/Alien-ProtoBuf-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(Module::Build) >= 0.28
Requires:       pkgconfig(protobuf) = %(type -p pkgconf >/dev/null && pkgconf --exists protobuf && pkg-config --modversion protobuf || echo 0)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Alien::Base)
BuildRequires:  perl(Alien::Base::ModuleBuild)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(protobuf)
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-ProtoBuf-tests -f %{oreon_filedir}/perl-Alien-ProtoBuf-tests.list

%changelog

%autochangelog
