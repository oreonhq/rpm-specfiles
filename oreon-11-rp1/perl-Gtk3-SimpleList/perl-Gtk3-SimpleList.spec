%global source0_hash 1d4465100bf3bc0474a29469a406fd033562b6e3736188121000372ab2ada884

Name:           perl-Gtk3-SimpleList
Version:        0.21
Release:        19%{?dist}
Summary:        Simple interface to Gtk3's complex MVC list widget
# lib/Gtk3/SimpleList.pm:   LGPL-2.1-or-later
# README:                   LGPL-2.1-or-later OR Artistic-2.0
License:        LGPL-2.1-or-later AND (LGPL-2.1-or-later OR Artistic-2.0)
URL:            https://metacpan.org/release/Gtk3-SimpleList
Source0:        https://cpan.metacpan.org/authors/id/T/TV/TVIGNAUD/Gtk3-SimpleList-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Gtk3)
# Gtk3::TreeView not provided by Gtk3 because the Perl module names are generated
# gtk3 gobject typelib at run-time.
# Tests:
BuildRequires:  perl(Test::More)

%description
Gtk3 has a powerful, but complex MVC (Model, View, Controller) system used
to implement list and tree widgets. Gtk3::SimpleList Perl module automates the
complex setup work and allows you to treat the list model as a more natural
list of lists structure.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk3-SimpleList-%{version}
chmod +x t/*.t

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
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license COPYING
%doc Changes README
%dir %{perl_vendorlib}/Gtk3
%{perl_vendorlib}/Gtk3/SimpleList.pm
%{_mandir}/man3/Gtk3::SimpleList.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
