%global source0_hash e41ddc3a473b555bdc0cbd80703dcb1f4610c1a7700d3b9d3d0c14a416e1074b

Name:           fcgi
Version:        2.4.7
Release:        2%{?dist}
Summary:        FastCGI development kit

License:        OML
URL:            https://github.com/FastCGI-Archives/%{name}2
Source0:        %{url}/archive/%{version}/%{name}2-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed

# The new author calls the project fcgi2, even though the changes to the original code are merely maintenance and bug fixes
# To avoid confusion, add a Provides here so it can be installed by the new name, fcgi2, as well as the old
Provides:       %{name}2 = %{version}-%{release}

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

# make sure all static libraries are deleted
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -type f -delete -print

# Now that the manpages have been installed into their proper place, remove them from the docs subfolder
rm -f doc/*.{1,3}
#rm -f -- doc/*.1
#rm -f -- doc/*.3

%check
# nothing to do, no tests are available

%files
%license LICENSE
%doc README.md README.supervise
%{_bindir}/cgi-fcgi
%{_libdir}/libfcgi.so.*
%{_libdir}/libfcgi++.so.*
%{_mandir}/man1/cgi-fcgi.1*

%files devel
%doc doc/
%{_includedir}/*
%{_libdir}/pkgconfig/fcgi.pc
%{_libdir}/pkgconfig/fcgi++.pc
%{_libdir}/libfcgi.so
%{_libdir}/libfcgi++.so
%{_mandir}/man3/FCGI*.3*

%changelog
%autochangelog
