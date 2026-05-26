%global base_version 5.78

Name:           perl-Exporter
Version:        5.79
Release:        521%{?dist}
Summary:        Implements default import method for modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Exporter
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Exporter-%{base_version}.tar.gz
# Upgrade to 5.79 based on perl-5.42.0
Patch0:         Exporter-5.78-Upgrade-to-5.79.patch
# oreon url source checksums begin
%global source0_sha256 bd17e99219aa2fb6a8acb3d11deffcb588708c70fc29f346e20ea7f71d3a48f0
%global source0_file Exporter-5.78.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp) >= 1.05
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(vars)
Requires:       perl(Carp) >= 1.05
Requires:       perl(warnings)

%description
The Exporter module implements an import method which allows a module to
export functions and variables to its users' name spaces. Many modules use
Exporter rather than implementing their own import method because Exporter
provides a highly flexible interface, with an implementation optimized for
the common case.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Exporter-5.78.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bd17e99219aa2fb6a8acb3d11deffcb588708c70fc29f346e20ea7f71d3a48f0" || { echo "oreon: Source0 SHA256 mismatch for Exporter-5.78.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Exporter-%{base_version}
%patch -P0 -p1

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
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
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{perl_vendorlib}/Exporter*
%{_mandir}/man3/Exporter*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.79-521
- Prepare for Oreon 11 (RP1)
