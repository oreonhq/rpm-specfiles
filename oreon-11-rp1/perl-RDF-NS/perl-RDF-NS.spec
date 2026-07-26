%global source0_hash 5856312dfda8852b10e9354b9565f506c1ff284e9c2349c9cb2d6d821bc66a5d

Name:           perl-RDF-NS
Version:        20230619
Release:        8%{?dist}
Summary:        Popular RDF name space prefixes from prefix.cc
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RDF-NS
Source0:        https://cpan.metacpan.org/authors/id/V/VO/VOJ/RDF-NS-%{version}.tar.gz
# Fix shell bang
Patch0:         RDF-NS-20160409-Do-not-use-usr-bin-env.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(RDF::Trine::Node::Blank)
BuildRequires:  perl(RDF::Trine::Node::Resource)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
# Optional tests:
BuildRequires:  perl(RDF::Trine)
Requires:       perl(File::ShareDir) >= 1.00

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::ShareDir\\)$

%description
Hard-coding URI name spaces and prefixes for RDF applications is neither
fun nor maintainable. In the end we all use more or less the same
prefix definitions, as collected at <http://prefix.cc/>. This Perl module
includes all these prefixes as defined at specific snapshots in time.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(RDF::NS::Trine)
Requires:       perl(RDF::NS::URIS)
Requires:       perl(RDF::Trine)
Requires:       perl(URI)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n RDF-NS-%{version}
chmod -x lib/App/rdfns.pm
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

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
%doc Changes README.md
%{_bindir}/rdfns
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/rdfns.pm
%dir %{perl_vendorlib}/RDF
%dir %{perl_vendorlib}/auto
%dir %{perl_vendorlib}/auto/share
%dir %{perl_vendorlib}/auto/share/dist
%{perl_vendorlib}/auto/share/dist/RDF-NS
%{perl_vendorlib}/RDF/NS
%{perl_vendorlib}/RDF/NS.pm
%{perl_vendorlib}/RDF/SN.pm
%{_mandir}/man1/rdfns.*
%{_mandir}/man3/App::rdfns.*
%{_mandir}/man3/RDF::NS.*
%{_mandir}/man3/RDF::NS::*
%{_mandir}/man3/RDF::SN.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
