%global source0_hash 16f4dd2d64da38690946a9670e59bc72a789cf6a323f792e159bb3a39cf4a7f5

%global baseurl https://6xq.net
%global common_description %{expand:
pianobar is a free/open-source, console-based client for the personalized
online radio Pandora.}

Name:           pianobar
Version:        2024.12.21
Release:        4%{?dist}
Summary:        Console-based client for Pandora

License:        MIT
URL:            %{baseurl}/%{name}
Source:         %{url}/%{name}-%{version}.tar.bz2
Source:         %{url}/%{name}-%{version}.tar.bz2.sha256
Source:         %{url}/%{name}-%{version}.tar.bz2.asc
Source:         %{baseurl}/08D8092A.gpg

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  gnutls-devel
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmad-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  json-c-devel

BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavfilter)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    %{common_description}

Features
* play and manage (create, add more music, delete, rename, ...) stations
* rate songs and explain why they have been selected
* upcoming songs/song history
* customize keybindings and text output
* remote control and eventcmd interface (send tracks to last.fm, for example)
* proxy support for listeners outside the USA

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains development headers and libraries for %{name}.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs %{common_description}

This package contains shared libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Verify source tarball
(cd "%{_sourcedir}" && sha256sum --check "%{SOURCE1}")
%{gpgverify} --keyring="%{SOURCE3}" --signature="%{SOURCE2}" --data="%{SOURCE0}"

# Preserve timestamps on install
sed -i 's/install /install -p /g' Makefile

%build
%make_build DYNLINK=1 V=1

%install
%make_install DYNLINK=1 PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

# Fix shared library permissions
chmod +x %{buildroot}%{_libdir}/libpiano.so.0.0.0

# We don't want the static library
rm %{buildroot}%{_libdir}/libpiano.a

%files
%doc ChangeLog README.rst
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/piano.h
%{_libdir}/libpiano.so

%files libs
%license COPYING
%{_libdir}/libpiano.so.0{,.*}

%changelog
%autochangelog
