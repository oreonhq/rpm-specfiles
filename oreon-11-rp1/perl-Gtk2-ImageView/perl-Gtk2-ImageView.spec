%global source0_hash 087186c3693acf196451cf59cc8b7f5cf9a7b05abe20d32dcbcba0822953fb80
Name:           perl-Gtk2-ImageView
Version:        0.05
Release:        1%{?dist}
Summary:        Perl bindings to the GtkImageView image viewer widget
License:        LGPL-3.0-or-later
URL:            https://metacpan.org/release/Gtk2-ImageView
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Gtk2-ImageView-%{version}.tar.gz
Requires:       perl(Glib) >= 1.163
Requires:       perl(Cairo) >= 1.00
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  gtkimageview-devel
BuildRequires:  make
BuildRequires:  perl(Cairo)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n perl-Gtk2-ImageView-devel -f %{oreon_filedir}/perl-Gtk2-ImageView-devel.list

%changelog

%autochangelog
