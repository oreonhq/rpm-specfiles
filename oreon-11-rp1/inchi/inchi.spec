%global source0_hash 4874e310c0f2f81b881e90dd0c534752e1b9421d7d92ccfb037710022c7e7efd

%define inchi_so_ver 1.06.00
%define url_ver 106

Summary: The IUPAC International Chemical Identifier library
Name: inchi
Version: 1.0.6
Release: 14%{?dist}
URL: https://www.inchi-trust.org/about-the-inchi-standard/
Source0: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-SRC.zip
Source1: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-DOC.zip
Source2: https://www.inchi-trust.org/download/%{url_ver}/INCHI-1-TEST.zip
Patch0: %{name}-rpm.patch
# reported upstream:
# https://sourceforge.net/p/inchi/bugs/77/
Patch1: %{name}-1.0.6-0001-MolfileReadCountsLine-fix-storing-n_atoms-n_bonds-me.patch
License: GPL-2.0-or-later
BuildRequires: dos2unix
BuildRequires: gcc
BuildRequires: make

%description
The IUPAC International Chemical Identifier (InChITM) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

This package contains the command line conversion utility.

%package libs
Summary: The IUPAC International Chemical Identifier library

%description libs
The IUPAC International Chemical Identifier (InChITM) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

%package devel
Summary: Development headers for the InChI library
Requires: %{name}-libs%{_isa} = %{version}-%{release}

%description devel
The inchi-devel package includes the header files and libraries
necessary for developing programs using the InChI library.

If you are going to develop programs which will use this library
you should install inchi-devel.  You'll also need to have the
inchi package installed.

%package doc
Summary: Documentation for the InChI library
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The inchi-doc package contains user documentation for the InChI software
and InChI library API reference for developers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n INCHI-1-SRC -a 1 -a 2
%patch -P0 -p1 -b .r
%patch -P1 -p1 -b .big_endian
for file in readme.txt ; do
  dos2unix -k $file
done
pushd INCHI-1-TEST/test
unzip -d reference -qq -a test-results.zip
unzip -qq -a test-datasets.zip
dos2unix -k reference/*.inc *.sdf
for f in inchify_{InChI_TestSet,zzp} ; do
    sed -e 's,REM,#,g' -e 's,/,-,g' -e 's,NUL,/dev/null,g' -e 's,inchi-1.exe,../../INCHI_EXE/bin/Linux/inchi-1,g' ${f}.cmd >${f}.sh
    dos2unix ${f}.sh
done
popd

%build
pushd INCHI_API/demos/inchi_main/gcc
%make_build SHARED_LINK_PARM="%{optflags}" OPTFLAGS="%{optflags} -Wno-comment -Wno-parentheses -Wno-unused -Wno-unused-but-set-variable"
popd
pushd INCHI_EXE/inchi-1/gcc
%make_build LINKER_OPTIONS="%{optflags}" OPTFLAGS="%{optflags} -Wno-comment -Wno-parentheses -Wno-unused -Wno-unused-but-set-variable"
popd

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/inchi}
install -pm 755 INCHI_EXE/bin/Linux/inchi-1 %{buildroot}%{_bindir}/
install -p INCHI_API/bin/Linux/libinchi.so.%{inchi_so_ver} $RPM_BUILD_ROOT%{_libdir}
ln -s libinchi.so.%{inchi_so_ver} $RPM_BUILD_ROOT%{_libdir}/libinchi.so.1
ln -s libinchi.so.1               $RPM_BUILD_ROOT%{_libdir}/libinchi.so
install -pm644 INCHI_BASE/src/{ichisize,inchi_api,ixa}.h $RPM_BUILD_ROOT%{_includedir}/inchi

%check
export LD_LIBRARY_PATH=$(pwd)/INCHI_API/bin/Linux/
pushd INCHI-1-TEST/test
for f in inchify_{InChI_TestSet,zzp} ; do
    sh ./${f}.sh
done
for t in its-*.inc zzp-*.inc ; do diff -u reference/$t $t ; done
popd

%files
%{_bindir}/inchi-1

%files libs
%license LICENCE.pdf
%doc readme.txt
%{_libdir}/libinchi.so.1*

%files devel
%{_includedir}/inchi
%{_libdir}/libinchi.so

%files doc
%doc INCHI-1-DOC/*

%changelog
%autochangelog
