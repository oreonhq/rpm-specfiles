%global source0_hash 9fcd00271e461ec9deda4aef83155f9f8c9125490123fc11121df48e11f4142e

Name:           R-websocket
Version:        %R_rpm_version 1.4.4
Release:        %autorelease
Summary:        'WebSocket' Client Library

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(websocketpp)

%description
Provides a WebSocket client interface for R. WebSocket is a protocol for
low-overhead real-time communication:
<https://en.wikipedia.org/wiki/WebSocket>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# unbundle https://github.com/rstudio/websocket/issues/59
pushd websocket/src/lib
    rm -rf websocketpp update.sh
    cp -r %{_includedir}/websocketpp .
    find . -type f -print0 | xargs -0 sed -i 's/websocketpp::/ws_websocketpp::/g'
    find . -type f -print0 | xargs -0 sed -i 's/namespace websocketpp/namespace ws_websocketpp/g'
    find . -type f -print0 | xargs -0 sed -i 's/&std::cout/(std::ostream*)\&WrappedOstream::cout/g'
    find . -type f -print0 | xargs -0 sed -i 's/&std::cerr/(std::ostream*)\&WrappedOstream::cerr/g'
popd
# remove https://github.com/rstudio/websocket/issues/111
sed -i '/openssl\/engine/d' websocket/src/tests/main.c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
