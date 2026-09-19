%global source0_hash 7e75853a0f8fe6c02fe90e4cb28f953bd23d7a976c53f220062064dd4284021f

Name:           perl-CGI-Application-Plugin-DebugScreen
Version:        1.00
Release:        44%{?dist}
Summary:        Add Debug support to CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-DebugScreen
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEKOKAK/CGI-Application-Plugin-DebugScreen-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::Application::Plugin::ViewCode)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This plugin adds debug support to CGI::Application and works like
Catalyst's debug mode.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-DebugScreen-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
