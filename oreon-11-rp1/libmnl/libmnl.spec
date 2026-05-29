%global source0_hash none

%global source2_key_fpr 37D964ACC04981C75500FB9BD55D978A8A1420E4

Name:          libmnl
Version:       1.0.5
Release:       9%{?dist}
Summary:       Minimalistic Netlink user-space library

License:       LGPL-2.1-or-later
URL:           https://netfilter.org/projects/libmnl/
Source0:        https://netfilter.org/projects/libmnl/files/libmnl-1.0.5.tar.bz2
Source1:        libmnl-1.0.5.tar.bz2.sig
Source2:       coreteam-gpg-key-0xD55D978A8A1420E4.txt

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
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
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
