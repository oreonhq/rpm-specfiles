%global source0_hash c6baafb4241693fdb34b29ebd906993add364bf31aafa4462f3e062204cc87f0

Name:           perl-DBIx-Class-IntrospectableM2M
Version:        0.001002
Release:        31%{?dist}
Summary:        Introspect many-to-many shortcuts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-IntrospectableM2M
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/DBIx-Class-IntrospectableM2M-%{version}.tar.gz
Patch0:         DBIx-Class-IntrospectableM2M-0.001002-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)

%description
Because the many-to-many relationships are not real relationships, they can
not be introspected with DBIx::Class. Many-to-many relationships are
actually just a collection of convenience methods installed to bridge two
relationships. This DBIx::Class component can be used to store all relevant
information about these non-relationships so they can later be introspected
and examined.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-IntrospectableM2M-%{version}
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
