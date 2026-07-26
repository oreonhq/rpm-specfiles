%global source0_hash 46958060e66f35bcb8a51ba22da1c13d726d28a86c1cf520511bcf7914bef39e

Summary: Locale and ISO 2022 support for Unicode terminals

%global AppVersion 20250912

Name: luit
Version: 2.0.%{AppVersion}
Release: 7%{?dist}
License: MIT
URL: https://invisible-island.net/%{name}/
Source0: https://invisible-island.net/archives/%{name}/%{name}-%{AppVersion}.tgz
BuildRequires: gcc
BuildRequires: make
BuildRequires: zlib-devel

%description
Luit is a filter that can be run between an arbitrary application and a
UTF-8 terminal emulator.  It will convert application output  from  the
locale's  encoding  into  UTF-8,  and convert terminal input from UTF-8
into the locale's encoding.

Unlike the older XFree86/Xorg version of luit, this does not rely upon
the fontenc package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{AppVersion}

%build

%configure

%make_build

%install
%make_install

%files
%license COPYING
%doc %{name}.log.html
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
%autochangelog
