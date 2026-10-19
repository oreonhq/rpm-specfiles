%global source0_hash eaf18e61ba6a3e143846a7cc66f08ce58a0c4fbda92acb31aede25cb3b5c3dcc
Name:           perl-Text-Patch
Version:        1.8
Release:        41%{?dist}
Summary:        Patches text with given patch
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Text-Patch
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CADE/Text-Patch-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Text::Patch combines source text with given diff (difference) data. Diff
data is produced by Text::Diff module or by the standard diff utility (man
diff, see -u option).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Patch-%{version}

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
