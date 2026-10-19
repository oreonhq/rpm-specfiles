%global source0_hash 20ab8070c56377bd302c9ec5a16873714026d03e56a31cf70ab65632c1ed5bc7
Name:           perl-Convert-NLS_DATE_FORMAT
Version:        0.06
Release:        38%{?dist}
Summary:        Convert Oracle NLS_DATE_FORMAT <-> strftime Format Strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-NLS_DATE_FORMAT
Source0:        https://cpan.metacpan.org/authors/id/K/KO/KOLIBRIE/Convert-NLS_DATE_FORMAT-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Convert Oracle's NLS_DATE_FORMAT string into a strptime format string, or
the reverse.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-NLS_DATE_FORMAT-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
