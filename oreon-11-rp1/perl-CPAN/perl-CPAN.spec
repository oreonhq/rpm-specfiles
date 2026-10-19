%global source0_hash ea6e8ce94ab51c1088071d7b0427c7f08eb1e2002ac9c69c6275aab958e7cf90
%bcond_with perl_CPAN_enables_gnupg_test
%bcond_with perl_CPAN_enables_optional_test
Name:           perl-CPAN
Version:        2.41
Release:        1%{?dist}
Summary:        Query, download and build perl modules from CPAN sites
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/CPAN-%{version}.tar.gz
Patch0:         CPAN-2.18-Attemp-to-create-site-library-directories-on-first-t.patch
Patch1:         CPAN-2.18-Replace-configuration-directory-string-with-a-marke.patch
Patch2:         CPAN-2.38-Only-require-config-for-CPAN-shell-operations.patch
Patch3:         CPAN-2.38-Add-notes-about-first-configuration.patch
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
%if %{with perl_CPAN_enables_optional_test}
%if %{with perl_CPAN_enables_gnupg_test}
%endif
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%if %{with perl_CPAN_enables_gnupg_test}
%endif
%endif
%if %{with perl_CPAN_enables_gnupg_test}
%endif
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       make
Requires:       perl
Requires:       perl(Archive::Tar) >= 1.50
%if !%{defined perl_bootstrap}
Recommends:     perl(CPAN::DistnameInfo)
%endif
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Data::Dumper)
%if !%{defined perl_bootstrap}
Requires:       perl(Devel::Size)
%endif
Requires:       perl(ExtUtils::Manifest)
%if !%{defined perl_bootstrap}
Requires:       perl(File::HomeDir) >= 0.65
%endif
Requires:       perl(File::Temp) >= 0.16
Requires:       perl(lib)
%if !%{defined perl_bootstrap}
Suggests:       perl(Log::Log4perl)
%endif
Requires:       perl(Net::Config)
Requires:       perl(Net::FTP)
Requires:       perl(POSIX)
Requires:       perl(Term::ReadLine)
Requires:       perl(Time::Local)
%if !%{defined perl_bootstrap}
Requires:       perl(URI)
Requires:       perl(URI::Escape)
%endif
Requires:       perl(User::pwent)
%if !%{defined perl_bootstrap}
Requires:       perl(Archive::Zip)
Requires:       perl(Compress::Bzip2)
Requires:       perl(CPAN::Meta) >= 2.110350
%endif
Requires:       perl(Compress::Zlib)
Requires:       perl(Digest::MD5)
Requires:       perl(Digest::SHA)
Requires:       perl(Dumpvalue)
Requires:       perl(ExtUtils::CBuilder)
%if ! %{defined perl_bootstrap}
Requires:       perl(Module::Signature)
%endif
%if ! %{defined perl_bootstrap}
Requires:       perl(local::lib)
%endif
%if ! %{defined perl_bootstrap}
Requires:       perl(Module::Build)
%endif
Recommends:     perl(Pod::Perldoc)
%if ! %{defined perl_bootstrap}
Recommends:     perl(Term::ReadKey)
Requires:       perl(Text::Glob)
Suggests:       perl(Text::Levenshtein::Damerau::XS)
Suggests:       perl(YAML::Syck)
%endif
Provides:       cpan = %{version}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mac::BuildTools\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN::Meta::Requirements\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(CPAN::MyConfig\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(local_utils\\)
Provides:       perl(CPAN::HandleConfig)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Dumpvalue)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::Ping)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(autouse)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The CPAN module automates or at least simplifies the make and install of
perl modules and extensions. It includes some primitive searching
capabilities and knows how to use LWP, HTTP::Tiny, Net::FTP and certain
external download clients to fetch distributions from the net.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CPAN-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# Change configuration name
find -type f -exec perl -i -pe 's/XCPANCONFIGNAMEX/cpan/g' {} \;
# Remove bundled modules
rm -r ./inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

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
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t distroprefs %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/5*pod*.t
rm %{buildroot}%{_libexecdir}/%{name}/t/03pkgs.t
rm %{buildroot}%{_libexecdir}/%{name}/t/04clean_load.t
rm %{buildroot}%{_libexecdir}/%{name}/t/31sessions.t
perl -i -ple 's{-Mblib}{}' %{buildroot}%{_libexecdir}/%{name}/t/97-run.t
perl -i -ple 's{-Mblib}{}' %{buildroot}%{_libexecdir}/%{name}/t/97-return_values.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/blib/script
ln -s %{_bindir}/cpan %{buildroot}%{_libexecdir}/%{name}/blib/script
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
unset AUTHOR_TEST CPAN_EXPECT_TIMEOUT CPAN_RUN_SHELL_TEST_WITHOUT_EXPECT \
    ftp_proxy http_proxy no_proxy \
    PERL5_CPAN_IS_RUNNING PERL5_CPAN_IS_RUNNING_IN_RECURSION PERL_CORE VERBOSE
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I .
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TEST CPAN_EXPECT_TIMEOUT CPAN_RUN_SHELL_TEST_WITHOUT_EXPECT \
    ftp_proxy http_proxy no_proxy \
    PERL5_CPAN_IS_RUNNING PERL5_CPAN_IS_RUNNING_IN_RECURSION PERL_CORE VERBOSE
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-CPAN-tests -f %{oreon_filedir}/perl-CPAN-tests.list

%changelog

%autochangelog
