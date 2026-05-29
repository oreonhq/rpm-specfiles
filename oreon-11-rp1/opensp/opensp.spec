%global source0_hash 57f4898498a368918b0d49c826aa434bb5b703d2c3b169beb348016ab25617ce

Summary: SGML and XML parser
Name: opensp
Version: 1.5.2
Release: 50%{?dist}
Requires: sgml-common >= 0.5
Provides: bundled(gettext) = 0.14.5
URL: http://openjade.sourceforge.net/
Source:        http://download.sourceforge.net/openjade/OpenSP-1.5.2.tar.gz
Patch0: opensp-multilib.patch
Patch1: opensp-nodeids.patch
Patch2: opensp-sigsegv.patch
Patch3: opensp-manpage.patch
Patch4: opensp-configure-c99.patch
License: X11

BuildRequires: make
BuildRequires:  gcc-c++

%if ! 0%{?_module_build}
BuildRequires: xmlto, jadetex
%endif

%description
OpenSP is an implementation of the ISO/IEC 8879:1986 standard SGML
(Standard Generalized Markup Language). OpenSP is based on James
Clark's SP implementation of SGML. OpenSP is a command-line
application and a set of components, including a generic API.

%package devel
Summary: Files for developing applications that use OpenSP
Requires: %{name} = %{version}-%{release}

%description devel
Header files and libtool library for developing applications that use OpenSP.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n OpenSP-%{version}
%patch -P0 -p1 -b .multilib
%patch -P1 -p1 -b .nodeids
%patch -P2 -p1 -b .sigsegv
%patch -P3 -p1 -b .manpage
%patch -P4 -p1 -b .configure-c99
# convert files to UTF-8
iconv -f latin1 -t utf8 ChangeLog -o ChangeLog.tmp
mv -f ChangeLog.tmp ChangeLog

# ensure that applying the above patches doesn't cause lib/parser_inst.cxx to
# be regenerated

touch lib/parser_inst.cxx

%build
%configure \
%if 0%{?_module_build}
 --disable-doc-build \
%endif
 --disable-dependency-tracking --disable-static --enable-http \
 --enable-default-catalog=/etc/sgml/catalog \
 --enable-default-search-path=/usr/share/sgml:/usr/share/xml

# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# Get rid of libtool libraries
rm $RPM_BUILD_ROOT%{_libdir}/*.la

# oMy, othis ois osilly.
for file in nsgmls sgmlnorm spam spent sx ; do
   ln -s o$file $RPM_BUILD_ROOT%{_bindir}/$file
%if ! 0%{?_module_build}
   echo ".so man1/o${file}.1" > $RPM_BUILD_ROOT%{_mandir}/man1/${file}.1
%endif
done

#
# Rename sx to sgml2xml.
mv $RPM_BUILD_ROOT%{_bindir}/sx $RPM_BUILD_ROOT%{_bindir}/sgml2xml
%if ! 0%{?_module_build}
mv $RPM_BUILD_ROOT%{_mandir}/man1/{sx,sgml2xml}.1
%endif

#
# Clean out (installed) redundant copies of the docs and DTDs.
rm -rf $RPM_BUILD_ROOT%{_docdir}/OpenSP
rm -rf $RPM_BUILD_ROOT%{_datadir}/OpenSP

%find_lang sp5

%check
make check || : # TODO: failures as of 1.5.2 :(


%ldconfig_scriptlets


%files -f sp5.lang
%if ! 0%{?_module_build}
%doc doc/*.htm
%doc docsrc/releasenotes.html
%endif
%doc AUTHORS BUGS COPYING ChangeLog NEWS README
%doc pubtext/opensp-implied.dcl
%{_bindir}/*
%{_libdir}/libosp.so.*
%if ! 0%{?_module_build}
%{_mandir}/man1/*.1*
%endif

%files devel
%{_includedir}/OpenSP/
%{_libdir}/libosp.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-50
- Prepare for Oreon 11 (RP1)
