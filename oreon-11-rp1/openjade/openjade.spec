%global source0_hash 1d2d7996cc94f9b87d0c51cf0e028070ac177c4123ecbfd7ac1cb8d0b7d322d1
Summary:        A DSSSL implementation
Name: openjade
Version: 1.3.2
Release:        85%{?dist}
Requires: sgml-common
URL: http://openjade.sourceforge.net/
Source0:        http://download.sourceforge.net/openjade/openjade-%{version}.tar.gz
Source2: config.guess
Source3: config.sub
Patch0: openjade-ppc64.patch
Patch1: openjade-1.3.1-nsl.patch
Patch2: openjade-deplibs.patch
Patch3: openjade-nola.patch
Patch4: openjade-1.3.2-gcc46.patch
Patch5: openjade-getoptperl.patch
Patch6: openjade-configure-c99.patch
License: LicenseRef-DMIT
Provides: jade = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  opensp-devel
BuildRequires:  perl-Getopt-Std
BuildRequires:  perl-POSIX
BuildRequires:  perl-interpreter
# /oreon:deps
%description
OpenJade is an implementation of the ISO/IEC 10179:1996 standard DSSSL
(Document Style Semantics and Specification Language). OpenJade is
based on James Clark's Jade implementation of DSSSL. OpenJade is a
command-line application and a set of components. The DSSSL engine
inputs an SGML or XML document and can output a variety of formats:
XML, RTF, TeX, MIF (FrameMaker), SGML, or XML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

cp -p %{SOURCE2} %{SOURCE3} config/
export CXXFLAGS="%optflags -fno-lifetime-dse"
%configure --disable-static --datadir=%{_datadir}/sgml/%{name}-%{version} \
	--enable-splibdir=%{_libdir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make
%install
rm -rf %{buildroot}
make install install-man DESTDIR=%{buildroot}
ln -s openjade %{buildroot}/%{_bindir}/jade
echo ".so man1/openjade.1" > %{buildroot}/%{_mandir}/man1/jade.1
cp dsssl/catalog %{buildroot}/%{_datadir}/sgml/%{name}-%{version}/
cp dsssl/{dsssl,style-sheet,fot}.dtd %{buildroot}/%{_datadir}/sgml/%{name}-%{version}/
mkdir -p %{buildroot}/etc/sgml
pushd %{buildroot}/etc/sgml
touch %{name}-%{version}-%{release}.soc
ln -s %{name}-%{version}-%{release}.soc %{name}.soc
popd
rm -f %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/*.la
%oreon_autofiles main

%post

%{?ldconfig}
%{_bindir}/install-catalog --add %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
    %{_datadir}/sgml/%{name}-%{version}/catalog >/dev/null 2>/dev/null || :
%preun

%{_bindir}/install-catalog --remove %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
    %{_datadir}/sgml/%{name}-%{version}/catalog >/dev/null 2>/dev/null || :
touch %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc 
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-85
- Prepare for Oreon 11 (RP1)
