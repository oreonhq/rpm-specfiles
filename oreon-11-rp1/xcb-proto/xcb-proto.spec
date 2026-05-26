Name:           xcb-proto
Version:        1.17.0
Release:        9%{?dist}
Summary:        XCB protocol descriptions

License:        X11-distribute-modifications-variant
URL:            https://xcb.freedesktop.org/
Source0:        https://xorg.freedesktop.org/archive/individual/proto/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 2c1bacd2110f4799f74de6ebb714b94cf6f80fb112316b1219480fd22562148c
%global source0_file xcb-proto-1.17.0.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xcb-proto-1.17.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2c1bacd2110f4799f74de6ebb714b94cf6f80fb112316b1219480fd22562148c" || { echo "oreon: Source0 SHA256 mismatch for xcb-proto-1.17.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
