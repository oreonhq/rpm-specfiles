%global source0_hash b5eb42995836eff58767e1ccc0a6551c2ac74f358094ac2402334389b075fba8

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/issuuArchive/ocaml-zmq

Name:           ocaml-zmq
Version:        5.3.0
Release:        11%{?dist}
Summary:        ZeroMQ bindings for OCaml

License:        MIT
URL:            https://issuuarchive.github.io/ocaml-zmq/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/zmq-%{version}.tbz

BuildRequires:  ocaml >= 4.04.1
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-lwt-devel >= 2.6.0
BuildRequires:  ocaml-ounit2-devel
BuildRequires:  pkgconfig(libzmq)

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

# We don't want a fake zmq-async install
rm -fr %{buildroot}%{ocamldir}/zmq-async

# We don't want a fake zmq-eio install
rm -fr %{buildroot}%{ocamldir}/zmq-eio

%check
%dune_check

%files -f .ofiles-zmq
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-zmq-devel

%files lwt -f .ofiles-zmq-lwt

%files lwt-devel -f .ofiles-zmq-lwt-devel

%changelog
%autochangelog
