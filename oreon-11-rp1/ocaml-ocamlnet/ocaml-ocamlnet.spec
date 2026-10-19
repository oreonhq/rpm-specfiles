%global source0_hash f98ed19979848f1949b1b001e30ac132b254d0f4a705150c6dcf9094bbec9cee
ExcludeArch: %{ix86}
Name:           ocaml-ocamlnet
Version:        4.1.9
Release:        1%{?dist}
Summary:        Network protocols for OCaml
License:        BSD-3-Clause
URL:            http://projects.camlcity.org/projects/ocamlnet.html
VCS:            git:https://gitlab.com/gerdstolpmann/lib-ocamlnet3.git
Source0:        http://download.camlcity.org/download/ocamlnet-%{version}.tar.gz
Patch:          0001-configure-Avoid-implicit-ints.patch
Patch:          0002-Build-ocamlrpcgen-as-native-code.patch
Patch:          0003-Make-library-linkage-explicit.patch
Patch:          0004-started-porting-to-OCaml-5.patch
Patch:          0005-more-build-fixes-for-OCaml-5.patch
Patch:          0006-Further-OCaml-5-changes.patch
Patch:          0007-netsys_c.h-Don-t-redefine-caml_ba_element_size.patch
Patch:          0008-configure-Assume-we-have-the-Bytes-type-immutable-st.patch
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings
# oreon:deps
BuildRequires:  gnutls-devel
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  ocaml-labltk-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  tcl-devel
# /oreon:deps
%description
Ocamlnet is an ongoing effort to collect modules, classes and
functions that are useful to implement network protocols. Since
version 2.2, Ocamlnet incorporates the Equeue, RPC, and Netclient
libraries, so it is now really a big player.

In detail, the following features are available:

 * netstring is about processing strings that occur in network
   contexts. Features: MIME encoding/decoding, Date/time parsing,
   Character encoding conversion, HTML parsing and printing, URL
   parsing and printing, OO-representation of channels, and a lot
   more.

 * netcgi2 focuses on portable web applications.

 * rpc implements ONCRPC (alias SunRPC), the remote procedure call
   technology behind NFS and other Unix services.

 * netplex is a generic server framework. It can be used to build
   stand-alone server programs from individual components like those
   from netcgi2, nethttpd, and rpc.

 * netclient implements clients for HTTP (version 1.1, of course), FTP
   (currently partially), and Telnet.

 * equeue is an event queue used for many protocol implementations. It
   makes it possible to run several clients and/or servers in parallel
   without having to use multi-threading or multi-processing.

 * shell is about calling external commands like a Unix shell does.

 * netshm provides shared memory for IPC purposes.

 * netsys contains bindings for system functions missing in core OCaml.

 * netsmtp and netpop are client implementations of the SMTP and POP3
   protocols.

 * Bindings for GnuTLS and GSSAPI (TLS/HTTPS support).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-lablgtk-devel%{?_isa}
Requires:       ocaml-pcre-devel%{?_isa}
Requires:       ocaml-zip-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        nethttpd
Summary:        Ocamlnet HTTP daemon
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    nethttpd
Nethttpd is a web server component (HTTP server implementation). It
can be used for web applications without using an extra web server, or
for serving web services.

%package        nethttpd-devel
Summary:        Development files for %{name}-nethttpd
License:        GPL-2.0-or-later
Requires:       %{name}-nethttpd%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description    nethttpd-devel
The %{name}-nethttpd-devel package contains libraries and signature
files for developing applications that use %{name}-nethttpd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n ocamlnet-%{version}
%autopatch -M 0 -p2
%ifarch %{ocaml_native_compiler}
%patch -P 1 -p2
%endif
%autopatch -m 2 -p2

# Fix the version number
# See https://gitlab.com/gerdstolpmann/lib-ocamlnet3/-/merge_requests/19
sed -i 's/^\(version=\).*/\1"%{version}"/' configure

# cmxs detection broken with OCaml 5.2
%ifarch %{ocaml_native_compiler}
sed -i 's,ocamlopt -shared -o \.dummy\.cmxs >/dev/null 2>/dev/null,true,' configure
%endif

# safe-string detection broken with OCaml 5.2
sed -i 's,ocamlc -safe-string >/dev/null 2>/dev/null,true,' configure

# opaque detection broken with OCaml 5.2
sed -i 's,ocamlc -opaque >/dev/null 2>/dev/null,true,' configure

%build

unset MAKEFLAGS
./configure \
  -bindir %{_bindir} \
  -datadir %{_datadir}/%{name} \
  -disable-apache \
  -enable-pcre \
  -enable-gtk2 \
  -enable-gnutls \
  -enable-gssapi \
  -enable-nethttpd \
  -enable-tcl \
  -enable-zip
%ifarch %{ocaml_native_compiler}
make opt ||:
%endif
make all
%ifarch %{ocaml_native_compiler}
make opt
%endif
%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/ocaml/rpc-generator/dummy.mli
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-ocamlnet-devel -f %{oreon_filedir}/ocaml-ocamlnet-devel.list
%files -n ocaml-ocamlnet-nethttpd -f %{oreon_filedir}/ocaml-ocamlnet-nethttpd.list
%files -n ocaml-ocamlnet-nethttpd-devel -f %{oreon_filedir}/ocaml-ocamlnet-nethttpd-devel.list

%changelog

%autochangelog
