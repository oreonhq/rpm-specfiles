%global source0_hash 9176ad646729e3bd27cf7abf114bedd3424bff1ba61185cfc7d54f3a9223a8ff

Name:           perl-ExtUtils-XSpp
Epoch:          1
Version:        0.18
Release:        34%{?dist}
Summary:        C++ variant of Perl's XS language
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-XSpp
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-XSpp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
# Exporter not used at tests
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.07
BuildRequires:  perl(ExtUtils::Typemaps)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
# Getopt::Long not used at tests
BuildRequires:  perl(IO::Handle)
# IPC::Open2 not used at tests
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(if)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Base::Filter)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
Requires:       perl(IPC::Open2)
Requires:       perl(ExtUtils::ParseXS) >= 3.07

%global __requires_exclude_from %{?__requires_exclude_from:__requires_exclude_from|}^%{_datadir}/doc

%description
ExtUtils::XSpp handles the XS++ language, used to create an extension interface
between Perl and C++ code/library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-XSpp-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes examples README XSP.yp
%{_bindir}/xspp
%{perl_vendorlib}/ExtUtils*
%{_mandir}/man?/*

%changelog
%autochangelog
