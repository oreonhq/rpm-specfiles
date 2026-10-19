%global source4_hash f0dced9b581a5808bd2d0d5e4716997043960a56333d5f4c44b201b870aa0ea8
%global source3_hash ddb1802d10604e74188653c80212bb3a493cbe910b3597a68562f90fc1779d72
%global source2_hash 816cdbfd20ce3695be0eb976648714b6fe496785bb8026c6b8911712764d57c7
%global source1_hash cc84253b47b5c036aa1d529332a6c218a39ff71c76974296262b03776f822695
%global source0_hash b2824a6f7b75ffe0193ce9ba55463191a7af7c2ffe10e371e372451e2b527e09
%global sover 0.23
Name:           f2c
Summary:        A Fortran 77 to C/C++ conversion program
Version:        20210928
Release:        1%{?dist}
License:        MIT
URL:            http://www.netlib.org/f2c/
Source0:        http://www.netlib.org/f2c/src.tgz
Source1:        http://www.netlib.org/f2c/libf2c.zip
Source2:        http://www.netlib.org/f2c/f2c.pdf
Source3:        http://www.netlib.org/f2c/f2c.ps
Source4:        http://www.netlib.org/f2c/fc
Patch0:         f2c-20110801.patch
Patch1:         libf2c-20110801-format-security.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  unzip
# /oreon:deps
%description
F2c converts Fortran 77 source code to C or C++ source files. If no
Fortran files are named on the command line, f2c can read Fortran from
standard input and write C to standard output.

%package libs
Summary:        Dynamic libraries from %{name}
%description libs
Dynamic libraries from %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -c %{name}-%{version}
mkdir libf2c
unzip -qq %{SOURCE1} -d libf2c
%autopatch -p1

# Set library soversion
sed -i "s/@SOVER@/%{sover}/" libf2c/makefile.u

# Copy in other source files.
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build

make -C src -f makefile.u %{?_smp_mflags} CFLAGS="%{optflags}" f2c
make -C libf2c -f makefile.u %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"
%install
install -D -p -m 644 src/f2c.h  %{buildroot}%{_includedir}/f2c.h
install -D -p -m 755 src/f2c    %{buildroot}%{_bindir}/f2c
install -D -p -m 644 src/f2c.1t %{buildroot}%{_mandir}/man1/f2c.1
install -D -p -m 755 libf2c/libf2c.so.%{sover} %{buildroot}%{_libdir}/libf2c.so.%{sover}
ln -sr %{buildroot}%{_libdir}/libf2c.so.%{sover} %{buildroot}%{_libdir}/libf2c.so.0
ln -sr %{buildroot}%{_libdir}/libf2c.so.%{sover} %{buildroot}%{_libdir}/libf2c.so
sed -i "s/@lib@/%{_lib}/" fc
install -Dpm 0755 fc %{buildroot}%{_bindir}/f77
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n f2c-libs -f %{oreon_filedir}/f2c-libs.list

%changelog

%autochangelog
