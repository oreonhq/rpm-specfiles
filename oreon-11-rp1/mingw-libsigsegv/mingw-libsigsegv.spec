%global source0_hash c18b3b0975ec7e0a6af03a9533d7ffbdc500bb146e0ca338a6174b1346d655bb

%global __strip %{mingw32_strip}
%global __objdump %{mingw32_objdump}

Summary: MinGW library for handling page faults in user mode
Name:    mingw-libsigsegv
Version: 2.6
Release: 33%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://libsigsegv.sourceforge.net/
Source0: http://ftp.gnu.org/gnu/libsigsegv/libsigsegv-%{version}.tar.gz

## upstream patches
# based on:
# http://git.savannah.gnu.org/cgit/libsigsegv.git/patch/?id=4f14ef87b2fba9718c1a88b9ed9ca7ba111d60da
# http://git.savannah.gnu.org/cgit/libsigsegv.git/patch/?id=54b612e978e26a52b5706272dabf84ed9d895fa7
Patch100: libsigsegv-2.6-mystack.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  autoconf automake libtool
BuildRequires:  mingw32-filesystem >= 56
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc

%description
MinGW library for handling memory faults and stack overflows in user mode.

%package -n mingw32-libsigsegv
Summary:        MinGW library for handling page faults in user mode

%description -n mingw32-libsigsegv
MinGW library for handling memory faults and stack overflows in user mode.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libsigsegv-%{version}

%patch -P100 -p1 -b .mystack
autoreconf --install --force

%build
%{mingw32_configure} --disable-static --enable-shared
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-libsigsegv
%doc AUTHORS COPYING NEWS README
%{mingw32_bindir}/libsigsegv-0.dll
%{mingw32_libdir}/libsigsegv.dll.a
%{mingw32_includedir}/*.h

%changelog
%autochangelog
