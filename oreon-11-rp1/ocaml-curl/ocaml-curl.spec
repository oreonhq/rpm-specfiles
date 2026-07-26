%global source0_hash 68b5c12bde559f11e362e3bfe92601c525893f7a2349c7a75198c54d3ea2cce2

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
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

BuildRequires:  libcurl-devel >= 7.28.0
BuildRequires:  ocaml >= 4.11
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-dune-configurator-devel >= 3.18.1
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-lwt-ppx-devel

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

%autosetup -p1 -n ocurl-%{version}

%build
%dune_build

%install
%dune_install -s

%check
%dune_check

%files -f .ofiles-curl -f .ofiles-ocurl
%doc CHANGES.txt README.md
%license COPYING

%files devel -f .ofiles-curl-devel -f .ofiles-ocurl-devel
%doc examples

%files lwt -f .ofiles-curl_lwt

%files lwt-devel -f .ofiles-curl_lwt-devel

%changelog
%autochangelog
