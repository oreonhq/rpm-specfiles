%global source0_hash fd003ff722d8b654a6ceaaadeffb1806d2d513afe888ba00ecfb4a115897844c

Name:		mongoose
Summary:	An easy-to-use self-sufficient web server
Version:	3.1
Release:	30%{?dist}
License:	MIT
URL:		http://code.google.com/p/mongoose
Source0:	http://mongoose.googlecode.com/files/mongoose-%{version}.tgz
Source1:	mongoose.conf
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	openssl-devel

# Build changes:
# http://code.google.com/p/mongoose/issues/detail?id=372 
Patch0:		mongoose-fix-libmongoose-so-build.patch
# http://code.google.com/p/mongoose/issues/detail?id=371
Patch1:		mongoose-fix-no-ssl-dl-build-error.patch

%description
Mongoose web server executable is self-sufficient, it does not depend on 
anything to start serving requests. If it is copied to any directory and 
executed, it starts to serve that directory on port 8080 (so to access files, 
go to http://localhost:8080). If some additional configuration is required - 
for example, different listening port or IP-based access control, then a 
'mongoose.conf' file with respective options can be created in the same 
directory where executable lives. This makes Mongoose perfect for all sorts 
of demos, quick tests, file sharing, and Web programming.

%package lib
Summary:	Shared Object for applications that use %{name} embedded

%description lib
This package contains the shared library required by applications that
are using %{name}'s embeddable API to provide web services. 

%ldconfig_scriptlets lib

%package devel
Summary:	Header files and development libraries for %{name}
Requires:	%{name}-lib = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs embedding %{name} on them,
you will need to install %{name}-devel and check %{name}'s API at its
comprisable header file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1 -b .solib-build
%patch -P1 -p1 -b .nossldl-build
%{__install} -p -m 0644  %{SOURCE1} .

%build
export VERSION=%{version}
%{__make} %{?_smp_mflags} VER="$VERSION" SOVER="${VERSION%.?}" \
			CFLAGS="%{optflags} -lssl -lcrypto -DNO_SSL_DL" linux 

%install
%{__rm} -rf %{buildroot}
%{__install} -D -p -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
%{__install} -D -p -m 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
# -lib subpackage
export VERSION=%{version}
%{__install} -D -p -m 0755 lib%{name}.so.%{version} \
		%{buildroot}/%{_libdir}/lib%{name}.so.$VERSION
ln -s %{_libdir}/lib%{name}.so.$VERSION \
		%{buildroot}/%{_libdir}/lib%{name}.so.${VERSION%.?}
# -devel subpackage
%{__install} -D -p -m 0644 %{name}.h %{buildroot}/%{_includedir}/%{name}.h
ln -s %{_libdir}/lib%{name}.so.$VERSION \
		%{buildroot}/%{_libdir}/lib%{name}.so

%files
%doc %{name}.conf LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files lib
%{_libdir}/lib%{name}.so.* 

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
