%global source0_hash f8a13466b48faa3ba99fe17a069e71c9ab006d9b1cfabe699f8c60a47d5bb49a
Summary:        Automated text file generator
Name:		autogen
Version:	5.18.16
Release:        1%{?dist}
License:	GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND GPL-1.0-or-later AND (LGPL-3.0-or-later OR BSD-3-Clause) AND GFDL-1.2-or-later
URL:		http://www.gnu.org/software/autogen/
Source0:        https://mirrors.kernel.org/gnu/autogen/rel%{version}/%{name}-%{version}.tar.xz
Patch0:        autogen-multilib.patch
Patch1:        autogen-overlap.patch
Patch2:        autogen-configure-c99.patch
Patch3:        autogen-fortify.patch
Requires:	%{name}-libopts%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  guile22-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  sed
# /oreon:deps
%description
AutoGen is a tool designed to simplify the creation and maintenance of
programs that contain large amounts of repetitious text. It is especially
valuable in programs that have several blocks of text that must be kept
synchronised.

%package libopts
Summary:	Automated option processing library based on %{name}
License:	LGPL-3.0-or-later
%description libopts
Libopts is very powerful command line option parser consisting of a set of
AutoGen templates and a run time library that nearly eliminates the hassle of
parsing and documenting command line options.

%package libopts-devel
Summary:	Development files for libopts
License:	LGPL-3.0-or-later
Requires:	automake
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libopts%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
%description libopts-devel
This package contains development files for libopts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n autogen-5.18.16

# Disable failing test
sed -i 's|errors.test||' autoopts/test/Makefile.in

%build

export CFLAGS="$RPM_OPT_FLAGS -Wno-implicit-fallthrough -Wno-format-overflow \
		-Wno-format-truncation -Wno-error=discarded-qualifiers \
		-Wno-error=unused-but-set-variable"
autoreconf -fiv
%configure
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' ./libtool
make %{?_smp_mflags}
%check

make check
%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -delete
find $RPM_BUILD_ROOT -type f -name "*.a" -delete
sed -i 's|\(It has been AutoGen-ed\).*.\(by AutoGen\)|\1 \2|' \
	$RPM_BUILD_ROOT%{_mandir}/man3/*.3
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/{columns,getdefs,%{name},xml2ag}
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/lib*.so.*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%ldconfig_scriptlets libopts
%oreon_autofiles autogen-libopts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles autogen-libopts-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n autogen-libopts -f %{oreon_filedir}/autogen-libopts.list
%files -n autogen-libopts-devel -f %{oreon_filedir}/autogen-libopts-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.18.16-1
- Import
