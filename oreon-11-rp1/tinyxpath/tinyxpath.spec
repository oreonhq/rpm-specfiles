%global source0_hash c1ea02fffed6f2353870c96b41f62c382ebc0812997322ab8683d016e4ea126b
Name:           tinyxpath
Version:        1.3.1
Release:        26%{?dist}
Summary:        Small XPath syntax decoder
License:        zlib
URL:            http://tinyxpath.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_1_3_1.zip
Patch0:         %{name}.remove_bundled_tinyxml.patch
Patch1:         %name.fix_test.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  tinyxml-devel
# /oreon:deps
%description
TinyXPath is a small footprint XPath syntax decoder, written in C++.
- Syntax decoding
- Application to a TinyXML tree
- Function to extract a result from a tree (string, node set or integer)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       tinyxml-devel
%description    devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version}
%patch -P0
%patch -P1
rm -rf tinyxml* tinystr*

# Correct some errors due to bundled tinyxml
sed -i 's+TiXmlNode::+TiXmlNode::TINYXML_+g' *.cpp
sed -i 's+#include "tinystr.h"+//#include "tinystr.h"+g' *.h

# Fix wrong EOF encoding
sed -i 's/\r$//' AUTHORS

%build

make -f Makefile.configure
%configure CPPFLAGS="-fPIC"
make %{?_smp_mflags}
g++ $RPM_OPT_FLAGS -shared -o lib%{name}.so.0.1 \
   -Wl,-soname,lib%{name}.so.0.1 `ls *.o | grep -v main.o` -ltinyxml
%check

./tinyxpath
BEFORE=($(grep "<tr><td>" out.htm | sed 's~<td>~_~' | sed 's~</td><td>~_~g' | sed 's~</td></tr>~~' | cut -d '_' -f 3))
AFTER=($(grep "<tr><td>" out.htm | sed 's~<td>~_~' | sed 's~</td><td>~_~g' | sed 's~</td></tr>~~' | cut -d '_' -f 4))
COUNT=0
TOTAL=$(grep "<tr><td>" out.htm | sed 's~<td>~_~' | sed 's~</td><td>~_~g' | sed 's~</td></tr>~~' | cut -d '_' -f 3 | wc -l)
while [ $COUNT -lt $TOTAL ]; do
  if [ -z "${AFTER[$COUNT]}" ] || [ "${AFTER[$COUNT]}" != "${BEFORE[$COUNT]}" ]
  then
    echo "Before: ${BEFORE[$COUNT]} After: ${AFTER[$COUNT]}"
    false
    break
  fi
  COUNT=$(($COUNT + 1))
done
%install
%make_install
mkdir -p %{buildroot}%{_includedir}/%{name}
install -pDm644 *.h %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}
install -m 755 lib%{name}.so.0.1 %{buildroot}%{_libdir}
ln -s lib%{name}.so.0.1 %{buildroot}%{_libdir}/lib%{name}.so.0
ln -s lib%{name}.so.0.1 %{buildroot}%{_libdir}/lib%{name}.so
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tinyxpath-devel -f %{oreon_filedir}/tinyxpath-devel.list

%changelog

%autochangelog
