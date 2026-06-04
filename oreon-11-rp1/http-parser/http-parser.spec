%global source0_hash 467b9e30fd0979ee301065e70f637d525c28193449e1b13fbcb1b1fab3ad224f

Name:           http-parser
Version:        2.9.4
Release:        16%{?dist}
Summary:        HTTP request/response parser for C

License:        MIT
URL:            https://github.com/nodejs/http-parser
Source0:        https://github.com/nodejs/http-parser/archive/refs/tags/v2.9.4/http-parser-2.9.4.tar.gz
# https://github.com/nodejs/http-parser/pull/483
Patch0001:      0001-url-treat-empty-port-as-default.patch

BuildRequires:  meson
BuildRequires:  gcc

%description
This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP applications.
It does not make any syscalls nor allocations, it does not buffer data, it can
be interrupted at anytime. Depending on your architecture, it only requires
about 40 bytes of data per message stream (in a web server that is per
connection).

%package devel
Summary:        Development headers and libraries for http-parser
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development headers and libraries for http-parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%ifarch %{arm}
# https://github.com/nodejs/http-parser/issues/507
sed -i -e "/sizeof(http_parser)/d" test.c
%endif
# TODO: try to send upstream?
cat > meson.build << EOF
project('%{name}', 'c', version : '%{version}')
install_headers('http_parser.h')
foreach x : [['http_parser',        ['-DHTTP_PARSER_STRICT=0']],
             ['http_parser_strict', ['-DHTTP_PARSER_STRICT=1']]]
  lib = library(x.get(0), 'http_parser.c',
                c_args : x.get(1),
                version : '%{version}',
                install : true)
  test('test-@0@'.format(x.get(0)),
       executable('test-@0@'.format(x.get(0)), 'test.c',
                  c_args : x.get(1),
                  link_with : lib),
       timeout : 60)
endforeach
EOF

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license LICENSE-MIT
%doc AUTHORS README.md
%{_libdir}/libhttp_parser.so.*
%{_libdir}/libhttp_parser_strict.so.*

%files devel
%{_includedir}/http_parser.h
%{_libdir}/libhttp_parser.so
%{_libdir}/libhttp_parser_strict.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.4-16
- Prepare for Oreon 11 (RP1)
