%global source0_hash a49b08d56813789e5f03289a3f949459eafe9e40a1a9fc066c42c90009a322cf
Summary:        Internationalization library for Perl, compatible with gettext
Name:           perl-libintl-perl
Version:        1.37
Release:        1%{?dist}
License:        GPL-3.0-or-later AND LGPL-2.0-or-later
URL:            https://metacpan.org/release/libintl-perl
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIDO/libintl-perl-%{version}.tar.gz
Provides:       perl-libintl = %{version}-%{release}
Obsoletes:      perl-libintl < 1.25
Requires:       perl(Carp)
Requires:       perl(Encode::Alias)
Requires:       perl(POSIX)
Recommends:     perl(File::ShareDir)
Recommends:     perl(I18N::Langinfo)
%{?perl_default_filter}
Provides:       perl(Locale::TextDomain)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  glibc-langpack-de
BuildRequires:  glibc-langpack-en
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
The package libintl-perl is an internationalization library for Perl that
aims to be compatible with the Uniforum message translations system as
implemented for example in GNU gettext.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libintl-perl-%{version}
find -type f -exec chmod -x {} \;
find lib/Locale gettext_xs \( -name '*.pm' -o -name '*.pod' \) \
    -exec sed -i -e '/^#! \/bin\/false/d' {} \;
# Fix rpmlint errors and warnings
cd sample/simplecal
sed -i -e '1i#!%{__perl}' bin/simplecal.pl Makefile.PL
for file in po/*.po; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    mv $file.new $file
done
rm .gitignore MANIFEST

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PERLLOCAL=1
%make_build
%install
%make_install
/usr/bin/find %{buildroot} -type f \( -name .packlist -o \
                  -name '*.bs' -size 0 \) -delete
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.37-1
- Prepare for Oreon 11 (RP1)
