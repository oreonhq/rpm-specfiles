%global source0_hash 7b0d7aee291273ae02b661d14330e4e803ab6b673cd4aec39c0a00a5de2b793d
%bcond tests 1
Name:           forge-srpm-macros
Version:        0.4.0
Release:        1%{?dist}
Summary:        Macros to simplify packaging of forge-hosted projects
License:        GPL-1.0-or-later
URL:            https://git.sr.ht/~gotmax23/forge-srpm-macros
BuildArch:      noarch
Source0:        https://git.sr.ht/~gotmax23/forge-srpm-macros/archive/v0.4.0.tar.gz#/forge-srpm-macros-0.4.0.tar.gz
%if %{with tests}
%endif
%if (0%{?fedora} >= 40 || 0%{?rhel} >= 10) || (0%{?oreon} >= 11)
Requires:       redhat-rpm-config >= 266-1
%elif 0%{?fedora} == 39
Requires:       redhat-rpm-config >= 265-1
%else
Requires:       redhat-rpm-config
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
BuildRequires:  python3-rpm-macros
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%if %{defined el9}
%make_build epel9-build
%endif
%install
%make_build \
    DESTDIR=%{buildroot} \
    RPMMACRODIR=%{_rpmmacrodir} RPMLUADIR=%{_rpmluadir} %{?el9:epel9-}install
%oreon_autofiles main

%check

%if %{with tests}
export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
export MACRO_LUA_DIR="%{buildroot}%{_rpmluadir}"
%pytest
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.0-4
- Import
