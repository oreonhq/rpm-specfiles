%global source0_hash 157b8051aed7f534e5093471e734e7a95e509c577324099c3c81324ed9d0de77

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Logic for creating an unversioned symlink to %%{_pkgdocdir}
# in case %%{_pkgdocdir} is actually a versioned directory.
# %%global doesn't work here as we need lazy expansion.
%define doc_symlink %{lua:if rpm.expand("%{_pkgdocdir}") ~= rpm.expand("%{_docdir}/%{name}") then print (1) end}

# Setup macros for compile flags if not defined already.
%{!?build_cflags:%global build_cflags %{optflags}}
%{!?build_ldflags:%global build_ldflags %{?__global_ldflags}}

# Construct the distribution string for BUILD_ID.
# Please alter them, if you are building packages
# for third-party repositories from this spec file.
%if 0%{?fedora}
%global dist_string Fedora
%else
%if 0%{?rhel}
%global dist_string Fedora EPEL
%else
%global dist_string UNKNOWN
%endif
%endif

# Some general used defines to reduce boilerplate.
%global git_url https://github.com/%{name}/%{name}

%global make_opts BUILD_ID="%{dist_string} %{version}-%{release}" \\\
LDFLAGS="%{build_ldflags}" USER_CFLAGS="%{build_cflags}"

%global dir_opts PREFIX="%{_prefix}" bindir="%{_bindir}" \\\
datadir="%{_datadir}/%{name}" htmldir="%{_pkgdocdir}/html" \\\
infodir="%{_infodir}"

# Run check target by default.
%bcond check 0

# Workaround for texinfo 7.0.x issue - allow disabling docs in info format
# https://bugzilla.redhat.com/show_bug.cgi?id=2188018
%bcond_with info

Name:           cc65
Version:        2.19
Release:        15%{?dist}
Summary:        A free C compiler for 6502 based systems

# For license clarification see:
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=714058#30
License:        zlib
URL:            https://cc65.github.io
Source0:        %{git_url}/archive/V%{version}/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2253946
Patch0:         cc65-c99.patch

# Backported from upstream.
# none

BuildRequires:  gcc
BuildRequires:  make

Requires:       %{name}-common = %{version}-%{release}

%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Recommends:     %{name}-doc = %{version}-%{release}
Recommends:     %{name}-utils%{?_isa} = %{version}-%{release}
%endif

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

%autosetup -p 1

%build
# Parallel build sometimes fails.
# It finishes fine in a second run, tho.
%make_build %{make_opts} %{dir_opts} || \
%make_build %{make_opts} %{dir_opts}

# Build some additional utils.
%{__mkdir_p} util_bin
%{__cc} %{build_cflags} util/atari/ataricvt.c \
  -o util_bin/ataricvt65 %{build_ldflags}
%{__cc} %{build_cflags} util/cbm/cbmcvt.c \
  -o util_bin/cbmcvt65 %{build_ldflags}
%{__cc} %{build_cflags} util/gamate/gamate-fixcart.c \
  -o util_bin/gamate-fixcart65 %{build_ldflags}
%{__cc} %{build_cflags} util/zlib/deflater.c \
  -o util_bin/deflater65 %{build_ldflags} -lz

# Build the documentation.
%if %{with info}
%make_build doc
%else
%make_build html
%endif

%install
%make_install %{make_opts} %{dir_opts}

# Install additional utils.
%{__install} -p -m 0755 util/ca65html %{buildroot}%{_bindir}
%{__install} -p -m 0755 util_bin/* %{buildroot}%{_bindir}

# Install more documentation.
%{__mv} %{buildroot}%{_datadir}/%{name}/samples %{buildroot}%{_pkgdocdir}
%{__install} -p -m 0644 README.md %{buildroot}%{_pkgdocdir}
%if !(0%{?fedora} >= 21 || 0%{?rhel} >= 7)
%{__install} -p -m 0644 LICENSE %{buildroot}%{_pkgdocdir}
%endif
%if 0%{doc_symlink}
%{__ln_s} %{_pkgdocdir} %{buildroot}%{_docdir}/%{name}
%endif

%if %{with check}
%check
# We need a clean build without PREFIX et all defined
# to successfully run the tests from inside the builddir.
# Unfortunately the testsuite cannot be run threaded.  -_-
%{__make} clean
%make_build %{make_opts} || \
%make_build %{make_opts}
%{__make} -C test QUIET=1
%endif

%files
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license LICENSE
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_bindir}/ar65
%{_bindir}/ca65
%{_bindir}/cc65
%{_bindir}/chrcvt65
%{_bindir}/cl65
%{_bindir}/co65
%{_bindir}/da65
%{_bindir}/grc65
%{_bindir}/ld65
%{_bindir}/od65
%{_bindir}/sim65
%{_bindir}/sp65

%files devel
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_datadir}/%{name}

%files doc
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %{_pkgdocdir}
%if %{with info}
%{_infodir}/*.info*
%endif

%files utils
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%else
%doc %{_pkgdocdir}/LICENSE
%endif
%if 0%{doc_symlink}
%doc %{_docdir}/%{name}
%endif
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%{_bindir}/ataricvt65
%{_bindir}/ca65html
%{_bindir}/cbmcvt65
%{_bindir}/deflater65
%{_bindir}/gamate-fixcart65

%changelog
%autochangelog
