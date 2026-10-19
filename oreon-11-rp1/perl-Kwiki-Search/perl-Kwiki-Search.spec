%global source0_hash 278d7efa753d07ad1f70426fa78f80a601ce0934a40e8812d481cd95ba0c7740
Name:           perl-Kwiki-Search
Version:        0.12
Release:        1%{?dist}
Summary:        Kwiki Search Plugin
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-Search
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Kwiki-Search-%{version}.tar.gz
Patch0:         Kwiki-Search-0.12-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
Requires:       perl(Kwiki) >= 0.34
Requires:       perl(Kwiki::Installer)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Kwiki)
BuildRequires:  perl(Kwiki::CGI)
BuildRequires:  perl(Kwiki::Installer)
BuildRequires:  perl(Kwiki::Plugin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(mixin)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
