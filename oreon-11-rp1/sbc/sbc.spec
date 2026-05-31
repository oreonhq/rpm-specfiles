%global source0_hash 426633cabd7c798236443516dfa8335b47e004b0ef37ff107e0c7ead3299fcc2

Name:          sbc
Version:       2.1
Release:       %autorelease
Summary:       Sub Band Codec used by bluetooth A2DP

License:       GPL-2.0-only AND LGPL-2.1-or-later
URL:           http://www.bluez.org
Source0:        http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: libsndfile-devel
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
SBC (Sub Band Codec) is a low-complexity audio codec used in the Advanced Audio 
Distribution Profile (A2DP) bluetooth standard but can be used standalone. It 
uses 4 or 8 subbands, an adaptive bit allocation algorithm in combination with 
an adaptive block PCM quantizers.

%package -n libsbc
Summary: Library for the SBC (Sub Band Codec)

%description -n libsbc
Library for SBC (Sub Band Codec) is a low-complexity audio codec used in the
Advanced Audio Distribution Profile (A2DP) bluetooth standard but can be used
standalone. It uses 4 or 8 subbands, an adaptive bit allocation algorithm in
combination with an adaptive block PCM quantizers.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%configure --disable-static

%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog
%{_bindir}/sbc*

%files -n libsbc
%license COPYING
%{_libdir}/libsbc.so.1*

%files devel
%{_includedir}/sbc/
%{_libdir}/pkgconfig/sbc.pc
%{_libdir}/libsbc.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-1
- Prepare for Oreon 11 (RP1)
