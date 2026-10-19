%global source0_hash d9375d7da8a1f17e73404ede34604341dde2abee21aa3b1119eb66d123638e25
Name:		opal
Summary:        Open Phone Abstraction Library
Version:	3.10.11
Release:        1%{?dist}
URL:		http://www.opalvoip.org/
License:	MPLv1.0
Source0:        %{name}-%{version}-clean.tar.xz
Patch0:		opal-3.10-fix-cflags.patch
Patch1:		opal-c99.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  libtheora-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  ptlib-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
# /oreon:deps
%description
Open Phone Abstraction Library, implementation of the ITU H.323
teleconferencing protocol, and successor of the openh323 library.

%package devel
Summary:	Development package for opal
Requires:	opal = %{version}-%{release}
Requires:	openssl-devel
Requires:	ptlib-devel = 2.10.11
Requires:	pkgconfig
%description devel
The opal-devel package includes the development libraries and 
header files for opal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%patch -P0 -p1 -b.cf
%patch -P1 -p1

for file in dll so bin lib exe; do 
  find . -name "*.$file" -delete
done    

%build

%configure --disable-silk
%make_build OPTCCFLAGS="$RPM_OPT_FLAGS"
%install
%make_install
rm -f %{buildroot}/%{_datadir}/opal/opal_inc.mak
rm -f %{buildroot}/%{_libdir}/libopal_s.a
mv %{buildroot}/%{_includedir}/opal/opal/buildopts.h \
   %{buildroot}/%{_includedir}/opal/opal/buildopts-%{__isa_bits}.h
cat >%{buildroot}/%{_includedir}/opal/opal/buildopts.h <<EOF
EOF
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n opal-devel -f %{oreon_filedir}/opal-devel.list

%changelog

%autochangelog
