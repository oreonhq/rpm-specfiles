%global source0_hash 3b58430172392ec75acdad5fd833ecf494c5518382bc27932f48d46dbb01cd29

%global major 5

Name:           GLee
Version:        %{major}.4.0
Release:        34%{?dist}
Summary:        GL Easy Extension library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://elf-stone.com/glee.php
Source0:        http://www.elf-stone.com/downloads/%{name}/%{name}-%{version}-src.tar.gz
Patch0:         GLee-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires: make

%description
GLee (GL Easy Extension library) is a free cross-platform extension loading
library for OpenGL. It provides seamless support for OpenGL functions up
to version 3.0 and 399 extensions. 

%package devel
Summary:        Development headers for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       mesa-libGL-devel

%description devel
Development headers for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -c %{name}-%{version}

sed -i "s|\r||g" *.h *.c *.txt
chmod -x *.h *.c *.txt
iconv -f=iso-8859-1 -t=utf-8 readme.txt > tmp && mv tmp readme.txt

sed -i -e '/${LDCONFIG}/d' Makefile.in
sed -i -e '/doc/d' Makefile.in

sed -i 's|-shared|-shared -Wl,-soname,lib%{name}.so.%{major} -fPIC|g' Makefile.in
sed -i 's|LIBNAME=.*|LIBNAME=lib%{name}.so.%{version}|g' Makefile.in

%build
%configure
%make_build

%install
install -dm755 %{buildroot}%{_includedir}/GL
install -dm755 %{buildroot}%{_libdir}
make install INCLUDEDIR=%{buildroot}%{_includedir} \
             LIBDIR=%{buildroot}%{_libdir}
ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so

%ldconfig_scriptlets

%files
%{_libdir}/lib%{name}.so.*
%doc readme.txt

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/GL/%{name}.h
%doc extensionList.txt

%changelog
%autochangelog
