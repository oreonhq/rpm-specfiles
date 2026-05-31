%global source0_hash a4e1297b69b9fd1054ee7f5bcc55f4d56da152d41d2eabdf18727a9cddc1f402

Name:		libpaper
Version:	2.1.1
Release:	10%{?dist}
# Needed to replace separate paper package
Epoch:		1
Summary:	Library and tools for handling papersize
# libpaper is LGPL-2.1+
# bundled libgnu is LGPL-2.1+, LGPL-2+ and GPL-3+
# paperspecs is Public Domain
# localepaper.c is FSFAP
License:	LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND GPL-3.0-or-later AND LGPL-2.0-or-later AND FSFAP
URL:		https://github.com/rrthomas/libpaper/
# Upstream GitHub archive has no generated configure. Fedora ships this dist tarball (lookaside).
Source0:        https://github.com/rrthomas/libpaper/archive/v%{version}/%{name}-%{version}.tar.gz
# Pulled from paper
Source1:	localepaper.c
# from libpaper-1.x
Source2:        paperconf.1

# gcc is no longer in buildroot by default
BuildRequires:  gcc
# use git for autosetup
BuildRequires:  git-core
# uses make
BuildRequires:  make
BuildRequires:	libtool, gettext, gawk, autoconf, automake
BuildRequires:	help2man, tar, gnupg2, perl-interpreter, gzip

Provides: bundled(gnulib)

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
# This is licensed differently from libpaper.
# paper.c is GPL-3.0-or-later
# paperconf.c is GPL 2.0 only
# localepaper.c is FSFAP (except it is missing the warranty disclaimer... but the intent is clear)
License:	GPL-3.0-or-later AND FSFAP AND GPL-2.0-only

%description -n paper
The paper(1) utility can be used to find the user's preferred
default paper size and give information about known sizes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git
cp %{SOURCE1} src/

%if 0
sed -i 's|gnulib_tool=$gnulib_path/gnulib-tool|gnulib_tool=%{_bindir}/gnulib-tool|g' bootstrap
sed -i 's|./gnulib/gnulib-tool|%{_bindir}/gnulib-tool|g' bootstrap.conf
sed -i '/doc\/INSTALL/d' bootstrap
./bootstrap --gnulib-srcdir=%{_datadir}/gnulib/ --skip-git
%endif

%build
%configure --disable-static
%make_build

# localepaper
pushd src
%{__cc} %{optflags} -I.. -Ilibgnu -o localepaper localepaper.c libgnu/.libs/libgnupaper.a %{_hardening_ldflags}
popd

%check
# No upstream tests
echo "Testing localepaper tool"
locale width height > expected
./src/localepaper | tr ' ' "\n" > got
diff -u expected got
# No real way to test the paper tool

%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
# maybe someday the translations will return
%if 0
for i in cs da de es fr gl hu it ja nl pt_BR sv tr uk vi; do
	mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES/;
	msgfmt debian/po/$i.po -o $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES/%{name}.mo;
done
%find_lang %{name}
%endif

mkdir %{buildroot}%{_libexecdir}
install -m0755 src/localepaper %{buildroot}%{_libexecdir}

gzip -c %{SOURCE2} > paperconf.1.gz
install -m0644 paperconf.1.gz %{buildroot}%{_mandir}/man1/paperconf.1

%ldconfig_scriptlets

%files
%doc ChangeLog README
%license COPYING
%config(noreplace) %{_sysconfdir}/paperspecs
%{_libdir}/libpaper.so.2*

%files devel
%{_includedir}/paper.h
%{_libdir}/libpaper.so

%files -n paper
%{_bindir}/paper
%{_bindir}/paperconf
%{_libexecdir}/localepaper
%{_mandir}/man1/paper.*
%{_mandir}/man1/paperconf.*
%{_mandir}/man5/paperspecs.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-10
- Prepare for Oreon 11 (RP1)
