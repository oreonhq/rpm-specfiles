%global source0_hash 68b5c12bde559f11e362e3bfe92601c525893f7a2349c7a75198c54d3ea2cce2
ExcludeArch: %{ix86}
%global giturl  https://github.com/ygrek/ocurl
Name:           ocaml-curl
Version:        0.10.0
Release:        4%{?dist}
Summary:        OCaml Curl library (ocurl)
License:        MIT
URL:            https://ygrek.org/p/ocurl
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/ocurl-%{version}.tar.gz
# oreon:deps
BuildRequires:  libcurl-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-lwt-ppx-devel
# /oreon:deps
%description
The Ocaml Curl Library (Ocurl) is an interface library for the
programming language Ocaml to the networking library libcurl.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       libcurl-devel%{?_isa} >= 7.28.0
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        lwt
Summary:        LWT bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    lwt
The %{name}-lwt package contains LWT bindings for %{name}.

%package        lwt-devel
Summary:        LWT development files for %{name}
Requires:       %{name}-lwt%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}
%description    lwt-devel
The %{name}-devel package contains libraries and signature files for
developing applications that use LWT with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ocurl-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install -s
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-curl-devel -f %{oreon_filedir}/ocaml-curl-devel.list
%files -n ocaml-curl-lwt -f %{oreon_filedir}/ocaml-curl-lwt.list
%files -n ocaml-curl-lwt-devel -f %{oreon_filedir}/ocaml-curl-lwt-devel.list

%changelog

%autochangelog
