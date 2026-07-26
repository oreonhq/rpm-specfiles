%global source0_hash 40f5472df5f6356a4d6f48862a19091bd4de3f802b3444891b3bc4b710fb35ca

Name:           yank
Version:        1.3.0
Release:        9%{?dist}
Summary:        Tool for selecting and copying text from stdin without a mouse

License:        MIT
URL:            https://github.com/mptre/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

Requires:       bash

# Executable 'yank' already exists in another package (EMBOSS-6.6.0-3.fc24.x86_64). Binary is 'yank-cli'.
%global name_change yank-cli

%description
Read input from stdin and display a selection interface that allows a field 
to be selected and copied to the clipboard. Fields are either recognized by 
a regular expression using the -g option or by splitting the input on a 
delimiter sequence using the -d option.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
CFLAGS=${RPM_OPT_FLAGS} %make_build PROG=%{name_change}

%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir} INSTALL_PROGRAM='install -m 0755' PROG=%{name_change}

# Provide the same manpage for both 'yank' and 'yank-cli'
ln -s %{_mandir}/man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name_change}.1

%files
%{_bindir}/%{name_change}
%{_mandir}/man1/%{name}*
%{_mandir}/man1/%{name_change}*
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog
