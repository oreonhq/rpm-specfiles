%global source0_hash e83148d49014f3b5a2bbe07a0698ad277dfa0a38fd8babce66d421f7ee151d5e

%if 0%{?rhel} >= 10
%define test_with_wayland 1
%else
%define test_with_wayland 0
%endif

Name:           perl-Tk-EntryCheck
Version:        0.04
Release:        42%{?dist}
Summary:        Interface to Tk::Entry for controlling its length and content
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-EntryCheck
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STRAT/Tk-EntryCheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.5
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::Entry)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test)
BuildRequires:  perl(Tk)
%if %{test_with_wayland}
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
BuildRequires:  font(:lang=en)
BuildRequires:  xorg-x11-server-Xvfb
%endif

%description
This module acts as a little wrapper around Tk::Entry and adds an easy to
use interface to -validate and -validatecommand for controlling length and
content of an entry widget.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{test_with_wayland}
Requires:       mesa-dri-drivers
Requires:       mutter
Requires:       xwayland-run
%else
Requires:       font(:lang=en)
Requires:       xorg-x11-server-Xvfb
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-EntryCheck-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
%if %{test_with_wayland}
cd %{_libexecdir}/%{name} && exec xwfb-run -c mutter -- prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%else
cd %{_libexecdir}/%{name} && exec xvfb-run -d prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%if %{test_with_wayland}
xwfb-run -c mutter -- make test
%else
xvfb-run -d make test
%endif

%files
%doc example CHANGES README
%dir %{perl_vendorlib}/Tk
%{perl_vendorlib}/Tk/EntryCheck.pm
%{_mandir}/man3/Tk::EntryCheck.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
