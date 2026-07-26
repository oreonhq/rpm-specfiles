%global source0_hash 087186c3693acf196451cf59cc8b7f5cf9a7b05abe20d32dcbcba0822953fb80

Name:           perl-Gtk2-ImageView
Version:        0.05
Release:        36%{?dist}
Summary:        Perl bindings to the GtkImageView image viewer widget

License:        LGPL-3.0-or-later
URL:            https://metacpan.org/release/Gtk2-ImageView
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Gtk2-ImageView-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  gtkimageview-devel >= 1.6.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Glib) >= 1.163
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Cairo) >= 1.00
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Test::More)
Requires:       perl(Glib) >= 1.163
Requires:       perl(Cairo) >= 1.00

%description
Perl bindings to the GtkImageView image viewer widget. Find out more about 
GtkImageView at http://trac.bjourne.webfactional.com/. The Perl bindings follow 
the C API very closely, and the C reference should be considered the canonical 
documentation.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-ImageView-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# There are tests, but they need an X DISPLAY to run. Not worth it.
# make test

%files
%doc AUTHORS COPYING.LESSER README
%{perl_vendorarch}/auto/Gtk2/ImageView/
%{perl_vendorarch}/Gtk2*
%exclude %{perl_vendorarch}/Gtk2/ImageView/Install/*.h
%{_mandir}/man3/*.3pm*

%files devel
%{perl_vendorarch}/Gtk2/ImageView/Install/*.h

%changelog
%autochangelog
