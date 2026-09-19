%global source0_hash 73c14ad5304c509d5f9032f93d1f8435b21fd2832caf0ed0e2a3ade4b33ef07d

Name:           perl-EV-Glib
Version:        2.01
Release:        %autorelease
Summary:        Embed the GLib main loop into EV

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/EV-Glib
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/EV-Glib-%{version}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(EV) >= 2.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(glib-2.0)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module embeds the GLib main loop into Perl's EV; that is, EV will
also handle GLib events.  If you want to use GLib/Gtk+ in an EV program,
you are at the right place here.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n EV-Glib-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING
%doc README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
