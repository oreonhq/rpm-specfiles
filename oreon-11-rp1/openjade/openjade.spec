%global source0_hash 1d2d7996cc94f9b87d0c51cf0e028070ac177c4123ecbfd7ac1cb8d0b7d322d1

Summary: A DSSSL implementation
Name: openjade
Version: 1.3.2
Release: 85%{?dist}
Requires: sgml-common
URL: http://openjade.sourceforge.net/
Source:        http://download.sourceforge.net/openjade/openjade-%{version}.tar.gz

# I can't get them from autoreconf, because of the very strange openjade structure of config files
# 'config.sub' and 'config.guess' from upstream sources (2023-01-21 and 2023-01-01 respectivelly).
# https://git.savannah.gnu.org/cgit/config.git/plain/config.guess
Source2: config.guess
# https://git.savannah.gnu.org/cgit/config.git/plain/config.sub
Source3: config.sub

# Fix build on ppc64
Patch0: openjade-ppc64.patch

# Do not link against -lnsl
Patch1: openjade-1.3.1-nsl.patch

# Fix dependent libs for libogrove (bug #198232).
Patch2: openjade-deplibs.patch

# Do not require OpenSP libosp.la file for build(#485114)
Patch3: openjade-nola.patch

# Upstream bug tracker fix for build with gcc46
Patch4: openjade-1.3.2-gcc46.patch

# Use Getopt:Std to prevent build failure
Patch5: openjade-getoptperl.patch

Patch6: openjade-configure-c99.patch
License: LicenseRef-DMIT

# Last jade version is from Red Hat 6.2
Provides: jade = %{version}-%{release}

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: opensp-devel

BuildRequires: perl-interpreter
BuildRequires: perl-POSIX
BuildRequires: perl-Getopt-Std

%description
OpenJade is an implementation of the ISO/IEC 10179:1996 standard DSSSL
(Document Style Semantics and Specification Language). OpenJade is
based on James Clark's Jade implementation of DSSSL. OpenJade is a
command-line application and a set of components. The DSSSL engine
inputs an SGML or XML document and can output a variety of formats:
XML, RTF, TeX, MIF (FrameMaker), SGML, or XML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1


%build
cp -p %{SOURCE2} %{SOURCE3} config/
# more info: rhbz#1306162
export CXXFLAGS="%optflags -fno-lifetime-dse"
%configure --disable-static --datadir=%{_datadir}/sgml/%{name}-%{version} \
	--enable-splibdir=%{_libdir}
# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make


%install
rm -rf %{buildroot}

make install install-man DESTDIR=%{buildroot}

# oMy, othis ois osilly., oyes
ln -s openjade %{buildroot}/%{_bindir}/jade
echo ".so man1/openjade.1" > %{buildroot}/%{_mandir}/man1/jade.1

# Install jade/jade %%{buildroot}/%%{prefix}/bin/jade
cp dsssl/catalog %{buildroot}/%{_datadir}/sgml/%{name}-%{version}/
cp dsssl/{dsssl,style-sheet,fot}.dtd %{buildroot}/%{_datadir}/sgml/%{name}-%{version}/

# Add unversioned/versioned catalog and symlink
mkdir -p %{buildroot}/etc/sgml
pushd %{buildroot}/etc/sgml
touch %{name}-%{version}-%{release}.soc
ln -s %{name}-%{version}-%{release}.soc %{name}.soc
popd

rm -f %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/*.la

%post
%{?ldconfig}
%{_bindir}/install-catalog --add %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
    %{_datadir}/sgml/%{name}-%{version}/catalog >/dev/null 2>/dev/null || :

%preun
%{_bindir}/install-catalog --remove %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
    %{_datadir}/sgml/%{name}-%{version}/catalog >/dev/null 2>/dev/null || :

# The install-catalog removes the file making uninstallation throw a warning about removing a non-existent file
# This file creation suppresses the warning (rhbz#2193429)
touch %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc 

%files
%doc jadedoc/* dsssl/README.jadetex
%doc README COPYING VERSION

# Removed %%ghost for succesful instalation on OSTree (rhbz#2193429)
%verify(not size filedigest mtime) %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
%{_sysconfdir}/sgml/%{name}.soc
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/*/*
%{_datadir}/sgml/%{name}-%{version}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-85
- Prepare for Oreon 11 (RP1)
