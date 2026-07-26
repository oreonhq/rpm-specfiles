%global source0_hash 87539b62e1f8375506b0e81111bfa67ee54ee260fa02176b85e1df19cfabbc20

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global debug_package %{nil}

Name:           ocaml-xmlrpc-light
Version:        0.6.1
Release:        88%{?dist}
Summary:        OCaml library for writing XML-RPC clients and servers
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://code.google.com/archive/p/xmlrpc-light/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/xmlrpc-light/xmlrpc-light-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-ocamlnet-nethttpd-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  dos2unix

# Fix the package to work with ocamlnet 3.x.
Patch1:         debian_patches_0002-Compile-with-ocamlnet-3.3.5.patch

# Further fix the package to work with ocamlnet 4.x.
Patch2:         xmlrpc-light-0.6.1-ocamlnet4.patch

# Safe-string patches for OCaml 4.06.
Patch3:         xmlrpc-light-0.6.1-safe-string.patch

# Use camlp-streams for compatibility with OCaml 5.0
Patch4:         xmlrpc-light-0.6.1-camlp-streams.patch

%description
XmlRpc-Light is an XmlRpc library written in OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-xml-light-devel%{?_isa}
Requires:       ocaml-ocamlnet-devel%{?_isa}
Requires:       ocaml-ocamlnet-nethttpd-devel%{?_isa}
Requires:       ocaml-camlp-streams-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n xmlrpc-light-%{version} -p1
dos2unix LICENSE
dos2unix README.txt

%ifnarch %{ocaml_native_compiler}
# Do not try to build or install the native library
sed -i 's/ xmlrpc-light\.cmxa xmlrpc-light\.a//' Makefile
sed -i '/libinstall:/s/\tall/ byte-code-library/' OCamlMakefile
%endif

%build
%ifarch %{ocaml_native_compiler}
make
%else
make byte-code-library
%endif

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
%make_install
%ocaml_files

%files -f .ofiles
%license LICENSE

%files devel -f .ofiles-devel
%doc doc/xmlrpc-light/{html,latex} README.txt
%license LICENSE

%changelog
%autochangelog
