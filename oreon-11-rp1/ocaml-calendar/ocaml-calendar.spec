# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# ocaml-alcotest requires ocaml-astring, ocaml-cmdliner, ocaml-fmt, and ocaml-uutf,
# none of which are otherwise needed for building the OCaml-dependent packages
# found in RHEL and ELN.  We want to avoid the extra dependencies there.
%bcond tests %[!0%{?rhel}]

%global giturl  https://github.com/ocaml-community/calendar

Name:           ocaml-calendar
Epoch:          1
Version:        3.0.0
Release:        21%{?dist}
Summary:        Objective Caml library for managing dates and times
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://ocaml-community.github.io/calendar/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/calendar-%{version}.tar.gz
# Work around https://github.com/ocaml-community/calendar/issues/43
Patch:          %{name}-timezone-test.patch

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-re-devel >= 1.7.2

%if %{with tests}
BuildRequires:  ocaml-alcotest-devel
%endif


%description
Objective Caml library for managing dates and times.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n calendar-%{version} -p1


%build
%dune_build


%install
%dune_install


%if %{with tests}
%check
%dune_check
%endif


%files -f .ofiles
%doc CHANGES README.md TODO
%license LGPL COPYING


%files devel -f .ofiles-devel
%doc CHANGES README.md TODO calendarFAQ-2.6.txt
%license LGPL COPYING


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.0-21
- Prepare for Oreon 11 (RP1)
