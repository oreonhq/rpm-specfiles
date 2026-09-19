%global source0_hash eaf18e61ba6a3e143846a7cc66f08ce58a0c4fbda92acb31aede25cb3b5c3dcc

Name:           perl-Text-Patch
Version:        1.8
Release:        41%{?dist}
Summary:        Patches text with given patch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Text-Patch
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CADE/Text-Patch-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)

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

%check
make test

%files
%license COPYING
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
