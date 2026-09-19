%global source0_hash afa2472f9e381e9b205811959bbf716f75b4cd75656287396361444c970ac558

Name:           perl-Dist-Zilla-Config-Slicer
Version:        0.202
Release:        26%{?dist}
Summary:        Config::MVP::Slicer customized for Dist::Zilla
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Config-Slicer
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/Dist-Zilla-Config-Slicer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config::MVP::Slicer)
BuildRequires:  perl(Dist::Zilla::PluginBundle::Filter)
BuildRequires:  perl(Dist::Zilla::Util) >= 4
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:  perl(Dist::Zilla::Role::PluginBundle::Easy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Dist::Zilla::PluginBundle::Filter)

%description
These Dist::Zilla plugins allow to override a configuration for a bundle in
means of slicing as exists in Config::MVP::Slicer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Config-Slicer-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
