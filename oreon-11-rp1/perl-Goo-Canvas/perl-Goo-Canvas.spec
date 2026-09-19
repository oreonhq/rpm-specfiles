%global source0_hash 0c588c507eed5e62d12ed1cc1e491c6ff3a1f59c4fb3d435e14214b37ab39251

Name:           perl-Goo-Canvas
Version:        0.06
Release:        61%{?dist}
Summary:        Perl interface to the GooCanvas
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Goo-Canvas
Source0:        https://cpan.metacpan.org/authors/id/Y/YE/YEWENBIN/Goo-Canvas-%{version}.tar.gz
Source1:        Changes.20090614
Patch0:         perltetris_pl-undefined.diff
Patch1:         perl-Goo-Canvas-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  goocanvas-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Cairo) >= 1.00
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.0
BuildRequires:  perl(Glib) >= 1.103
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2) >= 1.100
BuildRequires:  perl(Test::More)

%{?perl_default_filter:
%filter_from_requires /perl(Tetris/d
%filter_from_requires /perl(Mine/d
%?perl_default_filter
}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Tetris|Mine

%description
GTK+ does't has an buildin canvas widget. GooCanvas is wonderful. It is easy to use
and has powerful and extensible way to create items in canvas. Just try it.
For more documents, please read GooCanvas Manual and the demo programs provided
in the source distribution in both perl-Goo::Canvas and GooCanvas.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Goo-Canvas-%{version}
pushd bin
%patch -P0 -p0 -b .warning
popd
%patch -P1 -p1
cp -f %{SOURCE1} Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags} NOECHO=

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/perltetris.pl $RPM_BUILD_ROOT%{_bindir}/perlfangkuai.pl
mv $RPM_BUILD_ROOT%{_mandir}/man1/perltetris.pl.1 $RPM_BUILD_ROOT%{_mandir}/man1/perlfangkuai.pl.1
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes goocanvas.typemap maps README
%{_bindir}/*
%{_mandir}/man3/*.3*
%{perl_vendorarch}/Goo/
%{_mandir}/man1/*.1.gz
%{perl_vendorarch}/auto/*

%changelog
%autochangelog
