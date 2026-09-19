%global source0_hash 595d2bf27e4e7791085d8f92d666634925433a0763a214e1ffbce0a128723ffd

Name:       perl-rpm-build-perl 
Version:    0.82
Release:    51%{?dist}
# ConstOptree/ConstOptree.pm:   GPL-2.0-or-later
# lib/B/Clobbers.pm:            GPL-2.0-or-later
# lib/B/PerlReq.pm:             GPL-2.0-or-later
# lib/B/Walker.pm:              GPL-2.0-or-later
# lib/PerlReq/Utils.pm:         LGPL-2.0-or-later
# perl.prov:        LGPL-2.0-or-later
# perl.prov.files:  GPL-2.0-or-later
# perl.req:         LGPL-2.0-or-later
# perl.req.files:   GPL-2.0-or-later
# README:       GPL-2.0-or-later
## Added with Port-to-OpSIBLING-like-macros-required-since-Perl-5..patch
# ConstOptree/ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
License:    GPL-2.0-or-later AND LGPL-2.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
Summary:    Perl compiler back-end to extract Perl dependencies 
Url:        https://metacpan.org/release/rpm-build-perl
Source:     https://cpan.metacpan.org/authors/id/A/AT/ATOURBIN/rpm-build-perl-%{version}.tar.gz 
# Perl 5.18 compatibility, CPAN RT#85411
Patch0:     rpm-build-perl-0.82-Fix-non-deterministic-failures-on-newer-perls.patch
# Perl 5.22 compatibility, bug #1231258, CPAN RT#104885
Patch1:     rpm-build-perl-0.82-Adjust-to-perl-5.22.patch
# Perl 5.26 compatibility, CPAN RT#117350
Patch2:     rpm-build-perl-0.82-Port-to-OpSIBLING-like-macros-required-since-Perl-5..patch
# Perl 5.36 compatibility, CPAN RT#142772
Patch3:     rpm-build-perl-0.82-Adapt-tests-to-Perl-5.35.12.patch
# Perl 5.38 compatibility, bug #2222640, CPAN RT#148982
Patch4:     rpm-build-perl-0.82-Adjust-to-Perl-5.38.0.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(version)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(attributes)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(autouse)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(dumpvar.pl)
BuildRequires:  perl(encoding)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
Requires:       perl(Carp)
Requires:       perl(Encode)
Requires:       perl(version)

%{?perl_default_filter}
# Do not export private modules
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(fake\\)

%description
B::PerlReq is a back-end module for the Perl compiler that extracts
dependencies from Perl source code, based on the internal compiled
structure that Perl itself creates after parsing a program. The output of
B::PerlReq is suitable for automatic dependency tracking (e.g. for RPM
packaging).

%package scripts
Summary:        Perl RPM prov/req scripts
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description scripts
The provides/requires scripts packaged along with perl-rpm-build-perl.

%package tests
Summary:        Tests for %{name}
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-scripts = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(attributes)
Requires:       perl(AutoLoader)
Requires:       perl(autouse)
Requires:       perl(base)
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(dumpvar.pl)
Requires:       perl(encoding)
Requires:       perl(fields)
Requires:       perl(File::Basename)
Requires:       perl(File::Glob)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
Requires:       perl(POSIX)
Requires:       perl(Socket)
Requires:       perl(Tie::Hash)
Requires:       perl(Tie::StdHash)
Requires:       perl(Try::Tiny)
Requires:       perl(utf8)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rpm-build-perl-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Adjust paths to executed scripts
perl -i -pe 's{-Mblib }{%{_bindir}/}' \
    %{buildroot}%{_libexecdir}/%{name}/t/{02-perlreq.t,03-perlprov.t}
# Remove the only remaining use of -Mblib so that we dont have to fake ./blib
# tree.
perl -i -pe 's{-Mblib }{}' \
    %{buildroot}%{_libexecdir}/%{name}/t/01-B-PerlReq.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc README* Changes perl5-alt-rpm-macros macros.env
%dir %{perl_vendorarch}/auto/B
%dir %{perl_vendorarch}/auto/B/ConstOptree
%{perl_vendorarch}/auto/B/ConstOptree/ConstOptree.so
%dir %{perl_vendorarch}/B
%{perl_vendorarch}/B/Clobbers.pm
%{perl_vendorarch}/B/ConstOptree.pm
%{perl_vendorarch}/B/PerlReq.pm
%{perl_vendorarch}/B/Walker.pm
%dir %{perl_vendorarch}/PerlReq
%{perl_vendorarch}/PerlReq/Utils.pm
%{perl_vendorarch}/fake.pm
%{_mandir}/man3/B::Clobbers.3*
%{_mandir}/man3/B::ConstOptree.3*
%{_mandir}/man3/B::PerlReq.3*
%{_mandir}/man3/B::Walker.3*
%{_mandir}/man3/PerlReq::Utils.3*

%files scripts
%{_bindir}/perl.clean
%{_bindir}/perl.prov
%{_bindir}/perl.prov.files
%{_bindir}/perl.req
%{_bindir}/perl.req.files
%{_mandir}/man1/perl.prov.1*
%{_mandir}/man1/perl.req.1*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
