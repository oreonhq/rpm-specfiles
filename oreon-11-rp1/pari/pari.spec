%global source1_hash 983e60f7fc2ab841ce1e10a20a7299feb39c371ddec508c8e7038f89e38b007c
%global source0_hash 02651d99c391007d384b3fadbc20abc6916b77036f9e496c99e9ce8688ca4b53
Name:           pari
Version:        2.17.4
Release:        1%{?dist}
Summary:        Number Theory-oriented Computer Algebra System
%global majver %(cut -d. -f1-2 <<< %{version})
License:        GPL-2.0-or-later
URL:            https://pari.math.u-bordeaux.fr/
VCS:            git:https://pari.math.u-bordeaux.fr/git/pari.git
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/unix/%{name}-%{version}.tar.gz
Source1:        https://pari.math.u-bordeaux.fr/pub/pari/unix/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
Source3:        fr.u-bordeaux.math.pari.desktop
Source4:        pari-gp.xpm
Source5:        pari.abignore
Source6:        fr.u-bordeaux.math.pari.metainfo.xml
Patch:          pari-2.17.0-xdgopen.patch
Patch:          pari-2.9.0-missing-field-init.patch
Patch:          pari-2.17.0-declaration-not-prototype.patch
%global __provides_exclude_from ^%{_datadir}/pari/PARI/
%global __requires_exclude_from ^%{_datadir}/pari/PARI/
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gpgverify
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pari-elldata
BuildRequires:  pari-galdata
BuildRequires:  pari-galpol
BuildRequires:  pari-nflistdata
BuildRequires:  pari-seadata
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(readline)
BuildRequires:  sed
BuildRequires:  tex(latex)
# /oreon:deps
%description
PARI is a widely used computer algebra system designed for fast computations in
number theory (factorizations, algebraic number theory, elliptic curves...),
but also contains a large number of other useful functions to compute with
mathematical entities such as matrices, polynomials, power series, algebraic
numbers, etc., and a lot of transcendental functions.

This package contains the shared libraries.  The interactive calculator
PARI/GP is in package pari-gp.

%package devel
Summary:        Header files and libraries for PARI development
Requires:       %{name} = %{version}-%{release}
%description devel
Header files and libraries for PARI development.

%package gp
Summary:        PARI calculator
Requires:       %{name} = %{version}-%{release}
Requires:       bzip2
Requires:       gzip
Requires:       xdg-utils
Requires:       mimehandler(application/x-dvi)
%description gp
PARI/GP is an advanced programmable calculator, which computes symbolically as
long as possible, numerically where needed, and contains a wealth of
number-theoretic functions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}

%autosetup -p0

# Silence abidiff warnings about the size of functions_basic[] changing
cp -p %{SOURCE5} .

%conf
# Avoid unwanted rpaths
sed -i "s|runpathprefix='.*'|runpathprefix=''|" config/get_ld

%build

./Configure \
    --prefix=%{_prefix} \
    --share-prefix=%{_datadir} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir}/man1 \
    --datadir=%{_datadir}/pari \
    --includedir=%{_includedir} \
%if 0%{?__isa_bits} == 64
    --mt=pthread \
%endif
    --enable-tls \
    --with-fltk \
    --with-gmp
%make_build gp
%install
%make_install INSTALL="install -p" STRIP=%{_bindir}/true
if [ "%{_lib}" != "lib" ]; then
    mkdir -p %{buildroot}%{_libdir}
    mv %{buildroot}%{_prefix}/lib/pari %{buildroot}%{_libdir}
fi
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m 644 misc/gprc.dft %{buildroot}%{_sysconfdir}/gprc
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE3}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE6} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/fr.u-bordeaux.math.pari.metainfo.xml
sed -e 's|%{build_cxxflags}|%{extension_cxxflags}|' \
    -e 's|%{build_ldflags}|%{extension_ldflags}|' \
    -i %{buildroot}%{_libdir}/pari/pari.cfg
%ifnarch %{ix86}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test-all
%endif
%files -f %{oreon_filedir}/main.list
%files -n pari-devel -f %{oreon_filedir}/pari-devel.list
%files -n pari-gp -f %{oreon_filedir}/pari-gp.list

%changelog

%autochangelog
