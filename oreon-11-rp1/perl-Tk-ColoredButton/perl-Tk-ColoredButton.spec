%global source0_hash f217783a8960f255dd42c8d5e8e90bf9f115855f0f37c9226478c9f2e3eecf42
Name:           perl-Tk-ColoredButton
Version:        1.05
Release:        1%{?dist}
Summary:        Button widget with background gradient color
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-ColoredButton
Source0:        https://cpan.metacpan.org/authors/id/D/DJ/DJIBEL/Tk-ColoredButton-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Tk) >= 800
Requires:       perl(Tk::Canvas::GradientColor) >= 1.04
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Tk::Canvas::GradientColor\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Balloon)
BuildRequires:  perl(Tk::Canvas::GradientColor)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Tk::ColoredButton is an extension of the Tk::Canvas::GradientColor
widget. It is an easy way to simulate a button widget with gradient
background color.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-ColoredButton-%{version}
sed -i -e 's/\r$//' Changes demo/create_buttons.pl README t/00-load.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{boilerplate,pod,pod-coverage}.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Tk-ColoredButton-tests -f %{oreon_filedir}/perl-Tk-ColoredButton-tests.list

%changelog

%autochangelog
