%global source0_hash 15bdfdcec58a7da30adc87ac2b078e4417dbe5392f3afb719f9ba6d062645593

%global         _hardened_build 1

%define underscore_version 2_6_2

Name:           tinyxml
Version:        2.6.2
Release:        33%{?dist}
Summary:        A simple, small, C++ XML parser
License:        zlib
URL:            http://www.grinninglizard.com/tinyxml/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}_%{underscore_version}.tar.gz
Source1:        tinyxml.pc.in
Patch0:         tinyxml-2.5.3-stl.patch
# https://sourceforge.net/p/tinyxml/patches/_discuss/thread/fa2235db/f16d/attachment/entity.patch
Patch1:         tinyxml-issue51.patch
Patch2:         https://sources.debian.org/data/main/t/tinyxml/2.6.2-6.1/debian/patches/CVE-2021-42260.patch
Patch3:         https://sources.debian.org/data/main/t/tinyxml/2.6.2-6.1/debian/patches/CVE-2023-34194.patch

BuildRequires:  gcc-c++

%description
TinyXML is a simple, small, C++ XML parser that can be easily integrating
into other programs. Have you ever found yourself writing a text file parser
every time you needed to save human readable data or serialize objects?
TinyXML solves the text I/O file once and for all.
(Or, as a friend said, ends the Just Another Text File Parser problem.)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
%{set_build_flags}
mv changes.txt changes.txt-orig
iconv -f ISO-8859-1 -t UTF-8 changes.txt-orig > changes.txt
rm -f changes.txt-orig
# Not really designed to be build as lib, DYI
for i in tinyxml.cpp tinystr.cpp tinyxmlerror.cpp tinyxmlparser.cpp; do
  ${CXX} $RPM_OPT_FLAGS -fPIC -o $i.o -c $i
done
${CXX} $RPM_LD_FLAGS -shared -o lib%{name}.so.0.%{version} \
   -Wl,-soname,lib%{name}.so.0 *.cpp.o

%install
rm -rf $RPM_BUILD_ROOT
# Not really designed to be build as lib, DYI
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 lib%{name}.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.0
ln -s lib%{name}.so.0.%{version} $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -p -m 644 %{name}.h $RPM_BUILD_ROOT%{_includedir}

mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's![@]prefix[@]!%{_prefix}!g' \
 -e 's![@]exec_prefix[@]!%{_exec_prefix}!g' \
 -e 's![@]libdir[@]!%{_libdir}!g' \
 -e 's![@]includedir[@]!%{_includedir}!g' \
 -e 's![@]version[@]!%{version}!g' \
 %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%check
%{set_build_flags}
${CXX} $RPM_OPT_FLAGS -DTIXML_USE_STL -fPIE -ltinyxml -L%{buildroot}%{_libdir} -o xmltest xmltest.cpp
chmod +x xmltest
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./xmltest

%files
%doc changes.txt readme.txt
%{_libdir}/*.so.*

%files devel
%doc docs/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
