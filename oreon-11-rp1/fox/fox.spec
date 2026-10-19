%global source0_hash 48f33d2dd5371c2d48f6518297f0ef5bbf3fcd37719e99f815dc6fc6e0f928ae
Name:		fox
Version:	1.6.59
Release:        1%{?dist}
Summary:        C++ based Toolkit for developing Graphical User Interfaces
License:	LGPL-2.1-or-later
URL:		http://www.fox-toolkit.org/   
Source0:        http://fox-toolkit.org/ftp/%{name}-%{version}.tar.gz
Patch0:	fox-1.6.49-adie-syspath.patch
Patch1:	fox-1.6.54-format-security.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
FOX is a C++ based Toolkit for developing Graphical User Interfaces 
easily and effectively. It offers a wide, and growing, collection of 
Controls, and provides state of the art facilities such as drag and drop,
selection, as well as OpenGL widgets for 3D graphical manipulation.
FOX also implements icons, images, and user-convenience features such as 
status line help, and tooltips.  Tooltips may even be used for 3D
objects.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	utils
Summary:	Utility applications based on %{name}
Requires:	%{name}%{?isa} = %{version}-%{release}
License:	GPL-2.0-or-later
%description	utils
This package contains some utility applications based on
%{name}.

%package	doc
Summary:	Documentation files for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
This package contains some documentation files for
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .syspath
%patch -P1 -p1 -b .format

# Honor Fedora compilar flags
touch -r configure.ac{,.timestamp}
sed -i.flags \
	-e '\@^CXXFLAGS=""@d' \
	configure.ac configure
touch -r configure.ac{.timestamp,}

for f in \
	AUTHORS \
	doc/{styles,menu}.css
do
	mv $f{,.iso}
	iconv -f ISO-8859-1 -t UTF-8 -o $f{,.iso}
	touch -r $f{.iso,}
	rm -f $f.iso
done

%build

%configure \
	--disable-static \
	%{nil}
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/lib*.la
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_bindir}/Adie.stx %{buildroot}%{_datadir}/%{name}/
chmod 0644 %{buildroot}%{_datadir}/%{name}/Adie.stx
mv \
	%{buildroot}/%{_bindir}/fox-config \
	%{buildroot}/%{_bindir}/fox-config.$(arch)
cat > %{buildroot}/%{_bindir}/fox-config <<EOF
exec %{_bindir}/fox-config.\$(arch) \$@
EOF
chmod 0755 %{buildroot}%{_bindir}/fox-config
mkdir -p %{buildroot}%{_libexecdir}/fox
mkdir -p %{buildroot}%{_datadir}/applications
for bin in %{buildroot}%{_bindir}/*
do
	name=$(basename $bin)
	[ "${name%.stx}" = "${name}" ] || continue
	[ "${name#fox-config}" = "${name}" ] || continue
	mv %{buildroot}%{_bindir}/${name} %{buildroot}%{_libexecdir}/fox/
	cat > %{buildroot}%{_bindir}/fox-${name} <<EOF
export PATH=%{_libexecdir}/%{name}:\$PATH
exec ${name} \$@
EOF
	chmod 0755 %{buildroot}%{_bindir}/fox-${name}
	mv %{buildroot}/%{_mandir}/man1/{,fox-}$name.1
	[ "$name" = reswrap ] && continue
	[ "$name" = adie ] && EXTRA_CATEGORY="TextEditor;"
	cat > %{buildroot}%{_datadir}/applications/fox-${name}.desktop <<EOF
[Desktop Entry]
Name=fox-${name}
Comment=${name}
TryExec=fox-${name}
Exec=fox-${name}
Terminal=false
Type=Application
Categories=Utility;$EXTRA_CATEGORY
EOF
	desktop-file-validate %{buildroot}%{_datadir}/applications/fox-${name}.desktop
done
rm -rf doc-files
mkdir doc-files
mv %{buildroot}%{_docdir}/%{name}-*/html doc-files
rm -f doc-files/html/filter.pl
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

exit 0
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n fox-devel -f %{oreon_filedir}/fox-devel.list
%files -n fox-utils -f %{oreon_filedir}/fox-utils.list
%files -n fox-doc -f %{oreon_filedir}/fox-doc.list

%changelog

%autochangelog
