%global source0_hash fb8480750439128515a11e7e405888f560419fd657ca1ae6a23e3e836ae95873
%global upstream_owner    AdaCore
%global upstream_name     gnatcoll-bindings
%global upstream_version  26.0.0
%global upstream_commit   4d3761dd658759b06aea4fdf028ba5a4bdf89785
Name:           gnatcoll-bindings
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        The GNAT Components Collection – bindings
Summary(sv):    GNAT Components Collection – bindningar
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        https://github.com/%{upstream_owner}/%{name}/archive/%{upstream_commit}.tar.gz#/%{name}-%{version}.tar.gz
Patch:          %{name}-zstd-requires-gnatcoll-os.patch
ExclusiveArch:  %{GPRbuild_arches}
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  fedora-gnat-project-common
BuildRequires:  gcc-c++
BuildRequires:  gcc-gnat
BuildRequires:  gmp-devel
BuildRequires:  gnatcoll-core-devel
BuildRequires:  gprbuild
BuildRequires:  libzstd-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  sed
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This is the bindings module of the GNAT Components Collection. It provides
bindings to GMP, Iconv, LZMA, Python 3, Readline, Syslog, ZLib and ZSTD,
and a parallel sorting algorithm using OpenMP.

%description -l sv
Detta är bindningsmodulen i GNAT Components Collection. Den tillhandahåller
bindningar till GMP, Iconv, LZMA, Python 3, Readline, Syslog, ZLib och ZSTD,
samt en parallell sorteringsalgoritm som använder OpenMP.

#################
## Subpackages ##
#################

%package devel
Summary:        Development metapackage for the GNAT Components Collection – bindings
Summary(sv):    Metapaket för programmering med GNAT Components Collection – bindningar
Requires:       gnatcoll-gmp-devel      = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-iconv-devel    = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-readline-devel = %{epoch}:%{version}-%{release}
Requires:       gnatcoll-syslog-devel   = %{epoch}:%{version}-%{release}
Provides:       deprecated()
%description devel
Each binding in the GNAT Components Collection now has its own development
package. This meta-package exists to prevent problems when Fedora is upgraded.
It pulls in those development packages that were previously combined as
gnatcoll-bindings-devel.

Do not specify this package in any configurations or dependencies. Specify the
packages you actually need.

%description devel -l sv
Varje bindning i GNAT Components Collection har nu ett eget programmeringspaket.
Detta metapaket är till för att undvika problem när Fedora uppgraderas. Det drar
in de programmeringspaketen som förut ingick i gnatcoll-bindings-devel.

Ange inte det här paketet i några konfigurationer eller beroenden. Ange paketen
du faktiskt behöver.

%package -n gnatcoll-cpp
Summary:        The GNAT Components Collection – C++ binding
Summary(sv):    GNAT Components Collection – C++-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%description -n gnatcoll-cpp
This is the C++ component of the GNAT Components Collection. It is an interface
to the C++ ISO/IEC 14882:1998(E) string class.

%description -n gnatcoll-cpp -l sv
Detta är C++-komponenten i GNAT Components Collection. Den är ett gränssnitt
till C++-strängklassen i ISO/IEC 14882:1998(E).

%package -n gnatcoll-cpp-devel
Summary:        Development files for the GNAT Components Collection – C++ binding
Summary(sv):    Filer för programmering med GNAT Components Collection – C++-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-cpp%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-cpp-devel
This package contains source code and linking information for developing
applications that use the C++ component of the GNAT Components Collection.
It is an interface to the C++ ISO/IEC 14882:1998(E) string class.

%description -n gnatcoll-cpp-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder C++-komponenten i GNAT Components Collection.
Den är ett gränssnitt till C++-strängklassen i ISO/IEC 14882:1998(E).

%package -n gnatcoll-gmp
Summary:        The GNAT Components Collection – GMP binding
Summary(sv):    GNAT Components Collection – GMP-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later
%description -n gnatcoll-gmp
This is the GMP component of the GNAT Components Collection. It is an interface
to the GNU Multiple Precision (GMP) arithmetic library.

%description -n gnatcoll-gmp -l sv
Detta är GMP-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket GNU Multiple Precision (GMP) för godtyckligt precisa
beräkningar.

%package -n gnatcoll-gmp-devel
Summary:        Development files for the GNAT Components Collection – GMP binding
Summary(sv):    Filer för programmering med GNAT Components Collection – GMP-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later
Requires:       gnatcoll-gmp%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-gmp-devel
This package contains source code and linking information for developing
applications that use the GMP component of the GNAT Components Collection.
It is an interface to the GNU Multiple Precision (GMP) arithmetic library.

%description -n gnatcoll-gmp-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder GMP-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket GNU Multiple Precision (GMP) för
godtyckligt precisa beräkningar.

%package -n gnatcoll-iconv
Summary:        The GNAT Components Collection – Iconv binding
Summary(sv):    GNAT Components Collection – Iconvbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%description -n gnatcoll-iconv
This is the Iconv component of the GNAT Components Collection. It is an
interface to libiconv for conversion between character encodings.

%description -n gnatcoll-iconv -l sv
Detta är Iconv-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket Iconv för omvandling mellan teckenkodningar.

%package -n gnatcoll-iconv-devel
Summary:        Development files for the GNAT Components Collection – Iconv binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Iconvbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-iconv%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-iconv-devel
This package contains source code and linking information for developing
applications that use the Iconv component of the GNAT Components Collection.
It is an interface to libiconv for conversion between character encodings.

%description -n gnatcoll-iconv-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder Iconv-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket Iconv för omvandling mellan
teckenkodningar.

%package -n gnatcoll-lzma
Summary:        The GNAT Components Collection – LZMA binding
Summary(sv):    GNAT Components Collection – LZMAbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%description -n gnatcoll-lzma
This is the LZMA component of the GNAT Components Collection. It is an
interface to liblzma, a library for lossless data compression.

%description -n gnatcoll-lzma -l sv
Detta är LZMA-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket liblzma för förlustfri datakomprimering.

%package -n gnatcoll-lzma-devel
Summary:        Development files for the GNAT Components Collection – LZMA binding
Summary(sv):    Filer för programmering med GNAT Components Collection – LZMAbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-lzma%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-lzma-devel
This package contains source code and linking information for developing
applications that use the LZMA component of the GNAT Components Collection.
It is an interface to liblzma, a library for lossless data compression.

%description -n gnatcoll-lzma-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder LZMA-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket liblzma för förlustfri datakomprimering.

%package -n gnatcoll-omp
Summary:        The GNAT Components Collection – parallel sorting
Summary(sv):    GNAT Components Collection – parallell sortering
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%description -n gnatcoll-omp
This is the OpenMP component of the GNAT Components Collection. It provides a
parallel sorting algorithm using OpenMP.

%description -n gnatcoll-omp -l sv
Detta är OpenMP-komponenten i GNAT Components Collection. Den tillhandahåller
en parallell sorteringsalgoritm som använder OpenMP.

%package -n gnatcoll-omp-devel
Summary:        Development files for the GNAT Components Collection – parallel sorting
Summary(sv):    Filer för programmering med GNAT Components Collection – parallell sortering
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-omp%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-omp-devel
This package contains source code and linking information for developing
applications that use the OpenMP component of the GNAT Components Collection.
It provides a parallel sorting algorithm using OpenMP.

%description -n gnatcoll-omp-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder OpenMP-komponenten i GNAT Components Collection.
Den tillhandahåller en parallell sorteringsalgoritm som använder OpenMP.

%package -n gnatcoll-python3
Summary:        The GNAT Components Collection – Python 3 binding
Summary(sv):    GNAT Components Collection – Pythonbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later
%description -n gnatcoll-python3
This is the Python 3 component of the GNAT Components Collection. It is an
interface to the Python 3 interpreter.

%description -n gnatcoll-python3 -l sv
Detta är Python 3-komponenten i GNAT Components Collection. Den är ett
gränssnitt mot pythontolken.

%package -n gnatcoll-python3-devel
Summary:        Development files for the GNAT Components Collection – Python 3 binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Pythonbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later
Requires:       gnatcoll-python3%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-python3-devel
This package contains source code and linking information for developing
applications that use the Python 3 component of the GNAT Components Collection.
It is an interface to the Python 3 interpreter.

%description -n gnatcoll-python3-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder Python 3-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot pythontolken.

%package -n gnatcoll-readline
Summary:        The GNAT Components Collection – Readline binding
Summary(sv):    GNAT Components Collection – Readlinebindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later
%description -n gnatcoll-readline
This is the Readline component of the GNAT Components Collection. It is an
interface to the Readline library for interactive input from the user.

%description -n gnatcoll-readline -l sv
Detta är Readline-komponenten i GNAT Components Collection. Den är ett
gränssnitt mot biblioteket Readline för interaktiv inmatning från användaren.

%package -n gnatcoll-readline-devel
Summary:        Development files for the GNAT Components Collection – Readline binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Readlinebindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later
Requires:       gnatcoll-readline%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-readline-devel
This package contains source code and linking information for developing
applications that use the Readline component of the GNAT Components Collection.
It is an interface to the Readline library for interactive input from the user.

%description -n gnatcoll-readline-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder Readline-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket Readline för interaktiv inmatning från
användaren.

%package -n gnatcoll-syslog
Summary:        The GNAT Components Collection – Syslog binding
Summary(sv):    GNAT Components Collection – Syslogbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%description -n gnatcoll-syslog
This is the Syslog component of the GNAT Components Collection. It is an
interface to the system logger on Unix-like systems.

%description -n gnatcoll-syslog -l sv
Detta är Syslog-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot Unixlika operativsystems loggfunktion.

%package -n gnatcoll-syslog-devel
Summary:        Development files for the GNAT Components Collection – Syslog binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Syslogbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-syslog%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-syslog-devel
This package contains source code and linking information for developing
applications that use the Syslog component of the GNAT Components Collection.
It is an interface to the system logger on Unix-like systems.

%description -n gnatcoll-syslog-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder Syslog-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot Unixlika operativsystems loggfunktion.

%package -n gnatcoll-zlib
Summary:        The GNAT Components Collection – ZLib binding
Summary(sv):    GNAT Components Collection – Zlibbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%description -n gnatcoll-zlib
This is the ZLib component of the GNAT Components Collection. It is an
interface to ZLib, a library for lossless data compression.

%description -n gnatcoll-zlib -l sv
Detta är ZLib-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket ZLib för förlustfri datakomprimering.

%package -n gnatcoll-zlib-devel
Summary:        Development files for the GNAT Components Collection – ZLib binding
Summary(sv):    Filer för programmering med GNAT Components Collection – Zlibbindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-zlib%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-zlib-devel
This package contains source code and linking information for developing
applications that use the ZLib component of the GNAT Components Collection.
It is an interface to ZLib, a library for lossless data compression.

%description -n gnatcoll-zlib-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder ZLib-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket ZLib för förlustfri datakomprimering.

%package -n gnatcoll-zstd
Summary:        The GNAT Components Collection – ZSTD binding
Summary(sv):    GNAT Components Collection – ZSTD-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
%description -n gnatcoll-zstd
This is the ZSTD component of the GNAT Components Collection. It is an
interface to ZSTD, a library for lossless data compression.

%description -n gnatcoll-zstd -l sv
Detta är ZSTD-komponenten i GNAT Components Collection. Den är ett gränssnitt
mot biblioteket ZSTD för förlustfri datakomprimering.

%package -n gnatcoll-zstd-devel
Summary:        Development files for the GNAT Components Collection – ZSTD binding
Summary(sv):    Filer för programmering med GNAT Components Collection – ZSTD-bindning
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       gnatcoll-zstd%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common gnatcoll-core-devel
%description -n gnatcoll-zstd-devel
This package contains source code and linking information for developing
applications that use the ZSTD component of the GNAT Components Collection.
It is an interface to ZSTD, a library for lossless data compression.

%description -n gnatcoll-zstd-devel -l sv
Detta paket innehåller källkod och länkningsinformation som behövs för att
utveckla program som använder ZSTD-komponenten i GNAT Components Collection.
Den är ett gränssnitt mot biblioteket ZSTD för förlustfri datakomprimering.

%global set_env export GNATCOLL_VERSION=%{version} \
                export BUILD=PROD \
                export LIBRARY_TYPE=relocatable \
                export GNATCOLL_ICONV_OPT=@/dev/null \
                export GNATCOLL_PYTHON_CFLAGS=`python3-config --cflags` \
                export GNATCOLL_PYTHON_LIBS=`python3-config --ldflags` \
                export GNATCOLL_ZSTD_VERSION=%{version} \
                export GNATCOLL_ZSTD_OS=unix \
                export GNATCOLL_ZSTD_BUILD_MODE=PROD
# Iconv is not a separate library, but an empty GNATCOLL_ICONV_OPT doesn't
# prevent GPRbuild from using the default "-liconv", so it's set to a value
# that makes no difference.

#############
## Prepare ##
#############

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{upstream_commit}

# Convert line breaks.
dos2unix --keepdate gmp/examples/gmp_examples.gpr

###########
## Build ##
###########

%build

%set_env
for component in cpp gmp iconv lzma omp syslog zlib zstd; do
    gprbuild %{GPRbuild_flags} -P ${component}/gnatcoll_${component}.gpr
done
gprbuild %{GPRbuild_flags} -P python3/gnatcoll_python.gpr
gprbuild %{GPRbuild_flags} \
         -largs -Wl,--no-warn-execstack -gargs \
         -P readline/gnatcoll_readline.gpr
%install
%set_env
for component in cpp gmp iconv lzma omp readline syslog zlib zstd ; do
    %{GPRinstall -s gnatcoll-${component} -a gnatcoll-${component}} \
                 --no-build-var -P ${component}/gnatcoll_${component}.gpr
done
%{GPRinstall -s gnatcoll-python -a gnatcoll-python} \
             --no-build-var -P python3/gnatcoll_python.gpr
for component in cpp gmp iconv lzma omp python3 readline syslog zlib zstd ; do
    ln --symbolic --force libgnatcoll_${component}.so.%{version} \
       %{buildroot}%{_libdir}/libgnatcoll_${component}.so
done
for component in gmp iconv omp python3 readline syslog zstd ; do
    mkdir --parents %{buildroot}%{_docdir}/gnatcoll-${component}
    cp --preserve=timestamps ${component}/README* \
       --target-directory=%{buildroot}%{_docdir}/gnatcoll-${component}/
done
mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/gnatcoll/gmp \
   %{buildroot}%{_docdir}/gnatcoll-gmp/examples
rmdir %{buildroot}%{_datadir}/examples/gnatcoll
rmdir %{buildroot}%{_datadir}/examples
mkdir --parents %{buildroot}%{_licensedir}/%{name}
cp --preserve=timestamps COPYING3 COPYING.RUNTIME \
   --target-directory=%{buildroot}%{_licensedir}/%{name}
for component in cpp gmp iconv lzma omp python readline syslog zlib zstd ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=/package Linker is/,/end Linker/d' \
        '--expression=/python_(cflags|libs)/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'gnatcoll-${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'gnatcoll-${component}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/gnatcoll_${component}.gpr
done
%oreon_autofiles gnatcoll-cpp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-cpp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-gmp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-gmp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-iconv usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-iconv-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-lzma usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-lzma-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-omp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-omp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-python3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-python3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-readline usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-readline-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-syslog usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-syslog-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-zlib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-zlib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles gnatcoll-zstd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnatcoll-zstd-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gnatcoll-bindings-devel -f %{oreon_filedir}/gnatcoll-bindings-devel.list
%files -n gnatcoll-cpp -f %{oreon_filedir}/gnatcoll-cpp.list
%files -n gnatcoll-cpp-devel -f %{oreon_filedir}/gnatcoll-cpp-devel.list
%files -n gnatcoll-gmp -f %{oreon_filedir}/gnatcoll-gmp.list
%files -n gnatcoll-gmp-devel -f %{oreon_filedir}/gnatcoll-gmp-devel.list
%files -n gnatcoll-iconv -f %{oreon_filedir}/gnatcoll-iconv.list
%files -n gnatcoll-iconv-devel -f %{oreon_filedir}/gnatcoll-iconv-devel.list
%files -n gnatcoll-lzma -f %{oreon_filedir}/gnatcoll-lzma.list
%files -n gnatcoll-lzma-devel -f %{oreon_filedir}/gnatcoll-lzma-devel.list
%files -n gnatcoll-omp -f %{oreon_filedir}/gnatcoll-omp.list
%files -n gnatcoll-omp-devel -f %{oreon_filedir}/gnatcoll-omp-devel.list
%files -n gnatcoll-python3 -f %{oreon_filedir}/gnatcoll-python3.list
%files -n gnatcoll-python3-devel -f %{oreon_filedir}/gnatcoll-python3-devel.list
%files -n gnatcoll-readline -f %{oreon_filedir}/gnatcoll-readline.list
%files -n gnatcoll-readline-devel -f %{oreon_filedir}/gnatcoll-readline-devel.list
%files -n gnatcoll-syslog -f %{oreon_filedir}/gnatcoll-syslog.list
%files -n gnatcoll-syslog-devel -f %{oreon_filedir}/gnatcoll-syslog-devel.list
%files -n gnatcoll-zlib -f %{oreon_filedir}/gnatcoll-zlib.list
%files -n gnatcoll-zlib-devel -f %{oreon_filedir}/gnatcoll-zlib-devel.list
%files -n gnatcoll-zstd -f %{oreon_filedir}/gnatcoll-zstd.list
%files -n gnatcoll-zstd-devel -f %{oreon_filedir}/gnatcoll-zstd-devel.list

%changelog

%autochangelog
