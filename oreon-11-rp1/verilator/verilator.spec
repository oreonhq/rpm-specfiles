%global source0_hash 8c8d2e11e6ad32f641dd250742a94195ddecb912e2e2dabe2f42ddbbb99c1092
%bcond longtests 0
%ifarch x86_64 aarch64
%bcond ccwarn 1
%else
%bcond ccwarn 0
%endif
%bcond tcmalloc 1
%bcond z3 1
%bcond ccache 0
%bcond mold 0
Name:           verilator
Version:        5.052
Release:        1%{?dist}
Summary:        A fast simulator for synthesizable Verilog
License:        LGPL-3.0-only OR Artistic-2.0
URL:            https://veripool.org/verilator/
Source0:        https://github.com/verilator/verilator/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
%if %{with tcmalloc}
%endif
%if %{with mold}
Requires:       mold
%endif
%if %{with ccache}
Requires:       ccache
%endif
%if %{with z3}
Requires:       z3
%endif
Requires: %{name}-devel = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  gperftools-devel
BuildRequires:  gperftools-libs
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-lib
BuildRequires:  perl-version
BuildRequires:  python3-devel
BuildRequires:  python3-distro
BuildRequires:  sed
BuildRequires:  z3
# /oreon:deps
%description
Verilator is the fastest free Verilog HDL simulator. It compiles
synthesizable Verilog, plus some PSL, SystemVerilog and Synthesis
assertions into C++ or SystemC code. It is designed for large projects
where fast simulation performance is of primary concern, and is
especially well suited to create executable models of CPUs for
embedded software design teams.

%package devel
Summary:        Libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains library and header files needed to develop
applications based on %{name}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
This package contains the documentation for %{name}.

%prep

%autosetup -p1
find . -name .gitignore -delete
export VERILATOR_ROOT=%{_datadir}
autoconf
%configure \
    --disable-partial-static \
    --disable-defenv \
%if %{with ccwarn}
    --enable-ccwarn \
%else 
    --disable-ccwarn \
%endif
%if %{with longtests}
    --enable-longtests
%else
    --disable-longtests
%endif

# We cannot run autoreconf because upstream uses unqualified stdlib identifiers
# that are included by autoconf-generated header files.
find -name Makefile_obj -exec sed -i \
    -e 's|^\(COPT = .*\)|\1 %{optflags}|' \
    -e 's|^#LDFLAGS += .*|LDFLAGS += %{__global_ldflags}|' \
    {} \;

# Fix /usr/bin/env <bin> ("env-script-interpreter")
sed -i 's#/usr/bin/env python3#/usr/bin/python3#g' docs/bin/*

%build

export VERILATOR_SRC_VERSION=fedora-%{version}
%make_build 
%install
%make_install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/verilator.pc %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_datadir}/verilator/examples
rm -rf %{buildroot}%{_datadir}/verilator/tests
%undefine _auto_set_build_flags
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n verilator-devel -f %{oreon_filedir}/verilator-devel.list
%files -n verilator-doc -f %{oreon_filedir}/verilator-doc.list

%changelog

%autochangelog
