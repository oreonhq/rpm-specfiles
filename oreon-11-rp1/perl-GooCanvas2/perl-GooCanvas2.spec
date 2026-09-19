%global source0_hash e24c87873e19063dd4d5e2c709caacf8c0ae8881044395bb865dc2b4fdd63b50

Name:           perl-GooCanvas2
Version:        0.06
Release:        24%{?dist}
Summary:        Perl binding for GooCanvas2 widget using Glib::Object::Introspection
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GooCanvas2
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLMAX/GooCanvas2-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
# goocanvas2 typelib loaded by Glib::Object::Introspection
BuildRequires:  goocanvas2 >= 2.0
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
# goocanvas2 typelib loaded by Glib::Object::Introspection
Requires:       goocanvas2 >= 2.0
# Provide some class identifiers that are required by other RPM packages. We
# cannot list them all because they are created at run-time from typelib file
# provided by goocanvas2 package that could change between building and
# running.
Provides:       perl(GooCanvas2::Canvas) = %{version}

%description
GooCanvas2 is a new canvas widget for use with Gtk3 that uses the Cairo
2-dimensional library for drawing. This is a Perl binding for this wonderful
Canvas widget.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GooCanvas2-%{version}

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
%doc Changes README
%{perl_vendorlib}/GooCanvas2.pm
%{_mandir}/man3/GooCanvas2.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
