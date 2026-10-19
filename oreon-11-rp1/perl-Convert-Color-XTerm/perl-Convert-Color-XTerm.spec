%global source0_hash ae1b56388594bbccef6cffe708007f8bcccd4569e31a2c33745216a635237916
Name:           perl-Convert-Color-XTerm
Version:        0.06
Release:        1%{?dist}
Summary:        Indexed colors used by XTerm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Color-XTerm/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Convert-Color-XTerm-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Convert::Color::RGB8) >= 0.06
Suggests:       perl(Convert::Color::X11)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Convert::Color::RGB8\\)$
Provides:       perl(Convert::Color::XTerm)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::Color::RGB)
BuildRequires:  perl(Convert::Color::RGB8)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This subclass of Convert::Color::RGB8 provides lookup of the colors that
xterm uses by default. Note that the module is not intelligent enough to
actually parse the XTerm configuration on a machine, nor to query a running
terminal for its actual colors. It simply implements the colors that are
present as defaults in the XTerm source code.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Convert-Color-XTerm-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Convert-Color-XTerm-tests -f %{oreon_filedir}/perl-Convert-Color-XTerm-tests.list

%changelog

%autochangelog
