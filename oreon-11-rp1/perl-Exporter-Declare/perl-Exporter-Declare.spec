%global source0_hash 4bd70d6ca76f6f6ba7e4c618d4ac93b8593a58f1233ccbe18b10f5f204f1d4e4
Name:           perl-Exporter-Declare
Version:        0.114
Release:        1%{?dist}
Summary:        Exporting done right
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Exporter-Declare
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Exporter-Declare-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Meta::Builder) >= 0.003
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Meta::Builder\\)\s*$
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fennec::Lite)
BuildRequires:  perl(Meta::Builder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(aliased)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Exporter::Declare is a meta-driven exporting tool. Exporter::Declare tries
to adopt all the good features of other exporting tools, while throwing
away horrible interfaces. Exporter::Declare also provides hooks that allow
you to add options and arguments for import. Finally, Exporter::Declare's
meta-driven system allows for top-notch introspection.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Exporter-Declare-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
