%global source0_hash e1c958c042427a175e051e0008f2025e8ec80613d3c7750597bf8e529b04420e

Name:       perl-FCGI-ProcManager
Version:    0.28
Release:    27%{?dist}
# ProcManager.pm -> LGPLv2, LGPLv3
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+
Summary:    A FastCGI process manager
Source:     https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/FCGI-ProcManager-%{version}.tar.gz
Url:        https://metacpan.org/release/FCGI-ProcManager
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
# testing...
BuildRequires: perl(Test)

%{?perl_default_filter}

%description
FCGI::ProcManager is used to serve as a FastCGI process manager. By
re-implementing it in perl, developers can more finely tune performance
in their web applications, and can take advantage of copy-on-write
semantics prevalent in UNIX kernel process management.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n FCGI-ProcManager-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README ChangeLog
%license COPYING
%{perl_vendorlib}/FCGI*
%{_mandir}/man3/FCGI*.3*

%changelog
%autochangelog
