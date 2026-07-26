%global source0_hash a24daf6b363a9a2bd7d37a75bf42fb9fbe831c44c17fa8dda587237d005cd6e1

%global srcname fast_xml
%global p1_utils_ver 1.0.28

Name: erlang-%{srcname}
Version: 1.1.57
Release: %autorelease
License: Apache-2.0
Summary: Fast Expat based Erlang XML parsing and manipulation library
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:   erlang-fast_xml-0001-Disable-Rebar3-plugins.patch
Provides:  erlang-p1_xml = %{version}-%{release}
Obsoletes: erlang-p1_xml < 1.1.11
BuildRequires: erlang-edoc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: expat-devel
BuildRequires: gcc

%description
Fast Expat based Erlang XML parsing and manipulation library, with a strong
focus on XML stream parsing from network. It supports full XML structure
parsing, suitable for small but complete XML chunks, and XML stream parsing
suitable for large XML document, or infinite network XML stream like XMPP.
This module can parse files much faster than built-in module xmerl. Depending
on file complexity and size xml_stream:parse_element/1 can be 8-18 times faster
than calling xmerl_scan:string/2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/lib
gcc  c_src/fxml.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fxml.o
gcc c_src/fxml_stream.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fxml_stream.o
gcc c_src/fxml.o	$LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lexpat -lm -o priv/lib/fxml.so
gcc c_src/fxml_stream.o	$LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lexpat -lm -o priv/lib/fxml_stream.so

%install
%{erlang3_install}
install -p -D -m 755 priv/lib/* --target-directory=$RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{erlang_appdir}

%changelog
%autochangelog
