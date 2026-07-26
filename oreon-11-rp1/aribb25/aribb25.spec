%global source0_hash a437d3b7975db1732c18dcdc66f92bb11e21f0a0b33b95fab4e60f3a40508301

Name:           aribb25
Version:        0.2.7
Release:        8%{?dist}
Summary:        Basic implementation of the ARIB STD-B25 public standard
License:        ISC
URL:            https://code.videolan.org/videolan/aribb25

Source0:        https://download.videolan.org/pub/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libpcsclite)

%description
This implementation currently only allows playback of ARIB scrambled streams.

With the end of analog TV in Japan in July 2011 a wish for cheap Digital TV
receivers emerged. Although, the voluntary introduced complexity in the ARIB
standard makes it really hard to understand, induces higher development costs
for device manufacturers and then nullifies the chances of having low cost
receivers on the market.

For that reason, this library gathers most of the necessary specification into a
comprehensible code that can be used as a starting point.

The Conditional Access system (CA) accordingly to the associated B-CAS Card will
decrypt TS streams using the ECM table 0x82 and EMM table 0x84.
EMM table 0x85 messages processing are to be done.

Conditional Access Cards can be read through any ISO-7816 compliant IC card
reader.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

# Let RPM pick up docs directly in the files section:
rm -fr %{buildroot}%{_docdir}

%files
%license LICENCE
%doc README.md README.jp.txt
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.0.0

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
