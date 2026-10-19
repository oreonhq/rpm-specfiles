%global source0_hash 070e639398fda1a4665b3291e5ea80f2ba280d9bffd50656ad8482d471b96965
%global giturl  https://github.com/4ti2/4ti2
Name:           4ti2
Version:        1.6.15
Release:        1%{?dist}
Summary:        Algebraic, geometric and combinatorial problems on linear spaces
%global relver  %{gsub %version %. _}
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
SourceLicense:  GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-macro AND GPL-2.0-or-later WITH Libtool-exception AND (GPL-2.0-or-later OR MIT) AND GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later WITH Autoconf-exception-macro AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND LicenseRef-Fedora-Public-Domain
URL:            https://4ti2.github.io/
VCS:            git:%{giturl}.git
Source0:        https://github.com/%{name}/%{name}/releases/download/Release_1_6_15/%{name}-%{version}.tar.gz
Source1:        4ti2.module.in
ExcludeArch:	%{ix86}
Provides:       bundled(gnulib)
Requires:       4ti2-libs%{?_isa} = %{version}-%{release}
Requires:       environment(modules)
# oreon:deps
BuildRequires:  environment-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(epic.sty)
BuildRequires:  tex(latex)
# /oreon:deps
%description
A software package for algebraic, geometric and combinatorial problems on
linear spaces.

This package uses Environment Modules.  Prior to invoking the binaries, you
must run "module load 4ti2-%{_arch}" to modify your PATH.

%package devel
Summary:        Headers needed to develop software that uses 4ti2
License:        GPL-2.0-or-later
Requires:       4ti2-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description devel
Headers and library files needed to develop software that uses 4ti2.

%package libs
Summary:        Library for problems on linear spaces
License:        GPL-2.0-or-later
%description libs
A library for algebraic, geometric and combinatorial problems on linear
spaces.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Fix encodings
iconv -f ISO8859-1 -t UTF-8 NEWS > NEWS.utf8
touch -r NEWS NEWS.utf8
mv -f NEWS.utf8 NEWS

%configure --enable-shared --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%build

%make_build
export LD_LIBRARY_PATH=$PWD/src/4ti2/.libs:$PWD/src/fiber/.libs:$PWD/src/groebner/.libs:$PWD/src/ppi/.libs:$PWD/src/util/.libs:$PWD/src/zsolve/.libs
cd doc
make update-manual
bibtex 4ti2_manual
pdflatex 4ti2_manual
pdflatex 4ti2_manual
cd -
%install
%make_install
mkdir -p %{buildroot}%{_includedir}/tmp
mv %{buildroot}%{_includedir}/{4ti2,groebner,util,zsolve} \
   %{buildroot}%{_includedir}/tmp
mv %{buildroot}%{_includedir}/tmp %{buildroot}%{_includedir}/4ti2
mkdir -p %{buildroot}%{_libdir}/4ti2
mv %{buildroot}%{_bindir} %{buildroot}%{_libdir}/4ti2
mkdir -p %{buildroot}%{_modulesdir}
sed 's#@LIBDIR@#'%{_libdir}/4ti2'#g;' < %SOURCE1 >%{buildroot}%{_modulesdir}/4ti2-%{_arch}
rm -fr %{buildroot}%{_datadir}/4ti2/doc
%oreon_autofiles 4ti2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles 4ti2-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check
%files -f %{oreon_filedir}/main.list
%files -n 4ti2-devel -f %{oreon_filedir}/4ti2-devel.list
%files -n 4ti2-libs -f %{oreon_filedir}/4ti2-libs.list

%changelog

%autochangelog
