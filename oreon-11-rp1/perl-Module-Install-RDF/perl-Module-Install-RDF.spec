%global source0_hash 9857bcf2e64400339bdedd8c01598cec6a39b6ebedfcf2297aab553547cd027a
Name:           perl-Module-Install-RDF
Version:        0.009
Release:        29%{?dist}
Summary:        Advanced meta-data for your distribution
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND CC-BY-SA-2.0-UK
URL:            https://metacpan.org/release/Module-Install-RDF
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-RDF-%{version}.tar.gz
Patch0:         Module-Install-RDF-0.009-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
Requires:       perl(Module::Install::Base) >= 1.0
Requires:       perl(RDF::Trine) >= 0.135
Requires:       perl(RDF::TrineX::Parser::Pretdsl)
Requires:       perl(URI::file) >= 4.0
Requires:       perl(warnings)
Suggests:       perl(RDF::TrineX::Serializer::MockTurtleSoup)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::Install::Base|RDF::Trine|Test::More|URI::file)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Object::ID)
BuildRequires:  perl(RDF::Trine)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
These Perl modules read all the RDF files it can find in the distribution's
"meta" directory and expose them for other modules to make use of them. They
also allow you to write out a combined graph using Turtle.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.61
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Module-Install-RDF-%{version}
# Remove bundled modules.
# And remove inc/Module/Package/Dist/RDF.pm because it's a 
# Module::Package::RDF plug-in that run-depends on this (Module::Install::RDF)
# package. Fortunatelly, the inc/Module/Package/Dist/RDF.pm is not good for
# anything so the patch makes not to load it.
rm -r ./inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-Install-RDF-tests -f %{oreon_filedir}/perl-Module-Install-RDF-tests.list

%changelog

%autochangelog
