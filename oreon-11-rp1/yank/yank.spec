%global source0_hash 0f1d1000f358bfa373f3903ea2871e2585fa694a0b03d8ff7561c1205207dec5
Name:           yank
Version:        1.4.0
Release:        1%{?dist}
Summary:        Tool for selecting and copying text from stdin without a mouse
License:        MIT
URL:            https://github.com/mptre/%{name}
Source0:        https://github.com/mptre/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       bash
%global name_change yank-cli
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Read input from stdin and display a selection interface that allows a field 
to be selected and copied to the clipboard. Fields are either recognized by 
a regular expression using the -g option or by splitting the input on a 
delimiter sequence using the -d option.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

CFLAGS=${RPM_OPT_FLAGS} %make_build PROG=%{name_change}
%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir} INSTALL_PROGRAM='install -m 0755' PROG=%{name_change}
ln -s %{_mandir}/man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name_change}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
