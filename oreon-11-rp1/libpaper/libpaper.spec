%global source0_hash 882b1c7636052fc9a318caa20292b35616b588824b70e7053018262b29b1409a
Name:		libpaper
Version:	2.3.0
Release:        1%{?dist}
Epoch:		1
Summary:        Library and tools for handling papersize
License:	LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND GPL-3.0-or-later AND LGPL-2.0-or-later AND FSFAP
URL:		https://github.com/rrthomas/libpaper/
Source0:        https://github.com/rrthomas/libpaper/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	localepaper.c
Source2:        paperconf.1
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  gzip
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  tar
# /oreon:deps
%description
The libpaper package enables users to indicate their preferred paper
size and specifies system-wide and per-user paper size catalogues, which can
also be used directly (see paperspecs(5)).

%package devel
Summary:	Headers/Libraries for developing programs that use libpaper
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
This package contains headers and libraries that programmers will need
to develop applications which use libpaper.

%package -n paper
Summary:	Print paper size information
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}
License:	GPL-3.0-or-later AND FSFAP AND GPL-2.0-only
%description -n paper
The paper(1) utility can be used to find the user's preferred
default paper size and give information about known sizes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git
cp %{SOURCE1} src/

%build

%configure --disable-static
%make_build
pushd src
%{__cc} %{optflags} -I.. -Ilibgnu -o localepaper localepaper.c libgnu/.libs/libgnupaper.a %{_hardening_ldflags}
popd
%check

echo "Testing localepaper tool"
locale width height > expected
./src/localepaper | tr ' ' "\n" > got
diff -u expected got
%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir %{buildroot}%{_libexecdir}
install -m0755 src/localepaper %{buildroot}%{_libexecdir}
gzip -c %{SOURCE2} > paperconf.1.gz
install -m0644 paperconf.1.gz %{buildroot}%{_mandir}/man1/paperconf.1
%ldconfig_scriptlets
%oreon_autofiles paper usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libpaper-devel -f %{oreon_filedir}/libpaper-devel.list
%files -n paper -f %{oreon_filedir}/paper.list

%changelog

%autochangelog
