%global source0_hash cb99150f9ffa51dbc3be5ee98d8e91c98cdfeae22eb88e718f2cf367bf270d17
Name:           perl-Linux-Inotify2 
Summary:        Scalable directory/file change notification
Version:        2.3
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Linux-Inotify2-%{version}.tar.gz
URL:            https://metacpan.org/release/Linux-Inotify2
Patch0:         Linux-Inotify2-2.3-use-File-Temp-for-temporary-dir.patch
Requires:       perl(XSLoader)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(common::sense)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements an interface to the Linux 2.6.13+ Inotify
file/directory change notification system. It has a number of advantages over
the Linux::Inotify module: 
   - it is portable (Linux::Inotify only works on x86)
   - the equivalent of full name works correctly
   - it is better documented
   - it has callback-style interface, which is better suited for integration.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Linux-Inotify2-%{version}
%patch -P0 -p1

find . -type f -exec chmod -c -x {} ';'
find eg/ -type f -exec \
    perl -MConfig -pi -e 's|^#!/opt/bin/perl|$Config{startperl}|' {} ';'

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Linux-Inotify2-tests -f %{oreon_filedir}/perl-Linux-Inotify2-tests.list

%changelog

%autochangelog
