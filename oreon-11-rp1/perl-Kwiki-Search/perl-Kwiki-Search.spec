%global source0_hash 278d7efa753d07ad1f70426fa78f80a601ce0934a40e8812d481cd95ba0c7740

Name:           perl-Kwiki-Search
Version:        0.12
Release:        58%{?dist}
Summary:        Kwiki Search Plugin
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-Search
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Kwiki-Search-%{version}.tar.gz
Patch0:         Kwiki-Search-0.12-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(Kwiki) >= 0.34
BuildRequires:  perl(Kwiki::CGI)
BuildRequires:  perl(Kwiki::Installer)
BuildRequires:  perl(Kwiki::Plugin)
BuildRequires:  perl(mixin)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Kwiki) >= 0.34
Requires:       perl(Kwiki::Installer)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Kwiki-Search-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
