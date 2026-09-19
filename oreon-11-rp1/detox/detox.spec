%global source0_hash b3dac4f7fcfaa621c6fc5950a2c7e5747cdc9d78aacb9041875fad916b838e60

Name:		detox
Version:	3.0.1
Release:	%autorelease
Summary:	Utility to replace problematic characters in file names

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/dharple/detox
Source0:	https://github.com/dharple/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf automake flex flex-static
BuildRequires:	gcc
BuildRequires:	make

%description
Detox is a utility designed to clean up file names. It replaces difficult to
work with characters, such as spaces, with standard equivalents. It will also
clean up file names with UTF-8 or Latin-1 (or CP-1252) characters in them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}
%{_bindir}/inline-%{name}
%{_datadir}/%{name}
%doc README.md BUILD.md CHANGELOG.md THANKS.md
%license %{_docdir}/detox/LICENSE
%{_mandir}/man5/detox*
%{_mandir}/man1/inline-detox.1.gz
%{_mandir}/man1/detox*

%changelog
%autochangelog
