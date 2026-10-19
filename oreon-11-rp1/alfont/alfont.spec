%global source0_hash 50ef05bcb8eebf62db362c4e039a752b9eb4e87b4e15cf80d364c96e9774d882
Name:           alfont
Version:        2.0.9
Release:        1%{?dist}
Summary:        Font rendering library for the Allegro game library
License:        FTL
URL:            http://chernsha.sitesled.com/
Source0:        %{name}-%{version}.tar.gz
Patch0:         alfont-2.0.9-linux.patch
Patch1:         alfont-2.0.9-remove-alfont_get_string.patch
Patch2:         alfont-2.0.9-build-fixes.patch
# oreon:deps
BuildRequires:  allegro-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
# /oreon:deps
%description
alfont also known as AllegroFont or AlFont is a wrapper around the freetype2
library for use with the Allegro game library. Thus allowing the display of
text using freetype fonts on Allegro bitmaps.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       allegro-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for i in include/alfont*.h freetype/docs/FTL.TXT; do
    sed -i.orig s'/\r//g' $i
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.utf8
    mv $i.utf8 $i
    touch -r $i.orig $i
done

%build

gcc -fPIC -DPIC $RPM_OPT_FLAGS -Iinclude `freetype-config --cflags` \
  -o src/alfont.o -c src/alfont.c
gcc -shared -Wl,-soname,lib%{name}.so.2 -o lib%{name}.so.%{version} \
  $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  src/alfont.o $(freetype-config --libs) $(allegro-config --libs)
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 lib%{name}.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.2
ln -s lib%{name}.so.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -m 644 include/%{name}*.h $RPM_BUILD_ROOT%{_includedir}
%ldconfig_scriptlets
%oreon_autofiles alfont-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n alfont-devel -f %{oreon_filedir}/alfont-devel.list

%changelog

%autochangelog
