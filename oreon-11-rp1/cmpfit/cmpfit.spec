%global source0_hash 0652fdc04d4e76c3c3aee05d7a97507a9afe97758ee235fd2e7126f660a420e6

# We keep track manually of the library version
%global liblongver 0.0.0
%global libshortver 0

Name:           cmpfit
Version:        1.5
Release:        10%{?dist}
Summary:        A MINPACK-1 Least Squares Fitting Library in C

License:        BSD-2-Clause-FreeBSD
URL:            http://cow.physics.wisc.edu/~craigm/idl/cmpfit.html
Source0:        http://cow.physics.wisc.edu/~craigm/idl/down/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
CMPFIT uses the Levenberg-Marquardt technique to solve the least-squares 
problem. In its typical use, CMPFIT will be used to fit a user-supplied 
function (the "model") to user-supplied data points (the "data") by adjusting 
a set of parameters. CMPFIT is based upon MINPACK-1 (LMDIF.F) by More' and 
collaborators. 

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release} 

%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# Manual build, makefile only does static library
gcc %{optflags} -fpic -c -o mpfit.o mpfit.c
gcc -shared -Wl,-soname,libmpfit.so.%{libshortver} -o libmpfit.so.%{liblongver} mpfit.o -lm

%install
mkdir -p  %{buildroot}/%{_includedir}
mkdir -p  %{buildroot}/%{_libdir}

cp mpfit.h %{buildroot}/%{_includedir}
cp libmpfit.so.%{liblongver} %{buildroot}/%{_libdir}
pushd %{buildroot}/%{_libdir}
ln -s libmpfit.so.%{liblongver} libmpfit.so.%{libshortver}
ln -s libmpfit.so.%{liblongver} libmpfit.so
popd

%files
%doc README DISCLAIMER
%{_libdir}/libmpfit.so.%{liblongver}
%{_libdir}/libmpfit.so.%{libshortver}

%files devel
%{_includedir}/mpfit.h
%{_libdir}/libmpfit.so

%changelog
%autochangelog
