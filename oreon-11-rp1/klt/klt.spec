%global source0_hash dfad4da0d542985ff3f08ee0a557e233e145116e387ad8a833433efd2d27d3ec

Name:           klt
Version:        1.3.4
Release:        34%{?dist}
Summary:        An implementation of the Kanade-Lucas-Tomasi feature tracker

License:        LicenseRef-Fedora-Public-Domain
URL:            http://www.ces.clemson.edu/~stb/%{name}/index.html
Source0:        http://www.ces.clemson.edu/~stb/%{name}/%{name}%{version}.zip

# https://bugzilla.redhat.com/show_bug.cgi?id=1037150
Patch0:         0001-format-security.patch
BuildRequires:  gcc
BuildRequires: make

%description

KLT is an implementation, in the C programming language, of a 
feature tracker for the computer vision community.  The source 
code is in the public domain, available for both commercial and 
non-commercial use.

The tracker is based on the early work of Lucas and Kanade, 
was developed fully by Tomasi and Kanade, and was explained clearly 
in the paper by Shi and Tomasi. Later, Tomasi proposed a slight 
modification which makes the computation symmetric with respect 
to the two images -- the resulting equation is derived in the 
unpublished note by myself.  Briefly, good features are located 
by examining the minimum eigenvalue of each 2 by 2 gradient 
matrix, and features are tracked using a Newton-Raphson method of 
minimizing the difference between the two windows. Multi-resolution 
tracking allows for relatively large displacements between images. 
The affine computation that evaluates the consistency of features 
between non-consecutive frames was implemented by Thorsten 
Thormaehlen several years after the original code and documentation 
were written.

%package devel
Requires: %{name} = %{version}-%{release}
Summary:  This package contains development files for %{name}

%description devel
This package provides headers and shared libraries for %{name}

%package static
Requires: %{name} = %{version}-%{release}
Summary:  This package contains static libraries for %{name}

%description static
This package contains the static libraries 
provided by %{name}. 

%package doc
Requires: %{name} = %{version}-%{release}
Summary:  This package contains documentation for %{name}

%description doc
This package contains documentation files for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
sed -i 's/\r//' README.txt 
sed -i 's/\r//' speed.txt
sed -i 's/\r//' example?.c
sed -i '/FLAG1/d' Makefile
sed -i '/rm -f \*\.o/d' Makefile

%patch -P0

%build
%global klt_version %{version}
%global klt_version_major 1

export CFLAGS="$RPM_OPT_FLAGS -fPIC"

make lib %{?_smp_mflags} 
gcc -shared -Wl,-soname,libklt.so.%{klt_version_major} \
    -o libklt.so.%{klt_version} convolve.o error.o pnmio.o pyramid.o selectGoodFeatures.o \
    storeFeatures.o trackFeatures.o klt.o klt_util.o writeFeatures.o 

ln -sf libklt.so.%{klt_version} libklt.so.%{klt_version_major}
ln -sf libklt.so.%{klt_version} libklt.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

for f in *.so* *.a ; do
    cp -a $f $RPM_BUILD_ROOT/%{_libdir}/$f
done

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-doc
cp -av doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-doc/

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-doc/examples/
install -m 0644 -p example?.c -t $RPM_BUILD_ROOT%{_docdir}/%{name}-doc/examples/
install -m 0644 -p *.pgm -t $RPM_BUILD_ROOT%{_docdir}/%{name}-doc/examples/

install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m 0644 -p *.h -t $RPM_BUILD_ROOT%{_includedir}/%{name}

%files
%doc README.txt speed.txt
%{_libdir}/libklt.so.%{klt_version}
%{_libdir}/libklt.so.%{klt_version_major}

%files devel
%{_libdir}/libklt.so
%{_includedir}/%{name}/

%files static
%{_libdir}/*.a

%files doc
%{_docdir}/%{name}-doc

%ldconfig_scriptlets

%changelog
%autochangelog
