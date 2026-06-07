%global source0_hash none

%global has_which2_alias 1

Summary: Displays where a particular program in your path is located
Name: which
Version: 2.23
Release: 4%{?dist}
License: GPL-3.0-only
Source0:        https://mirrors.kernel.org/gnu/which/%{name}-%{version}.tar.gz
Source1: which2.sh
Source2: which2.csh
Patch0: which-2.21-warning.patch
Url: https://savannah.gnu.org/projects/which/
Requires: coreutils
BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: readline-devel

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
 
%build
%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
%if %{has_which2_alias}
    install -p -m 644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
%endif
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%license COPYING
%doc EXAMPLES README AUTHORS NEWS
%if %{has_which2_alias}
%attr(0644,root,root) %{_sysconfdir}/profile.d/which2.*
%endif
%{_bindir}/which
%{_infodir}/which.info*
%{_mandir}/man1/which.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.23-4
- Prepare for Oreon 11 (RP1)
