%global source0_hash bb54950b920ac1c8e3041096b4b7d1f588ae119d9e48acc51e20047f82c703b3
Name:           perl-opts
Summary:        Simple command line option parser
%global upstream_version 0.08
Version:        0.080
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKIHOSHI/opts-%{upstream_version}.tar.gz
URL:            https://metacpan.org/release/opts
BuildArch:      noarch
Requires:       perl(Getopt::Long) >= 2.37
Requires:       perl(PadWalker) >= 1.9
Requires:       perl(Text::Table)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Getopt::Long|PadWalker)\\)$
%{?perl_default_subpackage_tests}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
opts is a DSL for quickly and easily handling command line options.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n opts-%{upstream_version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
