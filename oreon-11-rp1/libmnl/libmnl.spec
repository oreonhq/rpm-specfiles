Name:          libmnl
Version:       1.0.5
Release:       9%{?dist}
Summary:       Minimalistic Netlink user-space library

License:       LGPL-2.1-or-later
URL:           https://netfilter.org/projects/libmnl/
Source0:       https://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2
Source1:       https://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2.sig
Source2:       https://netfilter.org/files/coreteam-gpg-key-0xD55D978A8A1420E4.txt
# oreon url source checksums begin
%global source0_sha256 274b9b919ef3152bfb3da3a13c950dd60d6e2bcd54230ffeca298d03b40d0525
%global source0_file libmnl-1.0.5.tar.bz2
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: make

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong.
This library aims to provide simple helpers that allows you to re-use code and
to avoid re-inventing the wheel.


%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%package       static
Summary:       Static development files for %{name}
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description   static
The %{name}-static package contains static libraries for developing
applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libmnl-1.0.5.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "274b9b919ef3152bfb3da3a13c950dd60d6e2bcd54230ffeca298d03b40d0525" || { echo "oreon: Source0 SHA256 mismatch for libmnl-1.0.5.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'


%build
%configure --enable-static
%make_build CFLAGS="%{optflags}"


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete
find examples '(' -name 'Makefile.am' -o -name 'Makefile.in' ')' -delete
find examples -type d -name '.deps' -prune -exec rm -rf {} ';'
mv examples examples-%{_arch}


%ldconfig_scriptlets


%files
%license COPYING
%doc README
%{_libdir}/%{name}.so.0*

%files devel
%doc examples-%{_arch}
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files static
%{_libdir}/%{name}.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.5-9
- Prepare for Oreon 11 (RP1)
