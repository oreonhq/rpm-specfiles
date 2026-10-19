%global source0_hash 8d896444d71e1d0bca3d24e31e5d82bd0d9542aaed91d1fb7eab367bce675c50
Name:           perl-Cairo-GObject
Version:        1.005
Release:        1%{?dist}
Summary:        Integrate Cairo into the Glib type system
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Cairo-GObject
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Cairo-GObject-%{version}.tar.gz
Requires:       perl(Cairo) >= 1.080
Requires:       perl(Glib) >= 1.224
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Cairo\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Cairo)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(cairo-gobject)
# /oreon:deps
%description
Cairo::GObject registers Cairo's types ("Cairo::Context", "Cairo::Surface",
etc.) with Glib's type systems so that they can be used normally in signals
and properties.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cairo-GObject-%{version}
chmod 0755 t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS" 
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
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
%files -n perl-Cairo-GObject-tests -f %{oreon_filedir}/perl-Cairo-GObject-tests.list

%changelog

%autochangelog
