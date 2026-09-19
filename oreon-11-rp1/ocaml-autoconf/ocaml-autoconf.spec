%global source0_hash dca81a55d755912b229de33fd4fed93ead9319e9bb9c545bc745eee98a7884ae

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-autoconf
Version:        1.1
Release:        47%{?dist}
Summary:        Autoconf macros for OCaml

License:        BSD-3-Clause

URL:            https://forge.ocamlcore.org/projects/ocaml-autoconf/
Source0:        https://forge.ocamlcore.org/frs/download.php/282/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  /usr/bin/perldoc

# Runtime requires /usr/share/aclocal subdirectory.
Requires:       automake

%description
Autoconf macros for OCaml projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
  prefix=%{_prefix} \
  datadir=%{_datadir} \
  mandir=%{_mandir} \
  DESTDIR=$RPM_BUILD_ROOT

%files
%doc README LICENSE
%{_mandir}/man1/*.1*
%{_datadir}/aclocal/ocaml.m4

%changelog
%autochangelog
