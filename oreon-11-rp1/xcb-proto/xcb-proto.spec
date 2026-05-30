%global source0_hash 2c1bacd2110f4799f74de6ebb714b94cf6f80fb112316b1219480fd22562148c

Name:           xcb-proto
Version:        1.17.0
Release:        9%{?dist}
Summary:        XCB protocol descriptions

License:        X11-distribute-modifications-variant
URL:            https://xcb.freedesktop.org/
Source0:        https://www.x.org/archive/individual/proto/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  autoconf automake
BuildRequires:  libxml2
BuildRequires:  make
BuildRequires:  python3-devel

%description
XCB is a project to enable efficient language bindings to the X11 protocol.
This package contains the protocol descriptions themselves.  Language
bindings use these protocol descriptions to generate code for marshalling
the protocol.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
autoreconf -fiv


%build
# Bit of a hack to get the pc file in /usr/share, so we can be noarch.
%configure --libdir=%{_datadir}
%make_build


%install
%make_install


%check
%make_build check


%files
%license COPYING
%doc NEWS README.md TODO doc/xml-xcb.txt
%{_datadir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml
%{python3_sitelib}/xcbgen


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-9
- Prepare for Oreon 11 (RP1)
