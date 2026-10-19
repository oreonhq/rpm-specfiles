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
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Win32::Console::ANSI\\)$
Provides:       perl(Spellunker)
Provides:       perl(Test::Spellunker)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Simple::Methody)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(open)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
