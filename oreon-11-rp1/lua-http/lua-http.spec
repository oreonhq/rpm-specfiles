%global source0_hash 329605beb09ad544bd48130634074810720dc73392efd3b9f23390b336d27246
%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}
%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}
%global luapkgname http
Name:           lua-%{luapkgname}
Version:        0.3
Release:        1%{?dist}
Summary:        HTTP library for Lua
License:        MIT
URL:            https://github.com/daurnimator/lua-http
Source0:        https://github.com/daurnimator/lua-http/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Patch1:         0001-rst_closed.patch
Patch2:         0002-throw_kill_connection.patch
Patch3:         0003-handle-EOF-when-body_read_type-length.patch
Requires:       lua-basexx >= 0.2.0
Requires:       lua-binaryheap >= 0.3
Requires:       lua-fifo
Requires:       lua-luaossl >= 20161208
Requires:       lua-lpeg
Requires:       lua-lpeg-patterns >= 0.5
Requires:       lua-cqueues >= 20171014
# oreon:deps
BuildRequires:  lua
BuildRequires:  make
BuildRequires:  pandoc
# /oreon:deps
%description
lua-http is an efficient, capable HTTP and WebSocket library for Lua.

%package doc
Summary:        Documentation for HTTP library for Lua
Requires:       %{name} = %{version}
%description doc
Documentation for the HTTP library for Lua.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build

pushd doc
%make_build lua-http.html lua-http.3
popd
%install
install -d -m 0755 "%{buildroot}%{_pkgdocdir}"
install -p -m 0644 doc/lua-http.html "%{buildroot}%{_pkgdocdir}/index.html"
install -D -p -m 0644 doc/lua-http.3 "%{buildroot}%{_mandir}/man3/lua-http.3"
install -d -m 0755 %{buildroot}%{luapkgdir}/%{luapkgname}
install -p -m 0644 %{luapkgname}/*.lua -t "%{buildroot}%{luapkgdir}/%{luapkgname}/"
install -d -m 0755 %{buildroot}%{luapkgdir}/%{luapkgname}/compat
install -p -m 0644 %{luapkgname}/compat/*.lua -t "%{buildroot}%{luapkgdir}/%{luapkgname}/compat/"
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lua-http-doc -f %{oreon_filedir}/lua-http-doc.list

%changelog

%autochangelog
