%global source0_hash 50fa76d827e119a80e2c86a5196ac4354e556f80b0a4fa440f69e1057b37faa1

Name:           ois
Version:        1.3.0
Release:        32%{?dist}
Summary:        Open Input System, OO gaming input library
License:        zlib
URL:            http://sourceforge.net/projects/wgois
Source0:        http://downloads.sourceforge.net/wgois/%{name}_v1-3.tar.gz
Patch0:         ois-gcc47.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libtool libXaw-devel

%description
Object Oriented Input System (OIS) is meant to be a cross platform, simple
solution for using all kinds of Input Devices (KeyBoards, Mice, Joysticks, etc)
and feedback devices (e.g. forcefeedback). Written in C++ using Object Oriented
Design patterns.

%package        devel
Summary:        Development files for %{name}
Requires:       pkgconfig, %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ois-v1-3
%patch -P0
chmod -x `find includes -type f` `find src -type f` ReadMe.txt
sed "s|\r||g" ReadMe.txt > ReadMe.txt.new
touch -r ReadMe.txt ReadMe.txt.new
mv ReadMe.txt.new ReadMe.txt
sh bootstrap

%build
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc ReadMe.txt
%{_libdir}/libOIS-1.3.0.so

%files devel
%{_includedir}/OIS
%{_libdir}/libOIS.so
%{_libdir}/pkgconfig/OIS.pc

%changelog
%autochangelog
