%global source0_hash 14b1173d2a64053e06571cbe4a86fa4be4b48ea190d1f0c389ce34fd9800c665
ExcludeArch: %{ix86}
Name:           ocaml-csv
Version:        2.4
Release:        1%{?dist}
Summary:        OCaml library for reading and writing CSV files
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/Chris00/ocaml-csv
VCS:            git:%{url}.git
Source0:        https://github.com/Chris00/ocaml-csv/archive/refs/tags/2.4.tar.gz#/ocaml-csv-2.4.tar.gz
Patch0:         %{name}-bytes.patch
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-uutf-devel
# /oreon:deps
%description
This OCaml library can read and write CSV files, including all
extensions used by Excel - eg. quotes, newlines, 8 bit characters in
fields, quote-0 etc.

The library comes with a handy command line tool called csvtool for
handling CSV files from shell scripts.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
%oreon_prep
%build

%dune_build -j1
%install
%dune_install -s
rm -r %{buildroot}%{ocamldir}/csvtool
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-csv-devel -f %{oreon_filedir}/ocaml-csv-devel.list
%files -n ocaml-csv-lwt -f %{oreon_filedir}/ocaml-csv-lwt.list
%files -n ocaml-csv-lwt-devel -f %{oreon_filedir}/ocaml-csv-lwt-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4-30
- Prepare for Oreon 11 (RP1)
