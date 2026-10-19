%global source0_hash 157b8051aed7f534e5093471e734e7a95e509c577324099c3c81324ed9d0de77
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}
%define doc_symlink %{lua:if rpm.expand("%{_pkgdocdir}") ~= rpm.expand("%{_docdir}/%{name}") then print (1) end}
%{!?build_cflags:%global build_cflags %{optflags}}
%{!?build_ldflags:%global build_ldflags %{?__global_ldflags}}
%global dist_string UNKNOWN
%global git_url https://github.com/%{name}/%{name}
%global make_opts BUILD_ID="%{dist_string} %{version}-%{release}" \\\
LDFLAGS="%{build_ldflags}" USER_CFLAGS="%{build_cflags}"
%global dir_opts PREFIX="%{_prefix}" bindir="%{_bindir}" \\\
datadir="%{_datadir}/%{name}" htmldir="%{_pkgdocdir}/html" \\\
infodir="%{_infodir}"
%bcond check 0
%bcond_with info
Name:           cc65
Version:        2.19
Release:        15%{?dist}
Summary:        A free C compiler for 6502 based systems
License:        zlib
URL:            https://cc65.github.io
Source0:        %{git_url}/archive/V%{version}/%{name}-%{version}.tar.gz
Patch0:         cc65-c99.patch
Requires:       %{name}-common = %{version}-%{release}
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Recommends:     %{name}-doc = %{version}-%{release}
Recommends:     %{name}-utils%{?_isa} = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  linuxdoc-tools
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  zlib-devel
# /oreon:deps
%description
cc65 is a complete cross development package for 65(C)02 systems,
including a powerful macro assembler, a C compiler, linker,
librarian and several other tools.

cc65 has C and runtime library support for many of the old 6502
machines, including

- the following Commodore machines:
  - VIC20
  - C16/C116 and Plus/4
  - C64
  - C128
  - CBM 510 (aka P500)
  - the 600/700 family
  - newer PET machines (not 2001).
- the Apple ]\[+ and successors.
- the Atari 8 bit machines.
- the Atari 2600 console.
- the Atari 5200 console.
- GEOS for the C64, C128 and Apple //e.
- the Bit Corporation Gamate console.
- the NEC PC-Engine (aka TurboGrafx-16) console.
- the Nintendo Entertainment System (NES) console.
- the Watara Supervision console.
- the VTech Creativision console.
- the Oric Atmos.
- the Oric Telestrat.
- the Lynx console.
- the Ohio Scientific Challenger 1P.

%package        devel
Summary:        Development files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-common = %{version}-%{release}
%description    devel
This package contains the development files needed to
compile and link applications for the 65(C)02 CPU with
the %{name} cross compiler toolchain.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
BuildRequires:  linuxdoc-tools
BuildRequires:  texinfo
%description    doc
This package contains the documentation files for %{name}.

%package        utils
Summary:        Additional utilities for %{name}
BuildRequires:  zlib-devel
%description    utils
This package contains the additional utilities for %{name}.

They are not needed for compiling applications with %{name},
but might be handy for some additional tasks.

Since these utility programs have some heavier dependencies,
and also can be used without the need of installing %{name},
they have been split into this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build %{make_opts} %{dir_opts} || \
%make_build %{make_opts} %{dir_opts}
%{__mkdir_p} util_bin
%{__cc} %{build_cflags} util/atari/ataricvt.c \
  -o util_bin/ataricvt65 %{build_ldflags}
%{__cc} %{build_cflags} util/cbm/cbmcvt.c \
  -o util_bin/cbmcvt65 %{build_ldflags}
%{__cc} %{build_cflags} util/gamate/gamate-fixcart.c \
  -o util_bin/gamate-fixcart65 %{build_ldflags}
%{__cc} %{build_cflags} util/zlib/deflater.c \
  -o util_bin/deflater65 %{build_ldflags} -lz
%if %{with info}
%make_build doc
%else
%make_build html
%endif
%install
%make_install %{make_opts} %{dir_opts}
%{__install} -p -m 0755 util/ca65html %{buildroot}%{_bindir}
%{__install} -p -m 0755 util_bin/* %{buildroot}%{_bindir}
%{__mv} %{buildroot}%{_datadir}/%{name}/samples %{buildroot}%{_pkgdocdir}
%{__install} -p -m 0644 README.md %{buildroot}%{_pkgdocdir}
%if 0%{doc_symlink}
%{__ln_s} %{_pkgdocdir} %{buildroot}%{_docdir}/%{name}
%oreon_autofiles cc65-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cc65-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cc65-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with check}
%check

%{__make} clean
%make_build %{make_opts} || \
%make_build %{make_opts}
%{__make} -C test QUIET=1
%endif
%files -f %{oreon_filedir}/main.list
%files -n cc65-devel -f %{oreon_filedir}/cc65-devel.list
%files -n cc65-doc -f %{oreon_filedir}/cc65-doc.list
%files -n cc65-utils -f %{oreon_filedir}/cc65-utils.list

%changelog

%autochangelog
