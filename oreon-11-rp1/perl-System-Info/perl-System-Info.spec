%global source0_hash 84268b8040254fb209779296a871ebde07d907b8acf3320bcb2f65f12c5a3d0f

Name:           perl-System-Info
Version:        0.067
Release:        1%{?dist}
Summary:        Factory for system specific information objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/System-Info
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/System-Info-%{version}.tgz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
#BuildRequires:  perl(Haiku::SysInfo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)

%description
System::Info tries to present system-related information, like number of
CPU's, architecture, OS and release related information in a system-
independent way. This releases the user of this module of the need to know
if the information comes from Windows, Linux, HP-UX, AIX, Solaris, Irix, or
VMS, and if the architecture is i386, x64, pa-risc2, or arm.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n System-Info-%{version}
chmod -x examples/*

# Help generators to recognize Perl scripts
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc ChangeLog CONTRIBUTING.md examples README SECURITY.md
%dir %{perl_vendorlib}/System
%{perl_vendorlib}/System/Info*
%{_mandir}/man3/System::Info*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
