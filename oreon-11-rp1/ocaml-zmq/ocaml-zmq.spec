%global source0_hash b5eb42995836eff58767e1ccc0a6551c2ac74f358094ac2402334389b075fba8
ExcludeArch: %{ix86}
%global giturl  https://github.com/issuuArchive/ocaml-zmq
Name:           ocaml-zmq
Version:        5.3.0
Release:        1%{?dist}
Summary:        ZeroMQ bindings for OCaml
License:        MIT
URL:            https://issuuarchive.github.io/ocaml-zmq/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/zmq-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-ounit2-devel
BuildRequires:  pkgconfig(libzmq)
# /oreon:deps
%description
This library contains basic OCaml bindings for ZeroMQ.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zeromq-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        lwt
Summary:        LWT-aware ZeroMQ bindings for OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    lwt
This library contains lwt-aware OCaml bindings for ZeroMQ.

%package        lwt-devel
Summary:        Development files for %{name}-lwt
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-lwt%{?_isa} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
%description    lwt-devel
The %{name}-lwt-devel package contains libraries and signature files for
developing applications that use %{name}-lwt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n zmq-%{version} -p1

%conf
# We cannot build the async-aware bindings until ocaml-async-kernel and
# ocaml-async-unix have been added to Fedora.
rm -fr zmq-async*

# We cannot build the eio-aware bindings until ocaml-eio and
# ocaml-eio-main have been added to Fedora.
rm -fr zmq-eio*

# Work around for ocaml-zmq 5.2.2.  See if later versions fixed this.
# https://github.com/issuu/ocaml-zmq/issues/128
sed -i 's/sleep 10/&00/' zmq/test/zmq_test.ml

%build

%dune_build
%install
%dune_install -s
rm -fr %{buildroot}%{ocamldir}/zmq-async
rm -fr %{buildroot}%{ocamldir}/zmq-eio
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-zmq-devel -f %{oreon_filedir}/ocaml-zmq-devel.list
%files -n ocaml-zmq-lwt -f %{oreon_filedir}/ocaml-zmq-lwt.list
%files -n ocaml-zmq-lwt-devel -f %{oreon_filedir}/ocaml-zmq-lwt-devel.list

%changelog

%autochangelog
