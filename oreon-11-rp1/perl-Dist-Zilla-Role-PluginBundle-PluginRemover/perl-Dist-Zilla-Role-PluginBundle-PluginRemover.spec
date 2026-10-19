%global source0_hash e389bcf18001017fe476a8fc244ccd81cdcaa6406b537322c7576f575d878026
Name:           perl-Dist-Zilla-Role-PluginBundle-PluginRemover
Version:        0.105
Release:        1%{?dist}
Summary:        Remove plugins from a Dist::Zilla plugin bundle
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Role-PluginBundle-PluginRemover
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/Dist-Zilla-Role-PluginBundle-PluginRemover-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(List::Util) >= 1.45
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:  perl(Dist::Zilla::Role::PluginBundle::Easy)
BuildRequires:  perl(Dist::Zilla::Util)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This role enables your Dist::Zilla plugin bundle to automatically remove
any plugins specified by the "-remove" attribute.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Role-PluginBundle-PluginRemover-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
