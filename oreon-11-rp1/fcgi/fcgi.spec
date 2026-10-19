%global source0_hash e41ddc3a473b555bdc0cbd80703dcb1f4610c1a7700d3b9d3d0c14a416e1074b
Name:           fcgi
Version:        2.4.7
Release:        1%{?dist}
Summary:        FastCGI development kit
License:        OML
URL:            https://github.com/FastCGI-Archives/%{name}2
Source0:        https://github.com/FastCGI-Archives/%{name}2/archive/%{version}/%{name}2-%{version}.tar.gz
Provides:       %{name}2 = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific APIs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{name}2-%{version}

# Delete files and folders we don't need
rm -rf Win32
find \( -name .git -or -name .gitignore \) -delete

# remove DOS End Of Line Encoding
sed -i 's/\r//' doc/fastcgi-prog-guide/ch2c.htm

# There are several files in the tarball that shouldn't have the executable bit set
find . -type f ! \( -name 'configure' -or -name '*.sh' -or -name 'distrib' \) -executable -print -exec chmod -x '{}' \;

%build

autoreconf --force --install
%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -type f -delete -print
rm -f doc/*.{1,3}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n fcgi-devel -f %{oreon_filedir}/fcgi-devel.list

%changelog

%autochangelog
