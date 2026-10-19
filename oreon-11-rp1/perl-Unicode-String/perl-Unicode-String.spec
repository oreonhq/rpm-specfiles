%global source0_hash 894a110ece479546af8afec0972eec7320c86c4dea4e6b354dff3c7526ba9b68
Name:           perl-Unicode-String
Version:        2.10
Release:        1%{?dist}
Summary:        Perl modules to handle various Unicode issues
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Unicode-String
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/Unicode-String-%{version}.tar.gz
Patch0:         perl-Unicode-String-2.09-utf8doc.patch
Requires:       perl(MIME::Base64)
%{?perl_default_filter}
Provides:       perl(Unicode::String)
Provides:       perl(Unicode::CharName)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Unicode-String-%{version}

# Recode documentation as UTF-8
# Can't just use iconv because README includes an example of
# character code conversion that would be wrong if simply recoded
%patch -P0 -p1

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"
%install
make install \
  DESTDIR=$RPM_BUILD_ROOT \
  INSTALLARCHLIB=$RPM_BUILD_ROOT%{perl_archlib}
find $RPM_BUILD_ROOT -type f \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -empty \) \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -empty -exec rmdir {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
