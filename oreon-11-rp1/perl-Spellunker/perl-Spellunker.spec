%global source0_hash 9ca19f3b65b7acd8da72dbb8f70ada6e875aa7bffc20b0b7e6eb6b109d3a8c9d

Name:           perl-Spellunker
Version:        0.4.0
Release:        34%{?dist}
Summary:        Pure perl spelling checker implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Spellunker
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Spellunker-v0.4.0.tar.gz
Patch10:        Spellunker-v0.4.0-Remove-usr-bin-env-from-shebang.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Simple::Methody)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(version)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.96
# Dependencies
# (none)

%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Win32::Console::ANSI\\)$

Provides:       perl(Spellunker)
Provides:       perl(Test::Spellunker)
%description
%{summary}, also usable as a library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Spellunker-v%{version}

# Fix shellbangs in shipped scripts
%patch -P 10 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{_bindir}/spellunker
%{_bindir}/spellunker-pod
%{perl_vendorlib}/Spellunker.pm
%{perl_vendorlib}/Spellunker/
%{perl_vendorlib}/Test/
%{perl_vendorlib}/auto/share/dist/Spellunker/
%{_mandir}/man1/spellunker.1*
%{_mandir}/man1/spellunker-pod.1*
%{_mandir}/man3/Spellunker.3*
%{_mandir}/man3/Test::Spellunker.3*

%changelog
%autochangelog
