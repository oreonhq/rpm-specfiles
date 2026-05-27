%global source0_hash 2dc6952b70283888994ae6e551a79039781f0a64c67fb637bffd5a8f483c34c5

Name:           fdk-aac-free
Version:        2.0.3
Release:        2%{?dist}
Summary:        Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library for Android

License:        FDK-AAC
URL:            https://cgit.freedesktop.org/~wtay/fdk-aac/log/?h=fedora
Source0:        https://wtaymans.fedorapeople.org/fdk-aac-free-%{version}.tar.gz

BuildRequires:  gcc gcc-c++
BuildRequires:  automake libtool
BuildRequires: make

%description
The Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library
for Android is software that implements part of the MPEG Advanced Audio Coding
("AAC") encoding and decoding scheme for digital audio.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n fdk-aac-%{version}
autoreconf -vif

%build
%configure \
  --disable-silent-rules \
  --disable-static

%make_build


%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -print -delete

%ldconfig_scriptlets

%files
%doc ChangeLog README.fedora
%license NOTICE
%{_libdir}/*.so.2
%{_libdir}/*.so.2.0.3

%files devel
%doc documentation/*.pdf
%dir %{_includedir}/fdk-aac
%{_includedir}/fdk-aac/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.3-2
- Prepare for Oreon 11 (RP1)
