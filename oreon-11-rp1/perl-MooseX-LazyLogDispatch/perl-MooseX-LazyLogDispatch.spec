%global source0_hash cad6d67e4d67c4158fcd62f85d1fc2a0b55cca53cfb5098a5a2f727918c067ab

Name:           perl-MooseX-LazyLogDispatch
Version:        0.02
Release:        49%{?dist}
Summary:        Logging Role for Moose
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-LazyLogDispatch
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLBLACK/MooseX-LazyLogDispatch-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Log::Dispatch::Config)
BuildRequires:  perl(Log::Dispatch::Configurator)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(IO::Scalar) >= 2.110
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More) >= 0.42

%{?perl_default_filter}

%description
Log::Dispatch role for use with your Moose classes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-LazyLogDispatch-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/Moose*
%{_mandir}/man3/Moose*

%changelog
%autochangelog
