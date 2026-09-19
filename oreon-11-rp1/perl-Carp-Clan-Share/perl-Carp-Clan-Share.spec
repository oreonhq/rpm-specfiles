%global source0_hash aed0015be480028b5337bb73b7e7290578e3cbbf8e90f13e96044f13134c1b3d

Name:           perl-Carp-Clan-Share
Version:        0.013
Release:        47%{?dist}
Summary:        Share your Carp::Clan settings with your whole Clan
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Carp-Clan-Share
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKRIMEN/Carp-Clan-Share-%{version}.tar.gz
Patch0:         Carp-Clan-Share-0.013-Fix-building-on-Perl-without-dot-in-INC.patch
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
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

%description
This is a very lightweight helper module (actually just an import method)
that will automagically create a __PACKAGE__::Carp module for you.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Carp-Clan-Share-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
