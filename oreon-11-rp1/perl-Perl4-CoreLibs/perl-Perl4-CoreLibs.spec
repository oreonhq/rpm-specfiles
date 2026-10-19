%global source0_hash 0250aafd307e5d25670946a662bdd0a2a8cc6ed9d949a848753f0b26910923a8
Name:           perl-Perl4-CoreLibs
Version:        0.005
Release:        1%{?dist}
Summary:        Libraries historically supplied with Perl 4
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl4-CoreLibs
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Perl4-CoreLibs-%{version}.tar.gz
BuildArch:      noarch
Requires:       hostname
Requires:       perl(File::Find)
Requires:       perl(IPC::Open2)
Requires:       perl(IPC::Open3)
Requires:       perl(Socket)
Requires:       perl(Sys::Syslog) => 0.19
Requires:       perl(Text::ParseWords) >= 3.25
Requires:       perl(Time::Local)
Requires:       perl(warnings::register)
Provides:       perl(abbrev.pl) = %{version}
Provides:       perl(assert.pl) = %{version}
Provides:       perl(bigfloat.pl) = %{version}
Provides:       perl(bigint.pl) = %{version}
Provides:       perl(bigrat.pl) = %{version}
Provides:       perl(cacheout.pl) = %{version}
Provides:       perl(chat2.pl) = %{version}
Provides:       perl(complete.pl) = %{version}
Provides:       perl(ctime.pl) = %{version}
Provides:       perl(dotsh.pl) = %{version}
Provides:       perl(exceptions.pl) = %{version}
Provides:       perl(fastcwd.pl) = %{version}
Provides:       perl(finddepth.pl) = %{version}
Provides:       perl(find.pl) = %{version}
Provides:       perl(flush.pl) = %{version}
Provides:       perl(ftp.pl) = %{version}
Provides:       perl(getcwd.pl) = %{version}
Provides:       perl(getopt.pl) = %{version}
Provides:       perl(getopts.pl) = %{version}
Provides:       perl(hostname.pl) = %{version}
Provides:       perl(importenv.pl) = %{version}
Provides:       perl(look.pl) = %{version}
Provides:       perl(open2.pl) = %{version}
Provides:       perl(open3.pl) = %{version}
Provides:       perl(pwd.pl) = %{version}
Provides:       perl(shellwords.pl) = %{version}
Provides:       perl(stat.pl) = %{version}
Provides:       perl(syslog.pl) = %{version}
Provides:       perl(tainted.pl) = %{version}
Provides:       perl(termcap.pl) = %{version}
Provides:       perl(timelocal.pl) = %{version}
Provides:       perl(validate.pl) = %{version}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  hostname
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(newgetopt.pl)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This is a collection of .pl files that have historically been bundled with the
Perl core and were removed from perl 5.16.  These files should not be used by
new code.  Functionally, most have been directly superseded by modules in the
Perl 5 style. This collection exists to support old Perl programs that
predates satisfactory replacements.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl4-CoreLibs-%{version}
# newgetopt.pl is distributed by Getopt-Long, CPAN RT#102212
rm lib/newgetopt.pl
sed -i -e '/^lib\/newgetopt\.pl/d' MANIFEST
%build

perl Build.PL installdirs=vendor
./Build
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
%install
./Build install destdir=%{buildroot} create_packlist=0
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Perl4-CoreLibs-tests -f %{oreon_filedir}/perl-Perl4-CoreLibs-tests.list

%changelog

%autochangelog
