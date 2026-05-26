# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-camomile
Version:        2.0.0
Release:        21%{?dist}
Summary:        Unicode library for OCaml

# LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception: the project as a whole
# ICU: files in src/locales; see src/locales/license.html
# Unicode-TOU: files in src/unidata; see src/unidata/UnicodeData.html using Unicode-3.0
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/30
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception AND ICU AND Unicode-3.0
URL:            https://github.com/ocaml-community/Camomile
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-community/Camomile/archive/v2.0.0/Camomile-2.0.0.tar.gz

# Fix a licensing issue in EO Unicode files.  Submitted but not
# accepted upstream: https://github.com/yoriyuki/Camomile/pull/84
Patch1:         0001-Camomile-locales-eo.txt-Fix-license-by-importing-dat.patch
# oreon url source checksums begin
%global source0_sha256 6bb421d0bb81594acb5dd902101a0609022d576fe373d956724fa60120bfd03d
%global source0_file Camomile-2.0.0.tar.gz
# oreon url source checksums end

BuildRequires:  ocaml >= 4.13
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-dune >= 3.4
BuildRequires:  ocaml-dune-site-devel
BuildRequires:  ocaml-stdlib-random-devel

# The base package requires the data files.  Note that it is possible
# to install the data files on their own to support other packages
# that need the mappings, and some packages (eg. guestfs-browser) do
# exactly this.
Requires:       %{name}-data = %{version}-%{release}


%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camlp-streams-devel%{?_isa}
Requires:       ocaml-dune-site-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch


%description    data
The %{name}-data package contains data files for developing
applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Camomile-2.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6bb421d0bb81594acb5dd902101a0609022d576fe373d956724fa60120bfd03d" || { echo "oreon: Source0 SHA256 mismatch for Camomile-2.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n Camomile-%{version}


%build
# This avoids a stack overflow in the OCaml compiler on POWER only.
# Originally found with OCaml 4.05, still affecting 4.13.0.
# https://github.com/yoriyuki/Camomile/issues/39
%ifarch %{power64}
ulimit -Hs 65536
ulimit -Ss 65536
%endif
%dune_build


%install
%dune_install

# The data files are in their own package
sed -i '\@%{_datadir}@d' .ofiles


%check
%dune_check


%files -f .ofiles
%doc README.md CHANGES.md
%license LICENSE.md


%files devel -f .ofiles-devel
%license LICENSE.md


%files data
%license LICENSE.md
%{_datadir}/camomile/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-21
- Prepare for Oreon 11 (RP1)
