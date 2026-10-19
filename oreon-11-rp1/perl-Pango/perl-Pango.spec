%global source0_hash 34b0a422df3fecd7597587048552457d48ae764c43bbefd2a9d62ceb6c8bac71
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global use_x11_tests 1
Name:           perl-Pango
Version:        1.227
Release:        43%{?dist}
Summary:        Perl interface to the pango library
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Pango
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Pango-%{version}.tar.gz
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(Cairo) >= 1.000
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  perl(Cairo)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::CodeGen)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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
%oreon_autofiles main

%check

    xvfb-run -a make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
