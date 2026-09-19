%global source0_hash b73cbdd4202b29eab97e0c08dcd59d9273633610e8721cf449078656bd591a7c

Name:           perl-Parallel-Pipes
Version:        0.201
Release:        3%{?dist}
Summary:        Parallel processing using pipes for communication and synchronization
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parallel-Pipes
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/Parallel-Pipes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Time::HiRes)

%description
Parallel::Pipes tries to solve problems of parallel processing for
communication and synchronization by using pipe(2) and select(2).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parallel-Pipes-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
