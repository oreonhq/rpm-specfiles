%global source0_hash abc21827eb8a513171bf7fdecefce9945132cb76db945036518291f607b1491f
%global base_version 0.280236
Name:           perl-ExtUtils-CBuilder
Epoch:          1
Version:        0.280242
Release:        521%{?dist}
Summary:        Compile and link C code for Perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-CBuilder
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/ExtUtils-CBuilder-0.280236.tar.gz
Patch0:         ExtUtils-CBuilder-0.280230-Link-XS-modules-to-libperl.so-with-EU-CBuilder-on-Li.patch
Patch1:         ExtUtils-CBuilder-0.280236-Upgrade-to-0.280238.patch
Patch2:         ExtUtils-CBuilder-0.280238-Upgrade-to-0.280240.patch
Patch3:         ExtUtils-CBuilder-0.280240-Upgrade-to-0.280242.patch
BuildArch:      noarch
Requires:       gcc
Requires:       gcc-c++
Requires:       perl-devel
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::Mksymlists) >= 6.30
Requires:       perl(File::Spec) >= 3.13
Requires:       perl(Perl::OSType) >= 1
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((File::Spec|Perl::OSType)\\)$
Provides:       perl(ExtUtils::CBuilder)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was motivated
by the Module::Build project, but may be useful for other purposes as well.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n ExtUtils-CBuilder-%{base_version}

# Normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-ExtUtils-CBuilder-tests -f %{oreon_filedir}/perl-ExtUtils-CBuilder-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.280242-521
- Prepare for Oreon 11 (RP1)
