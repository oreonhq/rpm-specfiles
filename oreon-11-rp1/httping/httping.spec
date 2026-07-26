%global source0_hash d332fc5436bcf8290bcb4fe75b7019b90facfb64264dc3c7bc3407da27c18d77

%global debug_package %{nil}

Name:           httping
Version:        3.6
Release:        4%{?dist}
Summary:        Ping alike tool for http requests

License:        GPL-1.0-or-later AND OpenSSL
URL:            https://github.com/folkertvanheusden/HTTPing/
Source0:        https://github.com/folkertvanheusden/HTTPing/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         9524733e67454518ee1075a47f3c21166543e620.patch
Patch1:         7f76370729c594180348f94feb4216fd14e12abd.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine

%description
Httping is like 'ping' but for HTTP requests. Give it an URL, and it will 
show you how long it takes to connect, send a request and retrieve the
reply (only the headers). Be aware that the transmission across the network
also takes time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n HTTPing-%{version} -p1

%build
%cmake -DUSE_TUI=1 -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/%{_docdir}

%files
%doc README.md plot-json.py
%license LICENSE
%{_bindir}/httping
%{_mandir}/httping.1

%changelog
%autochangelog
