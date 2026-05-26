Name:           perl-Pod-LaTeX
Version:        0.61
Release:        326%{?dist}
Summary:        Convert POD data to formatted LaTeX
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-LaTeX
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJENNESS/Pod-LaTeX-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 15a840ea1c8a76cd3c865fbbf2fec33b03615c0daa50f9c800c54e0cf0659d46
%global source0_file Pod-LaTeX-0.61.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(Pod::ParseUtils) >= 0.3
BuildRequires:  perl(Pod::Select)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(deprecate)
Requires:       perl(Pod::ParseUtils) >= 0.3

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::ParseUtils\\)$

%description
Pod::LaTeX is a module to convert documentation in the POD format into
LaTeX. A pod2latex replacement command is provided.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Pod-LaTeX-0.61.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "15a840ea1c8a76cd3c865fbbf2fec33b03615c0daa50f9c800c54e0cf0659d46" || { echo "oreon: Source0 SHA256 mismatch for Pod-LaTeX-0.61.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Pod-LaTeX-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -fr %{buildroot}%{_libexecdir}/%{name}/t/misc
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Test t/pod2latex.t and t/user.t write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc ChangeLog README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.61-326
- Prepare for Oreon 11 (RP1)
