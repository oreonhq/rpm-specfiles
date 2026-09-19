%global source0_hash dc2d0ff651c2b275bc4af3af8ba59851a6fb6e1eaddc20ae75fb60b1e90126ec

Name:           newlisp
Version:        10.7.5
Release:        %autorelease
Summary:        Lisp-like general purpose scripting
License:        GPL-3.0-or-later
URL:            http://www.newlisp.org
Source0:        http://www.newlisp.org/downloads/%{name}-%{version}.tgz
Patch0:         %{name}-0000-Support-64bit.patch
Patch1:         %{name}-0003-Don-t-strip-the-resulting-binary.patch
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  make
BuildRequires:  readline-devel
# This is required for the modules for newLisp
Requires:       openssl-devel%{?_isa} gmp-devel%{_isa} gsl-devel%{_isa}
Requires:       mariadb-connector-c-devel%{?_isa} libpq-devel
Requires:       sqlite-devel%{?_isa} zlib-devel%{?_isa}

%description
Lisp-like general purpose scripting language. %{name} is well suited for
applications in AI, web search. It also can be used for embedded systems
applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .64bit-support
%patch -P1 -p1 -b .stop-binary-strip

# Remove it from the general build and specify it on supported platforms below
sed -i.m32 's/\-m32 //' makefile_linux
sed -i.m64 's/\-m64 //' makefile_linuxLP64
sed -i.m32 's/\-m32 //' makefile_linux_utf8
sed -i.m64 's/\-m64 //' makefile_linuxLP64_utf8

%build
%configure

%if "%{_lib}" == "lib64"
CFLAGS="%{optflags} -c -DREADLINE -DSUPPORT_UTF8 -DLINUX -DNEWLISP64" \
        make -f makefile_linuxLP64_utf8 %{?_smp_mflags}
%else
CFLAGS="%{optflags} -c -DREADLINE -DSUPPORT_UTF8 -DLINUX" \
        make -f makefile_linux_utf8 %{?_smp_mflags}
%endif

%install
make install_home HOME=%{buildroot}/usr/

%files
%doc %{_datadir}/doc/*
%{_bindir}/%{name}
%{_bindir}/newlispdoc
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/util/%{name}.vim
%{_datadir}/%{name}/modules/*
%attr(0755,-,-) %{_datadir}/%{name}/util/syntax.cgi

%changelog
%autochangelog
