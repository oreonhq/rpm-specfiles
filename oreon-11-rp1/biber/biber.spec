%global source0_hash 82adcff9e71b4fc02ad6132f9ccd79137ad390e4d3392c7f681a85246c0cdc01
%bcond_without biber_enables_extra_test
Name:           biber
%define bcfversion 3.11
Version:        2.22
Release:        1%{?dist}
Summary:        Command-line bibliographic manager, BibTeX replacement
License:        Artistic-2.0
SourceLicense:  %{license} AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            http://biblatex-biber.sourceforge.net/
Source0:        https://github.com/plk/biber/archive/v%{version}.tar.gz
Patch0:         biber-drop-builddeps-for-monolithic-build.patch
Patch1:         biber-2.16-Normalize-shebangs.patch
BuildArch:      noarch
%if %{with biber_enables_extra_test}
%endif
%if %{with biber_enables_extra_test}
%endif
%if %{with biber_enables_extra_test}
%endif
%if %{with biber_enables_extra_test}
%endif
Requires:       perl(autovivification)
Requires:       perl(Business::ISBN)
Requires:       perl(Business::ISMN)
Requires:       perl(Business::ISSN)
Requires:       perl(Lingua::Translit) >= 0.28
Requires:       perl(LWP::UserAgent)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Text::BibTeX) >= 0.88
Requires:       perl(Unicode::Collate::Locale) >= 1.29
Requires:       perl(XML::LibXSLT)
Provides:       bcfversion = %{bcfversion}
Provides:       perl(Biber) = %{version}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Text::BibTeX|Unicode::Collate::Locale)\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Biber\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Business::ISBN)
BuildRequires:  perl(Business::ISMN)
BuildRequires:  perl(Business::ISSN)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Compare)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Uniqid)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Calendar::Julian)
BuildRequires:  perl(DateTime::Format::Builder)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Lingua::Translit)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Log::Log4perl::Appender::File)
BuildRequires:  perl(Log::Log4perl::Appender::Screen)
BuildRequires:  perl(Log::Log4perl::Layout::PatternLayout)
BuildRequires:  perl(Log::Log4perl::Layout::SimpleLayout)
BuildRequires:  perl(Log::Log4perl::Level)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sort::Key)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::BibTeX)
BuildRequires:  perl(Text::BibTeX::Name)
BuildRequires:  perl(Text::BibTeX::NameFormat)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::Roman)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI)
BuildRequires:  perl(Unicode::Collate::Locale)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::Simple)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Writer)
BuildRequires:  perl(autovivification)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(open)
BuildRequires:  perl(parent)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Biber is a command-line tool for dealing with bibliographic databases.
Biber offers a large superset of legacy BibTeX (texlive-bibtex)
functionality.  It is often used with the popular BibLaTeX package
(texlive-biblatex), where it is required for some features.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n biber-%{version}
# t/remote-files.t needs the Internet
for F in \
    t/remote-files.t \
%if !%{with biber_enables_extra_test}
    t/full-*.t \
%endif
; do
    rm "$F";
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E\b}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/data/schemata
ln -s "$(realpath --relative-to \
        %{buildroot}%{_libexecdir}/%{name}/data \
        %{buildroot}%{perl_vendorlib}/Biber/biber-tool.conf)" \
    %{buildroot}%{_libexecdir}/%{name}/data
for F in {bcf,config}.{rnc,rng}; do
    ln -s %{perl_vendorlib}/Biber/"$F" \
        %{buildroot}%{_libexecdir}/%{name}/data/schemata
done
%if %{with biber_enables_extra_test}
mkdir %{buildroot}%{_libexecdir}/%{name}/bin
ln -s "$(realpath --relative-to \
        %{buildroot}%{_libexecdir}/%{name}/bin \
        %{buildroot}%{_bindir}/%{name})" \
    %{buildroot}%{_libexecdir}/%{name}/bin
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset BIBER_DEV_TESTS ISBN_RANGE_MESSAGE PAR_TEMP PERL_LWP_SSL_CA_FILE
%if %{with biber_enables_extra_test}
export BIBER_DEV_TESTS=1
%endif
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles biber-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset BIBER_DEV_TESTS ISBN_RANGE_MESSAGE PAR_TEMP PERL_LWP_SSL_CA_FILE
%if %{with biber_enables_extra_test}
export BIBER_DEV_TESTS=1
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n biber-tests -f %{oreon_filedir}/biber-tests.list

%changelog

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 10 2025 Petr Pisar <ppisar@redhat.com> - 2.21-1
- 2.21 bump

* Mon Feb 03 2025 Petr Pisar <ppisar@redhat.com> - 2.20-1
- 2.20 bump

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 10 2023 Petr Pisar <ppisar@redhat.com> - 2.19-2
- Rebuild with a different release number

* Tue Mar 07 2023 Petr Pisar <ppisar@redhat.com> - 2.19-1
- 2.19 bump
- License corrected to Artistic-2.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 09 2022 Petr Pisar <ppisar@redhat.com> - 2.18-1
- 2.18 bump

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.17-4
- Perl 5.36 rebuild

* Wed May 25 2022 Petr Pisar <ppisar@redhat.com> - 2.17-3
- Adapt to Perl 5.36
- Use relative symbolic links in the tests

* Mon Jan 31 2022 Petr Pisar <ppisar@redhat.com> - 2.17-2
- Provide bcfversion for textlive-biblatex to depend on (bug #2048536)

* Wed Jan 26 2022 Petr Pisar <ppisar@redhat.com> - 2.17-1
- 2.17 bump

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.16-3
- Perl 5.34 rebuild

* Tue May 18 2021 Petr Pisar <ppisar@redhat.com> - 2.16-2
- Fix a typo in a dependency type

* Tue May 18 2021 Petr Pisar <ppisar@redhat.com> - 2.16-1
- 2.16 bump
- Package the tests

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-3
- Perl 5.32 re-rebuild of bootstrapped packages

* Wed Jun 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-2
- Perl 5.32 rebuild

* Thu May 14 2020 Tom Callaway <spot@fedoraproject.org> - 2.14-1
- update to 2.14 for TL 2020

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Colin B. Macdonald <cbm@m.fsf.org> - 2.12-1
- Update to 2.12 (bug #1773172)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-5
- Perl 5.30 rebuild

* Tue Feb 12 2019 Petr Pisar <ppisar@redhat.com> - 2.11-4
- Adapt tests to Unicode-Collate-1.27 (bug #1674692)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Colin B. Macdonald <cbm@m.fsf.org> - 2.11-2
- Re-enable tests for e.g., #1512848

* Tue Oct 16 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.11-1
- Update to 2.11

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.7-2
- Perl 5.28 rebuild

* Wed Apr 11 2018 Colin B. Macdonald <cbm@m.fsf.org> - 2.7-1
- Version bump, temporarily disable tests

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.6-5
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2.6-3
- cherry-pick upstream commit for #1401750.
- more BR.

* Mon Dec 05 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2.6-2
- update biblatex dep, add compatibility table to spec

* Wed Oct 12 2016 Tom Callaway <spot@fedoraproject.org> - 2.6-1
- update to 2.6

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.1-5
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.1-3
- Add another missing BR for tests.

* Sun Dec 20 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.1-2
- cherry-pick from upstream to avoid braces warning.
- enable tests, then patch and cherry-pick so they pass.
- tarball missing two files needed for tests.
- BR on perl(open) for tests.
- patches to enquiet build, fix brace warnings.
- spec formatting fixes.

* Mon Dec 14 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.1-1
- Bump to 2.1, for biblatex-3.0.
- Update deps.
- Add more deps based on upstream confirmation.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-11
- Perl 5.22 rebuild

* Tue Jun 09 2015 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-10
- Add autovivification dep (#1229816).

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.8-9
- Perl 5.22 rebuild

* Wed May 20 2015 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-8
- Clean up deps as per review.

* Thu Mar 19 2015 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-7
- Upstream thinks ok to relax U::C requirements.

* Wed Dec 3 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-6
- Add Requires, taken from Build.pl.

* Tue Nov 25 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-5
- Use sourceforge for Source0 instead of particular git commit.

* Tue Nov 25 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-4
- lots more BRs, perm fixes.

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-3
- update description and Summary

* Wed Nov 19 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-2
- Add dep on (probably overly) specific texlive-biblatex

* Tue Jan 14 2014 Colin B. Macdonald <cbm@m.fsf.org> - 1.8-1
- Bump to 1.8
- perl-File-Slurp-Unicode no longer needed
- add perl-autovivification dep

* Wed Aug 22 2012 Mary Ellen Foster <mefoster@gmail.com> - 1.2-1
- Initial quick-and-dirty package
