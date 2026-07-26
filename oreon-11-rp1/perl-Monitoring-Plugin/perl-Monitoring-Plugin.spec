%global source0_hash f8ba6b7e27d2bb0a4f9a32955a2442d4e428d1c48b80c8b12142ff611be7236f

Name:           perl-Monitoring-Plugin
Version:        0.40
Release:        21%{?dist}
Summary:        Family of modules to streamline writing plugins for various monitoring systems
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Monitoring-Plugin
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIERLEIN/Monitoring-Plugin-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Math::Calc::Units)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)

%description
Monitoring::Plugin and its associated Monitoring::Plugin::* modules are a
family of perl modules to streamline writing Monitoring plugins. The main
end user modules are Monitoring::Plugin, providing an object-oriented
interface to the entire Monitoring::Plugin::* collection, and
Monitoring::Plugin::Functions, providing a simpler functional interface to
a useful subset of the available functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Monitoring-Plugin-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files

%doc Changes notes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
