%global source0_hash 4376bf16787a321e39dd3d88523314985d5e7fa6e3123f790390d26496d63615
%global source1_hash 25db846049e5aa047252c57b4446182bc9a8c062ba4c44d2fbb4e674f25e1a39

Name:           acpica-tools
Version:        20251212
Release:        4%{?dist}
Summary:        ACPICA tools for the development and debug of ACPI tables

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://www.intel.com/content/www/us/en/developer/topic-technology/open/acpica/overview.html

ExcludeArch:	i686 armv7hl s390x

Source0:        https://github.com/acpica/acpica/releases/download/%{version}/acpica-unix2-%{version}.tar.gz
Source1:        https://github.com/acpica/acpica/releases/download/%{version}/acpitests-unix-%{version}.tar.gz
Source2:        README.Fedora
Source3:        iasl.1
Source4:        acpibin.1
Source5:        acpidump.1
Source6:        acpiexec.1
Source7:        acpihelp.1
Source9:        acpisrc.1
Source10:       acpixtract.1
Source11:       acpiexamples.1
Source12:       badcode.asl.result
Source13:       grammar.asl.result
Source14:       converterSample.asl.result
Source15:       run-misc-tests.sh
Source16:       COPYING

# other miscellaneous patches
Patch00:	unaligned.patch
Patch01:	template.patch
Patch04:        cve-2017-13695.patch
Patch05:        str-trunc-warn.patch
Patch07:	dangling-ptr.patch
Patch08:	uuid-len.patch
Patch09: 0001-Fix-unused-attribute-error.patch
#Patch11:	0002-Correct-dumping-of-SLIC-tables.patch
#Patch12:	0003-PHAT-FW-health-table-can-be-zero-length.patch

BuildRequires:	make
BuildRequires:  bison patchutils flex gcc

# The previous iasl package contained only a very small subset of these tools
# and it produced only the iasl package listed below; further, the pmtools
# package -- which provides acpidump -- also provides a /usr/sbin/acpixtract
# that we don't really want to collide with
Provides:       acpixtract >= 20120913-7
Provides:       iasl = %{version}-%{release}
Obsoletes:      iasl < 20120913-8

# The pmtools package provides an obsolete and deprecated version of the
# acpidump command from lesswatts.org which has now been taken off-line.
# ACPICA, however, is providing a new version and we again do not want to
# conflict with the command name.
Provides:       acpidump >= 20100513-5
Provides:       pmtools = %{version}-%{release}
Obsoletes:      pmtools < 20100513-6

%description
The ACPI Component Architecture (ACPICA) project provides an OS-independent
reference implementation of the Advanced Configuration and Power Interface
Specification (ACPI).  ACPICA code contains those portions of ACPI meant to
be directly integrated into the host OS as a kernel-resident subsystem, and
a small set of tools to assist in developing and debugging ACPI tables.

This package contains only the user-space tools needed for ACPI table
development, not the kernel implementation of ACPI.  The following commands
are installed:
   -- iasl: compiles ASL (ACPI Source Language) into AML (ACPI Machine
      Language), suitable for inclusion as a DSDT in system firmware.
      It also can disassemble AML, for debugging purposes.
   -- acpibin: performs basic operations on binary AML files (e.g.,
      comparison, data extraction)
   -- acpidump: write out the current contents of ACPI tables
   -- acpiexec: simulate AML execution in order to debug method definitions
   -- acpihelp: display help messages describing ASL keywords and op-codes
   -- acpisrc: manipulate the ACPICA source tree and format source files
      for specific environments
   -- acpixtract: extract binary ACPI tables from acpidump output (see
      also the pmtools package)

This version of the tools is being released under GPLv2 license.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n acpica-unix2-%{version}
gzip -dc %{SOURCE1} | tar -x --strip-components=1 -f -

%autopatch -p1

cp -p %{SOURCE2} README.Fedora
cp -p %{SOURCE3} iasl.1
cp -p %{SOURCE4} acpibin.1
cp -p %{SOURCE5} acpidump.1
cp -p %{SOURCE6} acpiexec.1
cp -p %{SOURCE7} acpihelp.1
cp -p %{SOURCE9} acpisrc.1
cp -p %{SOURCE10} acpixtract.1
cp -p %{SOURCE11} acpiexamples.1
cp -p %{SOURCE12} badcode.asl.result
cp -p %{SOURCE13} grammar.asl.result
cp -p %{SOURCE14} converterSample.asl.result
cp -p %{SOURCE15} tests/run-misc-tests.sh
chmod a+x tests/run-misc-tests.sh
cp -p %{SOURCE16} COPYING

# spurious executable permissions on text files in upstream
chmod a-x changes.txt
chmod a-x source/compiler/new_table.txt


%build
CWARNINGFLAGS="\
    -std=c99\
    -Wall\
    -Wbad-function-cast\
    -Wdeclaration-after-statement\
    -Werror\
    -Wformat=2\
    -Wmissing-declarations\
    -Wmissing-prototypes\
    -Wstrict-aliasing=0\
    -Wstrict-prototypes\
    -Wswitch-default\
    -Wpointer-arith\
    -Wundef\
    -Waddress\
    -Waggregate-return\
    -Winit-self\
    -Winline\
    -Wmissing-declarations\
    -Wmissing-field-initializers\
    -Wnested-externs\
    -Wold-style-definition\
    -Wno-format-nonliteral\
    -Wredundant-decls\
    -Wempty-body\
    -Woverride-init\
    -Wlogical-op\
    -Wmissing-parameter-type\
    -Wold-style-declaration\
    -Wtype-limits"

OPT_CFLAGS="%{optflags} $CWARNINGFLAGS"
OPT_LDFLAGS="%{__global_ldflags}"
export OPT_CFLAGS
export OPT_LDFLAGS

%{make_build}


%install
# Install the binaries
mkdir -p %{buildroot}%{_bindir}
install -pD generate/unix/bin*/* %{buildroot}%{_bindir}/

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -pDm 0644 *.1 %{buildroot}%{_mandir}/man1/

# Install the examples source code
mkdir -p %{buildroot}%{_docdir}/acpica-tools/examples
install -pDm 0644 source/tools/examples/* %{buildroot}%{_docdir}/acpica-tools/examples/

%check
cd tests

# ASL tests
./aslts.sh                         # relies on non-zero exit
[ $? -eq 0 ] || exit 1

# misc tests
#./run-misc-tests.sh %%{buildroot}%%{_bindir} %%{version}

%pre
if [ -e %{_bindir}/acpixtract-acpica ]
then
    alternatives --remove acpixtract %{_bindir}/acpixtract-acpica
fi
if [ -e %{_bindir}/acpidump-acpica ]
then
    alternatives --remove acpidump %{_bindir}/acpidump-acpica
fi

%postun
if [ -e %{_bindir}/acpixtract-acpica ]
then
    alternatives --remove acpixtract %{_bindir}/acpixtract-acpica
fi
if [ -e %{_bindir}/acpidump-acpica ]
then
    alternatives --remove acpidump %{_bindir}/acpidump-acpica
fi


%files
%doc changes.txt source/compiler/new_table.txt
%doc README.Fedora COPYING
%{_bindir}/*
%{_mandir}/*/*
%{_docdir}/*/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20251212-4
- Prepare for Oreon 11 (RP1)
