%global source0_hash 6fd490b4446f3b2074918c0439761594a200327dcb9eb0bdfdee3c25ebba4efd

%global commit      136e5c25daf545753329d7cee1b06ae482fb9c44
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date    20220509

Summary:        Parallel LZMA compressor using XZ
Name:           pxz
Version:        4.999.9
Release:        32.beta.%{git_date}git%{?dist}
License:        GPL-2.0-or-later
URL:            https://jnovy.fedorapeople.org/pxz/
Source0:        https://github.com/jnovy/%{name}/archive/%{commit}/%{name}-%{version}beta.%{git_date}git%{shortcommit}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  xz-devel
Requires:       %{_bindir}/xz

%description
Parallel XZ is a compression utility that takes advantage of running
XZ compression simultaneously on different parts of an input file on
multiple cores and processors. This significantly speeds up compression
time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}

%build
export CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DXZ_BINARY='\"%{_bindir}/xz\"'"
export LDFLAGS="%{?__global_ldflags}"
%make_build

%install
%make_install

%check
# https://github.com/jnovy/pxz/pull/14
./pxz -3 -c COPYING > test.xz
xz -dc test.xz > COPYING.test
cmp COPYING COPYING.test
./pxz -dc test.xz > /dev/null

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
