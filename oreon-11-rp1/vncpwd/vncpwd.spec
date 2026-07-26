%global source0_hash ab9112b71afbc17b6100964b6358041877cb154849785baa1152d13b5c459070

%global         gituser         jeroennijhof
%global         gitname         vncpwd
%global         commit          58d585cbbc861bd6dbd9f6709ce8cb7f2afb75ba
%global         commitdate      20180223
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           vncpwd
Version:        0.1
Release:        10%{?dist}
Summary:        VNC Password Decrypter

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/jeroennijhof/vncpwd

# Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source0:        https://github.com/%{gituser}/%{gitname}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc

%description
The vncpwd decrypts the VNC password.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%make_build CFLAGS="%{optflags}"

%install
make install DESTDIR="%{buildroot}"

%files
%doc README
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
