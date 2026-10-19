%global source0_hash 39606a57aab20d4f4468300f2ec3fa2ab557fcc9cb7880ec7c6e07d80162da33
Name:           perl-Regexp-Common-net-CIDR
Version:        0.03
Release:        1%{?dist}
Summary:        Provide patterns for CIDR blocks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Regexp-Common-net-CIDR
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/Regexp-Common-net-CIDR-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Patterns for CIDR blocks.

Now only next IPv4 formats are supported:
  xxx.xxx/xx
  xxx.xxx.xxx/xx
  xxx.xxx.xxx.xxx/xx

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Regexp-Common-net-CIDR-%{version}

# Remove bundled modules
for f in $(find inc/Module -name *.pm); do
  pat=$(echo "$f" | sed 's,/,\\/,g;s,\.,\\.,g')
  rm $f
  sed -i -e "/$pat/d" MANIFEST
done

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
