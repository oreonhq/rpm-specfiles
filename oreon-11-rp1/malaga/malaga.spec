%global source0_hash 8811e5feaae03e1b6e3008116fdc7471a53b6c0c5036751c637b15058f855ace

Name:           malaga
Version:        7.12 
Release:        44%{?dist}
Summary:        A programming language for automatic language analysis

License:        GPL-2.0-or-later
URL:            http://home.arcor.de/bjoern-beutel/malaga/
Source0:        https://deb.debian.org/debian/pool/main/m/malaga/malaga_7.12.orig.tar.gz
# Fix map_file symbol conflict with samba. Upstream can be considered
# inactive but as libvoikko >= 2.2 doesn't use libmalaga anymore, these kind
# of problems won't probably come up. The only executables in Fedora which
# link to libmalaga currently are the malaga tools.
Patch0:         malaga-rename-map_file.diff
# Malshow needs to be linked with -lm as Fedora's ld doesn't do implicit
# linking anymore
Patch1:         malaga-malshow-lm.patch
Patch2:         malaga-aarch64.patch
Patch3:         malaga-fix-incompatible-GtkItemFactoryCallback-pointers.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk2-devel readline-devel
Requires: lib%{name} = %{version}-%{release}

%description
A software package for the development and application of
grammars that are used for the analysis of words and sentences of natural
languages. It is a language-independent system that offers a programming
language for the modelling of the language-dependent grammatical
information. This language is also called Malaga.

Malaga is based on the grammatical theory of the "Left Associative Grammar"
(LAG), developed by Roland Hausser, professor for Computational Linguistics at
University of Erlangen, Germany.

%package        devel
Summary:        Development files for %{name}
Requires:       lib%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n	lib%{name}
Summary:        Library files for %{name}

%description -n	lib%{name}
Library files for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n malaga-7.12
# Remove "@" marks so that the build process is more verbose
sed -i.debug -e 's|^\([ \t][ \t]*\)@|\1|' Makefile.in
# Remove "-s" so binaries won't be stripped
sed -i.strip -e 's| -s | |' Makefile.in
# Make libtool output more verbose
sed -i.silent -e 's|--silent||' Makefile.in

%build
%configure --with-readline
# Remove rpath,
# 
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install DESTDIR=$RPM_BUILD_ROOT INSTALL_INFO=/sbin/install-info INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Remove static archive
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'
# Change permission of libmalaga.so*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libmalaga.so*




%files
%{_infodir}/%{name}*
%{_bindir}/mal*
%{_datadir}/%{name}
%{_mandir}/man1/mal*

%files -n lib%{name}
%doc CHANGES.txt GPL.txt README.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/malaga.h


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.12-44
- Import
