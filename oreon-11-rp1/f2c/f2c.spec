%global source0_hash ca404070e9ce0a9aaa6a71fc7d5489d014ade952c5d6de7efb88de8e24f2e8e0

%global sover 0.23

Name:           f2c
Summary:        A Fortran 77 to C/C++ conversion program
Version:        20210928
Release:        12%{?dist}
License:        MIT

URL:            http://www.netlib.org/f2c/
Source0:        http://www.netlib.org/f2c/src.tgz
Source1:        http://www.netlib.org/f2c/libf2c.zip
Source2:        http://www.netlib.org/f2c/f2c.pdf
Source3:        http://www.netlib.org/f2c/f2c.ps
Source4:        http://www.netlib.org/f2c/fc

# Patch makefile to build a shared library
Patch0:         f2c-20110801.patch
Patch1:         libf2c-20110801-format-security.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  unzip

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

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

# Setup f77 script
sed -i "s/@lib@/%{_lib}/" fc
install -Dpm 0755 fc %{buildroot}%{_bindir}/f77

%ldconfig_scriptlets 

%files
%doc f2c.ps f2c.pdf src/changes src/README
%license src/Notice
%{_bindir}/f2c
%{_bindir}/f77
%{_mandir}/man1/f2c.1*
%{_includedir}/f2c.h
%{_libdir}/libf2c.so

%files libs
%doc libf2c/README
%license libf2c/Notice
%{_libdir}/libf2c.so.*

%changelog
%autochangelog
