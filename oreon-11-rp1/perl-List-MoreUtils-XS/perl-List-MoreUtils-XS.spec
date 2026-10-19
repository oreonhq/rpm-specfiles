%global source0_hash e8ce46d57c179eecd8758293e9400ff300aaf20fefe0a9d15b9fe2302b9cb242
%bcond_with perl_List_MoreUtils_XS_enables_extra_test
Name:		perl-List-MoreUtils-XS
Version:	0.430
Release:        1%{?dist}
Summary:        Provide compiled List::MoreUtils functions
License:	(GPL-1.0-or-later OR Artistic-1.0-Perl) AND Apache-2.0
URL:		https://metacpan.org/release/List-MoreUtils-XS
Source0:        https://cpan.metacpan.org/modules/by-module/List/List-MoreUtils-XS-%{version}.tar.gz
Patch0:		List-MoreUtils-XS-0.430-unbundle.patch
%if %{with perl_List_MoreUtils_XS_enables_extra_test}
%endif
%{?perl_default_filter}
Provides:       perl(List::MoreUtils::XS)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config::AutoConf)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides accelerated versions of functions in List::MoreUtils.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n List-MoreUtils-XS-%{version}

# Unbundle bundled modules except private inc::Config::AutoConf::LMU
%patch -P 0
find inc/ -type f ! -name LMU.pm -print -delete
perl -i -ne 'print $_ unless m{^inc/} and not m{LMU\.pm}' MANIFEST

%build

perl Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{optflags}"\
	NO_PERLLOCAL=1 \
	NO_PACKLIST=1
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.430-19
- Prepare for Oreon 11 (RP1)
