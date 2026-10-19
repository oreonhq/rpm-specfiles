%global source0_hash ba806736ebcc9de3d8141a763a682bdeabb1cb8702bde299adfd574ace875052
%global tarname GooCanvas2-CairoTypes
Name:           perl-GooCanvas2-CairoTypes
Version:        0.001
Release:        21%{?dist}
Summary:        Bridge between GooCanvas2 and Cairo types
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/GooCanvas2-CairoTypes
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASOKOLOV/GooCanvas2-CairoTypes-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Cairo::Install::Files)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Glib-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(goocanvas-2.0)
# /oreon:deps
%description
There is an issue in the interaction between GooCanvas, GObject
Introspection, Cairo, and their Perl bindings, which causes some
functionality to be unusable from Perl side. This is better described
here
<https://stackoverflow.com/questions/64625955/cairosolidpattern-is-not-o
f-type-goocanvas2cairopattern>, and there was an attempt
<https://gitlab.gnome.org/GNOME/goocanvas/-/merge_requests/9> to fix it
upstream. Until it's fixed, this can serve as a workaround for it.

Currently this module only "fixes"
"Cairo::Pattern/GooCanvas2::CairoPattern" interop. For certain calls it
just works if this module was included; for some other calls you need to
explicitly convert the type.

If you have any idea how to fix those cases to not require such call, or
need to bridge more types, pull requests
<https://github.com/DarthGandalf/GooCanvas2-CairoTypes> are welcome!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{tarname}-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
