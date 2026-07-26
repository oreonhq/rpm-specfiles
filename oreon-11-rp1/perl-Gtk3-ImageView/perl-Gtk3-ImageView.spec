%global source0_hash c04ee10f8ce55133d7f997cc88768a21a93496b5408aed806afcf77fc87a9fa9

%if 0%{?rhel} >= 10
%global wayland 1
%else
%global wayland 0
%endif

Name:           perl-Gtk3-ImageView
Version:        12
Release:        4%{?dist}
Summary:        Image viewer widget for GTK 3
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/DarthGandalf/gtk3-imageview
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASOKOLOV/Gtk3-ImageView-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Cairo)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Glib) >= 1.2100
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(if)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Carp::Always)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
%if %{wayland}
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
BuildRequires:  xorg-x11-server-Xvfb
%endif
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(if)
Requires:       perl(Glib) >= 1.2100

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\)$

%description
The Gtk3::ImageView widget allows the user to zoom, pan and select the
specified image and provides hooks to allow additional tools, e.g. painter,
to be created and used.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Glib) >= 1.2100
%if %{wayland}
Requires:       mutter
Requires:       xwayland-run
%else
Requires:       xorg-x11-server-Xvfb
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Gtk3-ImageView-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -ex
cd %{_libexecdir}/%{name}
%if %{wayland}
LOGFILE=$(mktemp)
# Some tests fail on Xwayland
xwfb-run -c mutter -- prove -I . -j 1 ||:
cat "$LOGFILE"
rm "$LOGFILE"
%else
xvfb-run -d prove -I . -j 1
%endif
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Not parallel-safe
%if %{wayland}
LOGFILE=$(mktemp)
# Some tests fail on Xwayland
xwfb-run -e "$LOGFILE" -c mutter -- make test ||:
cat "$LOGFILE"
rm "$LOGFILE"
%else
xvfb-run -d make test
%endif

%files
%license LICENSE
%doc README.md
%dir %{perl_vendorlib}/Gtk3
%{perl_vendorlib}/Gtk3/ImageView
%{perl_vendorlib}/Gtk3/ImageView.pm
%{_mandir}/man3/Gtk3::ImageView.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
