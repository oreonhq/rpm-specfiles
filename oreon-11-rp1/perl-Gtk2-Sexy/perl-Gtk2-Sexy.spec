%global source0_hash 96f64279424d640c4d60e7d820e55c1fd4cff32588cf40db0e3e70bde0796f3c

%global use_x11_tests 1

Name:           perl-Gtk2-Sexy
Version:        0.05
Release:        58%{?dist}
Summary:        Perl interface to the sexy widget collection 
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Gtk2-Sexy
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/Gtk2-Sexy-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Gtk2::CodeGen)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ExtraTests)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(libsexy)
# Run-time:
BuildRequires:  perl(DynaLoader)
# Tests:
BuildRequires:  perl(Gtk2::TestHelper)
# Optional tests:
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif

%description
This module allows a perl developer to access the widgets of the sexy widget
collection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Sexy-%{version}
# keep rpmlint happy...
chmod -x examples/*
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
%if %{use_x11_tests}
    xvfb-run -d make test
%else
    make test
%endif

%files
%doc ChangeLog examples/ README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
%autochangelog
