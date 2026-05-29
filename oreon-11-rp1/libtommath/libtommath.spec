%global source0_hash 0e9247ab1c4e64110024e34082ce8401f089f7df8e40de0b1ce6a03641302d56

Name:           libtommath
Version:        1.3.1~rc1
Release:        %autorelease
Summary:        A portable number theoretic multiple-precision integer library
License:        Unlicense
URL:            https://www.libtom.net/

Source0:        https://github.com/libtom/libtommath/archive/v%{version_no_tilde}.tar.gz#/libtommath-%{version_no_tilde}.tar.gz

BuildRequires:  make
BuildRequires:  libtool

%if ! 0%{?flatpak}
BuildRequires:  ghostscript
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  libtiff-tools
BuildRequires:  tex(amssymb.sty)
BuildRequires:  tex(epstopdf-base.sty)
BuildRequires:  tex(expl3.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(hyphen.tex)
BuildRequires:  tex(l3backend-dvips.def)
BuildRequires:  texlive-cm
BuildRequires:  texlive-appendix
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-kpathsea
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  texlive-makeindex-bin
BuildRequires:  texlive-metafont
BuildRequires:  texlive-mfware-bin
%endif

%description
A free open source portable number theoretic multiple-precision integer library
written entirely in C. (phew!). The library is designed to provide a simple to
work with API that provides fairly efficient routines that build out of the box
without configuration.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%if ! 0%{?flatpak}
%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
Provides:       %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < 0.42-1

%description    doc
The %{name}-doc package contains PDF documentation for using %{name}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{version_no_tilde}
# Fix permissions on installed library
sed -i -e 's/644 $(LIBNAME)/755 $(LIBNAME)/g' makefile.shared
# Fix pkgconfig path
sed -i \
    -e 's|^prefix=.*|prefix=%{_prefix}|g' \
    -e 's|^libdir=.*|libdir=%{_libdir}|g' \
    %{name}.pc.in

%build
%set_build_flags
%make_build V=1 CFLAGS="$CFLAGS -I./" -f makefile.shared
%if ! 0%{?flatpak}
make V=1 -f makefile manual docs
%endif

%check
make test
./test

%install
%make_install V=1 CFLAGS="$CFLAGS -I./" PREFIX=%{_prefix} LIBPATH=%{_libdir} -f makefile.shared

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%if ! 0%{?flatpak}
%files doc
%doc doc/bn.pdf
%endif

%changelog
* Sat May 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1~rc1-1
- Import libtommath
