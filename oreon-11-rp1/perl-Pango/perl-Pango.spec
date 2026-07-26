%global source0_hash 34b0a422df3fecd7597587048552457d48ae764c43bbefd2a9d62ceb6c8bac71

%global use_x11_tests 1

Name:           perl-Pango
Version:        1.227
Release:        43%{?dist}
Summary:        Perl interface to the pango library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Pango
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Pango-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pango-devel >= 1.0.0
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Cairo) >= 1.000
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.300 
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib) >= 1.220
BuildRequires:  perl(Glib::CodeGen)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
# Run-time:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests:
%if %{use_x11_tests}
BuildRequires:  font(:lang=en)
%if !%{defined perl_bootstrap}
# Break build-cycle: perl-Gtk2 → perl-Pango → perl-Gtk2
BuildRequires:  perl(Gtk2) >= 1.220
%endif
BuildRequires:  xorg-x11-server-Xvfb
%endif
Requires:       perl(Cairo) >= 1.000

%{?perl_default_filter}

%description
perl-Pango provides Perl bindings for the text layout/rendering library 
pango. Pango is a library for laying out and rendering text, with an 
emphasis on internationalization. Pango can be used anywhere that text layout 
is needed, but using Pango in conjunction with Cairo and/or Gtk2 provides a 
complete solution with high quality text handling and graphics rendering.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pango-%{version}
chmod -c a-x examples/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%if %{use_x11_tests}
    xvfb-run -a make test
%else
    make test
%endif

%files
%license LICENSE
%doc NEWS README examples/
%{perl_vendorarch}/Pango*
%{perl_vendorarch}/auto/Pango/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
