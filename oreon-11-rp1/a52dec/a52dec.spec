Summary:    Small test program for liba52
Name:       a52dec
Version:    0.7.4
Release:    53%{?dist}
License:    GPL-2.0-only
URL:        http://liba52.sourceforge.net
# Debian upstream orig tarball (same a52dec-0.7.4 tree as upstream releases)
Source0:    https://deb.debian.org/debian/pool/main/a/a52dec/a52dec_%{version}.orig.tar.gz
Patch0:     a52dec-configure-optflags.patch
Patch2:     liba52-silence.patch

BuildRequires: autoconf automake libtool
BuildRequires: gcc
BuildRequires: make

Requires:   liba52%{?_isa} = %{version}-%{release}
#Multilib transition
#Introduced in Fedora 26, can be dropped in Fedora 28
Obsoletes:  %{name} < 0.7.4-25


%package -n liba52
Summary:    A free ATSC A/52 stream decoder, also known as AC-3 or AC3
#Fix multilibs transition - introduced in f26
Obsoletes:  a52dec < 0.7.4-25
#Fix others 3rd part repos transition
Obsoletes:  a52dec-libs < 0.7.4-25
Provides:   a52dec-libs = %{version}-%{release}

%package -n liba52-devel
Summary:    Development files for liba52
Requires:   liba52%{?_isa} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
Obsoletes:  %{name}-devel < 0.7.4-25

%description
Small test program for liba52.

%description -n liba52
liba52 is a free library for decoding ATSC A/52 streams. The A/52
standard is used in a variety of applications, including digital
television and DVD. It is also known as AC-3 or AC3

%description -n liba52-devel
The liba52-devel package contains libraries and header files for
developing applications that use liba52-devel.


%prep
%autosetup -p1

sed -i -e 's/-prefer-non-pic/-prefer-pic/' liba52/configure.incl

# regenerate autotools
autoreconf -fiv

# Convert to utf-8
for file in AUTHORS; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done


%build
%configure --enable-shared --disable-static
%make_build


%install
%make_install


%ldconfig_scriptlets -n liba52


%files
%exclude %{_libdir}/liba52.la
%doc AUTHORS ChangeLog HISTORY NEWS TODO
%{_bindir}/%{name}
%{_bindir}/extract_a52
%{_mandir}/man1/a52dec.1*
%{_mandir}/man1/extract_a52.1*

%files -n liba52
%license COPYING
%{_libdir}/liba52.so.*

%files -n liba52-devel
%doc doc/liba52.txt
%{_includedir}/%{name}
%{_libdir}/liba52.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.4-53
- Prepare for Oreon 11 (RP1)
