# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-csv
Version:        2.4
Release:        30%{?dist}
Summary:        OCaml library for reading and writing CSV files
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception

URL:            https://github.com/Chris00/ocaml-csv
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Remove references to a bytes library for OCaml 5.0 support
Patch0:         %{name}-bytes.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-uutf-devel
BuildRequires:  ocaml-lwt-devel


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
%autosetup -p1


%build
# _smp_mflags breaks the build for some reason.
# https://github.com/Chris00/ocaml-csv/issues/34
%dune_build -j1


%install
%dune_install -s

# Remove the csvtool META file and opam project
rm -r %{buildroot}%{ocamldir}/csvtool


%files -f .ofiles-csv
%license LICENSE.md
%{_bindir}/csvtool


%files devel -f .ofiles-csv-devel
%doc CHANGES.md README.md


%files lwt -f .ofiles-csv-lwt


%files lwt-devel -f .ofiles-csv-lwt-devel


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4-30
- Prepare for Oreon 11 (RP1)
