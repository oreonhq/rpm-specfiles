%global source0_hash 09c11dc6b275fde4093b395dddbdee61c447d6be458f95937b475fb9da381a8b
Name:           perl-CPANPLUS-Shell-Default-Plugins-Diff
Version:        0.01
Release:        1%{?dist}
Summary:        Diff module versions from the CPANPLUS shell
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS-Shell-Default-Plugins-Diff
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KANE/CPANPLUS-Shell-Default-Plugins-Diff-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CPANPLUS::Shell::Default)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This plugin allows you to diff 2 versions of modules from within the CPANPLUS
shell and see what code changes have taken place.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CPANPLUS-Shell-Default-Plugins-Diff-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
